# Give cards pks, assign them to decks and then sync to google sheets (so pks are in sheets) when import done
import os
from aqt import mw
from aqt.utils import showInfo
import pprint

from anki.importing.csvfile import TextImporter

from utils import CSV_FILE, NOTE_TYPES

def import_csv_file():
    # Path to the CSV file you want to import
    csv_path = os.path.join(os.path.dirname(__file__), CSV_FILE)
    
    # Check if the file exists
    if not os.path.isfile(csv_path):
        showInfo(f"CSV file not found: {csv_path}")
        return False
    
    # Create a TextImporter instance
    importer = TextImporter(mw.col, csv_path)
    importer.delimiter = "," 
    # Set the note type (model)
    model = mw.col.models.byName(NOTE_TYPES["vocab"])
    importer.model = model
    # Perform the import
    importer.run()


    
    # Confirm the import
    file_path = 'C:\\Users\\rache\\AppData\\Roaming\\Anki2\\addons21\\debug.txt'
    # Open the file in write mode
    with open(file_path, 'w') as f:
        # Use the print function to write to the file
        print(pprint.pformat(vars(importer)), file=f)
        pprint(importer.foreignNotes)
    
    # Display the import summary
    summary = (
        f"Import Summary:\n\n"
        f"Notes Ignored: {importer.ignored}\n"
        f"Notes Updated: {importer.updateCount}\n"
        f"Total Notes Processed: {importer.total}\n"
    )
    showInfo(summary)
    settings = (
        f"Import Settings:\n\n"
        # f"deck: {importer.deck}\n"
        f"existing notes: {importer.importMode}\n"
    )
    showInfo("import settings:\n\n"+ settings)


    # Compare to (manual):
    # 1,032 notes found in file. Of those:
    #  883 notes already present in your collection. 
    #  149 notes were used to update existing ones. 
    # My add-on:
    # Notes Ignored: 0
    #Notes Updated: 129
    #Total Notes Processed: 1012
    return True


