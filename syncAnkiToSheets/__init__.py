import os

from aqt import mw
from aqt.qt import QAction
from functools import partial

from utils import runScriptInVenv, DEFAULT_VENV_EXE


def sync_anki_to_sheets():
    sync_file = 'sync.py'
    current_directory = os.path.dirname(__file__)
    sync_path = os.path.abspath(os.path.join(current_directory, sync_file))
    expected_errors = ["44: MarkupResemblesLocatorWarning"]
    runScriptInVenv(sync_path, DEFAULT_VENV_EXE, expected_errors)


# Attach subprocess script to be accessible from Anki
action = QAction("Sync to Google Sheets", mw)
action.triggered.connect(partial(sync_anki_to_sheets))
mw.form.menuTools.addAction(action)