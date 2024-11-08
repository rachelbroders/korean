from aqt import mw
from aqt.utils import showInfo
from aqt.qt import QAction
# utils has been added to sys.path
from utils import DECK_MAP, VOCAB

def move_cards():
    # Open the collection
    col = mw.col
    
    # Iterate through all cards
    for cid in col.db.list("select id from cards"):
        card = col.get_card(cid)
        note = card.note()
        note_type_name = note.model()['name']

        # Only working on vocab cards in this add-on (for now)
        if note_type_name != VOCAB:
            break
               
        # search non-verb decks
        for identifier, deck_name in DECK_MAP[''].items():
            if identifier in card.template()['qfmt'] or identifier in card.template()['afmt']:
                assign_card_to_deck(col, card, deck_name)
                break
        # search verb decks
        for identifier, deck_name in DECK_MAP['Verb'].items():
            if identifier in card.template()['qfmt'] or identifier in card.template()['afmt']:
                if 'Verb' in note["Verb"]:
                    assign_card_to_deck(col, card, deck_name)
                else:
                    # assign to trash
                    assign_card_to_deck(col, card, 'zzz_trash')
                break
        break
                
    showInfo("Cards have been moved based on identifiers in card templates.")


def assign_card_to_deck(col, card, deck_name):
    # Get the deck ID, creating the deck if it doesn't exist
    deck_id = col.decks.id(deck_name)
    
    # Change the card's deck
    card.did = deck_id
    col.update_card(card)


# Run the function
action = QAction("Assign Cards To Decks", mw)
action.triggered.connect(move_cards)
mw.form.menuTools.addAction(action)














