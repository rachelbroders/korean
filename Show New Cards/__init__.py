from aqt import mw
from aqt.qt import *
from aqt.utils import showInfo
from anki.collection import SearchNode

def show_new_cards_today():
    # Get the current collection (deck)
    col = mw.col
    if not col:
        showInfo("No collection loaded.")
        return

    # Get today's date in the format used by Anki
    today = col.sched.today

    # Get all deck names and IDs
    deck_names_and_ids = col.decks.all_names_and_ids()

    results = []
    
    for deck in deck_names_and_ids:
        deck_id = deck.id
        deck_name = deck.name
        if deck_name == 'trash':
            continue
        # Find all new cards for today in the current deck
        new_cards_today = col.find_cards(f"deck:{deck_name} prop:due=0")
        
        if new_cards_today:
            card_details = []
            for card_id in new_cards_today:
                card = col.get_card(card_id)
                if card.due == today:  # Ensure the card is due today
                    note = card.note()
                    english = note['English']
                    korean = note['Korean']
                    card_details.append(f"English: {english}, Korean: {korean}")
                
            if card_details:
                card_details_str = "\n".join(card_details)
                results.append(f"Deck '{deck_name}':\n{card_details_str}")

    if not results:
        showInfo("No new cards for today.")
        return

    # Combine results into a single message
    message = "\n\n".join(results)

    # Display the message
    showInfo(message)

# Add a menu item to trigger the function
action = QAction("Show New Cards Today (All Decks)", mw)
action.triggered.connect(show_new_cards_today)
mw.form.menuTools.addAction(action)