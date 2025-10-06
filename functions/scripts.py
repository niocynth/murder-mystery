import os
import json

def open_file(file):
    item = f"./content/{file}.json"
    if not os.path.exists(item):
        raise FileNotFoundError(f"File ./content/{file}.json does not exist")
    with open(item, 'r') as file:
        data = json.load(file)
    
    print(json.dumps(data, indent=4))

def load_story():
    # load the script to the story
    pass

def load_prop_descriptions():
    # load descriptions of the props
    pass

def load_weapon_descriptions():
    # load descriptions of the weapons
    pass

def load_cast_staff_descriptions():
    # load descriptions of the staff
    pass

def load_cast_family_descriptions():
    # load descriptions of the family members
    pass

def load_clues():
    # genuine clues
    pass

def load_red_herrings():
    # misleading clues
    pass

def load_blue_herrings():
    # counters to red herrings
    pass