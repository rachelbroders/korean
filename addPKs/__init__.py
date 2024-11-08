from aqt import mw
from aqt.utils import showInfo
from aqt.qt import *
from aqt.qt import QAction
# utils has been added to sys.path
from utils import getKoreanVocabNotes 


def add_pks_to_all_notes():
    # Specify the name of the note type you want to update
    field_name = "pk"  # The field to store the note ID
    notes = getKoreanVocabNotes()

    for note in notes:
        if field_name in note:
            note[field_name] = str(note.id)
            note.flush()

    showInfo("Notes have been updated such that pk in anki notes matches pk in anki database.")


# Run the function
action = QAction("Update PKs", mw)
action.triggered.connect(add_pks_to_all_notes)
mw.form.menuTools.addAction(action)
