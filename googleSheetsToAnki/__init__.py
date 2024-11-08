import os

from aqt import mw
from aqt.qt import QAction
from functools import partial
from aqt.utils import showInfo

from utils import runScriptInVenv, DEFAULT_VENV_EXE
from addPKs import add_pks_to_all_notes
from assignCardsToDecks import move_cards
from .csvToAnki import import_csv_file


def runScriptInVenvWrapper(script_path, python_exe, expected_errors):
    def callback(result):
        if result:
            success = import_csv_file()
            # if not success:
            #     return
            # add_pks_to_all_notes()
            # move_cards()
            showInfo("Entire process complete!")
        else:
            showInfo("Script did not run successfully.")

    runScriptInVenv(script_path, python_exe, expected_errors, callback)

# Set variables for locations of files needed to run subprocess
script_file = 'googleSheetsToCsv.py'
current_directory = os.path.dirname(__file__)
script_path = os.path.abspath(os.path.join(current_directory, script_file))


# Attach subprocess script to be accessible from Anki
action = QAction("Import from Google Sheets", mw)
action.triggered.connect(partial(runScriptInVenvWrapper, script_path, DEFAULT_VENV_EXE, []))
mw.form.menuTools.addAction(action)