from aqt import mw
from aqt.utils import showInfo
from aqt.qt import QAction
# utils has been added to sys.path
from utils import getAllNoteTypes, NOTE_TYPES, getCardTypesFromNoteType
from .html import verb, vocab, grammar


def update_templates():
    for note_type in NOTE_TYPES:
        card_types = getCardTypesFromNoteType(note_type)
        for tmpl in card_types.get("tmpls", []):
            update_card_template(tmpl)
    # save templates - same as clicking "save" button in template editor gui
    try:
        model = mw.col.models.byName(note_type)
        mw.col.models.save(model)
    except Exception as e:
        showInfo(f"Error: cannot save updates to templates for note {note_type}!!!")
        showInfo(e)

    showInfo("Done update_templates")
    
def update_card_template(tmpl):
    try:
        card_name = tmpl.get("name")
        # VERB CARDS
        if "verb" in card_name:
            if "eng_to_kr" in card_name:
                # showInfo(f"Updating card: {card_name}")
                tmpl["qfmt"] = verb.eng_to_kr.front(card_name)
                tmpl["afmt"] = verb.eng_to_kr.back(card_name)
            else:
                # showInfo(f"Updating card: {card_name}")
                tmpl["qfmt"] = verb.kr_to_eng.front(card_name)
                tmpl["afmt"] = verb.kr_to_eng.back(card_name)
        # GRAMMAR and VOCAB cards
        else:
            # update GRAMMAR cards
            if "grammar" in card_name:
                tmpl["qfmt"] = grammar.front()
                tmpl["afmt"] = grammar.back()
            # update basic VOCAB cards
            else: 
                if "eng_to_kr" in card_name:
                    # showInfo(f"Updating card: {card_name}")
                    tmpl["qfmt"] = vocab.eng_to_kr.front()
                    tmpl["afmt"] = vocab.eng_to_kr.back()
                else:
                    # showInfo(f"Updating card: {card_name}")
                    tmpl["qfmt"] = vocab.kr_to_eng.front()
                    tmpl["afmt"] = vocab.kr_to_eng.back()
    except KeyError:
        showInfo("Error: A template in notetype ??? has no name!!")


def update_templates_old():
    card_types = getAllNoteTypes()
    
    for tmpl in card_types.get("tmpls", []):
        try:
            card_name = tmpl.get("name")
            print("working on card : " + card_name)
            # VERB CARDS
            if "verb" in card_name:
                if "eng_to_kr" in card_name:
                    # showInfo(f"Updating card: {card_name}")
                    tmpl["qfmt"] = verb.eng_to_kr.front(card_name)
                    tmpl["afmt"] = verb.eng_to_kr.back(card_name)
                else:
                    # showInfo(f"Updating card: {card_name}")
                    tmpl["qfmt"] = verb.kr_to_eng.front(card_name)
                    tmpl["afmt"] = verb.kr_to_eng.back(card_name)
            # GRAMMAR and VOCAB cards
            else:
                # update GRAMMAR cards
                if "grammar" in card_name:
                    tmpl["qfmt"] = grammar.front()
                    tmpl["afmt"] = grammar.back()
                # update basic VOCAB cards
                else: 
                    if "eng_to_kr" in card_name:
                        # showInfo(f"Updating card: {card_name}")
                        tmpl["qfmt"] = vocab.eng_to_kr.front()
                        tmpl["afmt"] = vocab.eng_to_kr.back()
                    else:
                        # showInfo(f"Updating card: {card_name}")
                        tmpl["qfmt"] = vocab.kr_to_eng.front()
                        tmpl["afmt"] = vocab.kr_to_eng.back()
        except KeyError:
            showInfo("Error: A template in notetype ??? has no name!!")
            continue
    # save templates - same as clicking "save" button in template editor gui
    try:
        mw.col.models.save(note_type)
    except Exception:
        showInfo("Error: cannot save updates to templates!!!")

    showInfo("Done update_templates")




action = QAction("Update Templates", mw)
action.triggered.connect(update_templates)
mw.form.menuTools.addAction(action)