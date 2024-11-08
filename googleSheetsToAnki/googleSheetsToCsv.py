import os
import csv
import sys 

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, parent_dir)

from venv_utils import get_sheet, SPREADSHEET_ID, DATASHEET, ScriptError, CSV_FILE
  

def get_google_sheets_data():
    sheet = get_sheet()
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=DATASHEET).execute()
    values = result.get('values', [])
    return values


def write_data_to_csv(data):
    # Write data to csv file
    try:
        csv_path = os.path.join(os.path.dirname(__file__), CSV_FILE)
        with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(data)
    except Exception as e:
        ScriptError(e)


def main():
    data = get_google_sheets_data()
    if not data:
        raise ScriptError('No data found in Google Sheets.')
    write_data_to_csv(data)


if __name__ == "__main__":
    main()