import requests
from bs4 import BeautifulSoup

import pandas as pd
import os, sys

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, parent_dir)

from venv_utils import SPREADSHEET_ID, DATASHEET, DATASHEET, get_sheet


# AnkiConnect API setup
def invoke(action, **params):
    return requests.post('http://localhost:8765', json={
        'action': action,
        'version': 6,
        'params': params
    }).json()


def get_all_notes(note_type):
    result = invoke('findNotes', query=f'note:"{note_type}"')
    
    if 'result' in result:
        notes_info = invoke('notesInfo', notes=result['result'])
        return notes_info['result']
    else:
        return []


def get_field_names(note_type):
    result = invoke('modelFieldNames', modelName=note_type)
    if 'result' in result:
        # remove pk from fields because we want to extract this from the SQL database and not from the Anki column
        result['result'].remove('pk')
        return result['result']
    else:
        raise Exception(f"Failed to get fields for note type '{note_type}': {result}")


# Function to strip HTML tags and decode entities
def normalize_text(text):
    soup = BeautifulSoup(text, 'html.parser')
    return soup.get_text()


def process_anki_notes(notes_data, fields):
    data = []
    for note in notes_data:
        note_data = []
        note_id = note['noteId']
        tags = ' '.join(note['tags'])  # Concatenate tags into a single string
        for field in fields:
            note_data.append(normalize_text(note['fields'][field]['value']))
        data.append([note_id] + note_data + [tags])
    df = pd.DataFrame(data, columns = ['#pk'] + ['#' + f for f in fields] + ['#tags'])   
    return df
 

def upload_to_sheets(df, sheet):
    dup = "#Duplicates"
    duplicates_col_index = df.columns.get_loc(dup)

    # Select data to the left and right of the duplicates column
    left_values = df.iloc[:, :duplicates_col_index].values.tolist()   # Get left column values
    right_values = df.iloc[:, duplicates_col_index + 1:].values.tolist()   # Get left column values
 
    # Figure out where the duplicates column is in the spreadsheet
    header = get_header(sheet)
    if dup in header:
        column_index = header.index(dup) + 1  # +1 for 1-based index
    else:
        raise ValueError(f"Column {dup} not found in the header.".format(dup))
    
    # create spreadsheet ranges to the left and right of the duplicates column
    left_range = f"{DATASHEET}!A2:{index_to_column_letter(column_index-1)}"
    print("left range: {0}".format(left_range))
    right_range = f"{DATASHEET}!{index_to_column_letter(column_index+1)}2:{index_to_column_letter(len(header))}"
    print("right range: {0}".format(right_range))
    
    update_sheet(sheet, left_values, left_range)
    update_sheet(sheet, right_values, right_range)


def index_to_column_letter(index):
    """Convert a 1-based column index to a Google Sheets column letter."""
    letter = ''
    while index > 0:
        index -= 1
        letter = chr(index % 26 + 65) + letter
        index //= 26
    return letter


def update_sheet(sheet, values, range):
    body = {
        'values': values
    }
    result = sheet.values().update(
        spreadsheetId=SPREADSHEET_ID,
        range=range,
        valueInputOption='RAW',
        body=body
    ).execute()
    print('{0} cells updated.'.format(result.get('updatedCells')))


def get_header(sheet):
    header_response = sheet.values().get(
        spreadsheetId=SPREADSHEET_ID,
        range=DATASHEET
    ).execute()
    
    header = header_response.get('values', [])[0]  # Get the first row as header
    return header 

def sync_from_anki_to_sheets():
    # Fetch cards data from Anki
    note_type = "KoreanVocab"
    fields = get_field_names(note_type)
    notes_data = get_all_notes(note_type)
    df = process_anki_notes(notes_data, fields)
    sheet = get_sheet()
    upload_to_sheets(df, sheet)


if __name__ == "__main__":
    sync_from_anki_to_sheets()