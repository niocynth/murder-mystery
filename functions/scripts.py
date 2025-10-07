import os
import json
from constants.defaults import *

def open_file(file):
    item = f"./content/{file}.json"
    if not os.path.exists(item):
        raise FileNotFoundError(f"File ./content/{file}.json does not exist")
    with open(item, 'r') as file:
        data = json.load(file)
    return data

def load_story():
    # load the script to the story
    data = open_file("story")
    pass

def load_rooms(num_rooms=(MAP_HEIGHT*MAP_WIDTH)):
    data = open_file("rooms")
    pass

def load_weapons(num_weapons=WEAPONS):
    # load descriptions of the weapons
    data = open_file("weapons")
    pass

def load_cast_staff(num_staff=STAFF):
    # load descriptions of the staff
    pass

def load_cast_family(num_family=FAMILY):
    # load descriptions of the family members
    pass

def load_clues(num_clues=CLUES):
    # genuine clues
    load_red_herrings(num_clues)
    pass

def load_red_herrings(num_clues):
    num_red_herrings = num_clues * 2
    # misleading clues
    
    pass

def load_blue_herrings(red_herrings):
    # counters to red herrings
    pass