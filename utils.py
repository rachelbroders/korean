import subprocess
import os
import threading

from aqt import mw
from aqt.utils import showInfo


VOCAB = "KoreanVocab"
GRAMMAR = "KoreanGrammar"
NOTE_TYPES = [VOCAB, GRAMMAR]

CSV_FILE ='AnkiDatabase.csv'

DECK_MAP = {
    'Verb': {
        'eng_to_kr_verb_present': 'Verbs_ENG->KR::present',
        'eng_to_kr_verb_past': 'Verbs_ENG->KR::past',    
        'eng_to_kr_verb_future': 'Verbs_ENG->KR::future',     
        'eng_to_kr_verb_request_tense': 'Verbs_ENG->KR::request',    
        'eng_to_kr_verb_negative_request_tense': 'Verbs_ENG->KR::negative_request',   
        'eng_to_kr_verb_suggestion_tense': 'Verbs_ENG->KR::suggestion', 
        'eng_to_kr_verb_negation_past_tense': 'Verbs_ENG->KR::negation_past',
        'eng_to_kr_verb_negation_present_tense': 'Verbs_ENG->KR::negation_present',
        'eng_to_kr_verb_negation_future_tense': 'Verbs_ENG->KR::negation_future',
        'kr_to_eng_verb_present': 'Verbs_KR->ENG::present',
        'kr_to_eng_verb_past': 'Verbs_KR->ENG::past',
        'kr_to_eng_verb_future': 'Verbs_KR->ENG::future',
        'kr_to_eng_verb_request_tense': 'Verbs_KR->ENG::request',
        'kr_to_eng_verb_negative_request_tense': 'Verbs_KR->ENG::negative_request',
        'kr_to_eng_verb_suggestion_tense': 'Verbs_KR->ENG::suggestion',
        'kr_to_eng_verb_negation_past_tense': 'Verbs_KR->ENG::negation_past',
        'kr_to_eng_verb_negation_present_tense': 'Verbs_KR->ENG::negation_present',
        'kr_to_eng_verb_negation_future_tense': 'Verbs_KR->ENG::negation_future',
    },
    '': {
        'eng_to_kr': 'Korean_Vocab_ENG->KR',
        'kr_to_eng': 'Korean_Vocab_KR->ENG',
    }
}

TENSE_MAP = {
    'eng_to_kr_verb_present': 'PresentTense',
    'kr_to_eng_verb_present': 'PresentTense',
    'eng_to_kr_verb_past': 'PastTense',
    'kr_to_eng_verb_past': 'PastTense',
    'eng_to_kr_verb_future': 'FutureTense',
    'kr_to_eng_verb_future': 'FutureTense',
    'eng_to_kr_verb_request_tense': 'RequestTense',
    'kr_to_eng_verb_request_tense': 'RequestTense',
    'eng_to_kr_verb_negative_request_tense': 'NegativeRequestTense',
    'kr_to_eng_verb_negative_request_tense': 'NegativeRequestTense',
    'eng_to_kr_verb_suggestion_tense': 'SuggestionTense',
    'kr_to_eng_verb_suggestion_tense': 'SuggestionTense',
    'eng_to_kr_verb_negation_past_tense': 'NegationPastTense',
    'kr_to_eng_verb_negation_past_tense': 'NegationPastTense',
    'eng_to_kr_verb_negation_present_tense': 'NegationPresentTense',
    'kr_to_eng_verb_negation_present_tense': 'NegationPresentTense',
    'eng_to_kr_verb_negation_future_tense': 'NegationFutureTense',
    'kr_to_eng_verb_negation_future_tense': 'NegationFutureTense',
}

venv_name = 'sync_anki_to_sheets_venv'
current_directory = os.path.dirname(__file__)
DEFAULT_VENV_EXE = os.path.abspath(os.path.join(current_directory, venv_name, 'Scripts', 'python.exe'))


def getKoreanVocabNotes():
    # Get the model (note type) ID
    model = getKoreanVocabNoteType(VOCAB)
    model_id = model['id']

    # Get all notes of the specified note type
    note_ids = mw.col.db.list(
        f"SELECT id FROM notes WHERE mid = {model_id}"
    )
    return [mw.col.getNote(nid) for nid in note_ids]


def getCardTypesFromNoteType(note_type):
    # Get the model (note type) ID
    model = mw.col.models.byName(note_type)
    if not model:
        showInfo(f"Note type '{note_type}' not found.")
        return
    
    return model

def getAllNoteTypes():
    card_types = []
    # Get the model (note type) ID
    for t in learning_types:
        model = mw.col.models.byName(NOTE_TYPES[t])
        if not model:
            showInfo(f"Note type '{NOTE_TYPES[t]}' not found.")
            break
        card_types = card_types + model
    print("Card types: " + card_types)
    return card_types

def runScriptInVenv(sync_path, python_exe, expected_errors, callback=None):
    def subprocess_run():
        success = False
        if os.path.isfile(sync_path) and os.path.isfile(python_exe):
            try:
                # Run the script using the virtual environment's Python interpreter
                result = subprocess.run([python_exe, sync_path], 
                                        capture_output=True, text=True, 
                                        creationflags=subprocess.CREATE_NO_WINDOW)
    
                # Print the output of the script
                if result.stdout:
                    mw.taskman.run_on_main(lambda: showInfo(f"{result.stdout}"))
                if result.stderr and not any(substring in result.stderr for substring in expected_errors):
                    mw.taskman.run_on_main(lambda: showInfo(f"Standard Error:\n{result.stderr}"))
                else:
                    mw.taskman.run_on_main(lambda: set_success(True))
            except Exception as e:
                mw.taskman.run_on_main(lambda: showInfo(f"An error occurred while running the script:\n{str(e)}"))
        else:
            if not os.path.isfile(sync_path):
                mw.taskman.run_on_main(lambda: showInfo("Uh oh sync_path isnt found: " + sync_path))
            if not os.path.isfile(python_exe):
                mw.taskman.run_on_main(lambda: showInfo("Uh oh python_exe isnt found: " + python_exe))
        if callback:
            mw.taskman.run_on_main(lambda: callback(success))

        def set_success(value):
            nonlocal success
            success = value

    thread = threading.Thread(target=subprocess_run)
    thread.start()

