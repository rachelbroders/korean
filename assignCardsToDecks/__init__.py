from aqt import mw
from aqt.utils import showInfo
from aqt.qt import QAction
from bs4 import BeautifulSoup
# utils has been added to sys.path
from utils import DECK_MAP, VOCAB

def move_cards():
    # Open the collection
    col = mw.col
    card_ids = col.db.list("select id from cards")
    # Iterate through all cards
    for cid in card_ids:
        card = col.get_card(cid)
        note = card.note()
        note_type_name = note.model()['name']
        card_id_front = extract_card_identifier(card.template()['qfmt'])
        card_id_back = extract_card_identifier(card.template()['afmt'])

        # Only working on vocab cards in this add-on (for now)
        if note_type_name != VOCAB:
            continue

        assignee_deck = None
        verb_note = True if get_field_by_name(note, 'PresentTense') != "" else False
        verb_template = 'verb' in card_id_front or 'verb' in card_id_back

        if (not verb_note) and verb_template:
            assignee_deck = 'zzz_trash'
        else: 
            assignee_deck = DECK_MAP[card_id_front]

        assign_card_to_deck(col, card, assignee_deck)

                
    showInfo("Cards have been moved based on identifiers in card templates.")


def assign_card_to_deck(col, card, deck_name):
    # Get the deck ID, creating the deck if it doesn't exist
    deck_id = col.decks.id(deck_name)
    
    # Change the card's deck
    card.did = deck_id
    col.update_card(card)


def get_field_by_name(note, field_name):
    model = note.model()
    field_names = model['flds']
    field_name_to_index = {field['name']: idx for idx, field in enumerate(field_names)}

    if field_name in field_name_to_index:
        field_value = note.fields[field_name_to_index[field_name]]
    else:
        print(f"Field '{field_name}' not found.")
    return field_value
 
def extract_card_identifier(template):
    soup = BeautifulSoup(template, 'html.parser')
    element = soup.find(class_="identifier")
    value=""
    if element:
        value = element.text.strip()  # .text gives the text inside the element
    return value

# Run the function
action = QAction("Assign Cards To Decks", mw)
action.triggered.connect(move_cards)
mw.form.menuTools.addAction(action)














