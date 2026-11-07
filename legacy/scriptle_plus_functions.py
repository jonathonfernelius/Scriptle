import json
import random

with open('scriptures.json') as scriptures_file:
    scriptures = json.load(scriptures_file)

def select_scriptures(scripture_selection):
    match scripture_selection:
        case 'Book of Mormon':
            scripture_list = [entry for entry in scriptures if entry["volume_title"] == "Book of Mormon"]
        case 'New Testament':
            scripture_list = [entry for entry in scriptures if entry["volume_title"] == "New Testament"]
        case 'Old Testament':
            scripture_list = [entry for entry in scriptures if entry["volume_title"] == "Old Testament"]
        case _:
            scripture_list = scriptures
    
    return scripture_list

def get_scripture(scripture_list):
    return scripture_list[random.randint(0,len(scripture_list)-1)]