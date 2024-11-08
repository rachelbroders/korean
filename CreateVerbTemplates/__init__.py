import os
from string import Template

from aqt import mw
from aqt.utils import showInfo
from aqt.qt import QAction

# utils has been added to sys.path
from utils import NOTE_TYPES, getCardTypesFromNoteType, TENSE_MAP
from .html import common



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
        # set type
        if "verb" in card_name:
            type = "verb"
        elif "grammar" in card_name:
            type = "grammar"
        else:
            type = "vocab"

        # set eng_to_kr (note that it will be set to 0 for grammar cards even though its also 
        # not kr_to_eng but this is accounted for in "create_file_path" function)
        eng_to_kr = 1 if "eng_to_kr" in card_name else 0

        cur_dir = os.path.dirname(__file__)
        tmpl["qfmt"] = read_html(1, cur_dir, card_name, type, eng_to_kr)
        tmpl["afmt"] = read_html(0, cur_dir, card_name, type, eng_to_kr)

    except KeyError as e:
        showInfo(e)


def read_html(side, cur_dir, card_name, type, eng_to_kr):
    file_path = create_file_path(type, eng_to_kr, side)
    full_path = os.path.join(cur_dir, file_path)

    # Read the HTML file
    with open(full_path, 'r', encoding='utf-8') as file:
        template = Template(file.read())
        # content = file.read()

    html_var = {}
    if type == "verb":
        html_var = {
            'card_type': card_name,
            'eng_tense': TENSE_MAP[card_name] + 'English',
            'kr_tense': TENSE_MAP[card_name],
            'audio': common.audio(card_name),
            'more_info': common.more_info(),
            'duplicateScript': common.duplicateScript(card_name)
        }

    return template.safe_substitute(html_var)


def create_file_path(type, eng_to_kr, front):
    lang = "eng_to_kr" if eng_to_kr==1 else "kr_to_eng"
    side = "front" if front==1 else "back"
    file_path = "html\\" + type + "\\" + (type if type=="grammar" else lang)  + "_" + side + ".html"
    return file_path


def html_var_sub(card_name, content):
    html_var = {
        'card_type': card_name,
        'eng_tense': TENSE_MAP[card_name] + 'English',
        'kr_tense': TENSE_MAP[card_name],
        'audio': common.audio(card_name),
        'more_info': common.more_info(),
        'dup_script': common.duplicateScript(card_name)
    }

    for key, value in html_var.items():
        content = content.replace(f'{key}', value)
        # showInfo("Replacing {" + key + "} with " + value + "\n\nNew content: \n" + content)

    return content


action = QAction("Update Templates", mw)
action.triggered.connect(update_templates)
mw.form.menuTools.addAction(action)