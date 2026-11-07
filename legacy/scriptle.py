import random
import json

with open('scriptures.json') as scriptures_file:
    scriptures = json.load(scriptures_file)

bom_only = [entry for entry in scriptures if entry["volume_title"] == "Book of Mormon"]

scripture_num = len(bom_only)
bom_num = len(bom_only)
print(scripture_num)

while True:
    print()
    menu_choice = input('Scripture Guessing Game' \
                      '\n=======================' \
                      '\n1) Play a round' \
                      '\n2) Check high scores' \
                      '\n3) Exit\n')
    match menu_choice:
        case '1': # Game
            print()
            # random_scripture = scriptures[random.randint(0,scripture_num-1)]
            # print(random_scripture['scripture_text'])
            random_scripture = bom_only[random.randint(0,bom_num-1)]
            print(random_scripture['scripture_text'])
            scripture_guess = input('What book is this scripture from: ')
            print(random_scripture['verse_title'])
        case '2': # High scores
            pass
        case '3': # Exit
            print('Goodbye')
            break
        case _: # Invalid input
            print('Invalid input. Try again.')