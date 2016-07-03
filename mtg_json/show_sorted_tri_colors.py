import json

file_name = "mtg_card_db.json"

mtg_db = json.loads(open(file_name).read())

# sorts by the color wheel
wubrg_order = {
    "W": 0,  # white
    "U": 1,  # blue
    "B": 2,  # black
    "R": 3,  # red
    "G": 4   # green
}

# sort by alara shards, then tarkir guilds.
tri_color_order = {
    "WUG": 0,   # Bant
    "WUB": 1,   # Esper
    "UBR": 2,   # Grixis
    "BRG": 3,   # Jund
    "WRG": 4,   # Naya
    "WUG": 5,   # Abzan
    "WUB": 6,   # Jeskai
    "UBR": 7,   # Sultai
    "BRG": 8,   # Mardu
    "URG": 9    # Temur
}


def query_by_number_of_colors(card_db, num_of_colors):
    # returns a list of card names that have the desired
    #    number of colors in their color identidy.
    # card_db = MTG json of cards, as dict
    # num_of_colors = int number of colors to select
    #   between 1 and 5
    # Colorless is not yet supported

    card_list = []  # list to be returned.
    for card_name in card_db:
        card_dict = card_db[card_name]
        if("colorIdentity" in card_dict.keys()):
            # Colorless cards do not have color identidy
            if(len(card_dict["colorIdentity"]) == num_of_colors):
                if(card_name not in card_list):
                    card_list.append(card_name)
    return card_list


def bucket_by_tricolor(card_db):
    # Buckets the number of cards by distinct tri-color
    #     combinations.
    tri_color = query_by_number_of_colors(
        card_db=mtg_db,
        num_of_colors=3
    )
    distinct_colors = []

    for card_name in tri_color:
        color_identidy_list = mtg_db[card_name]['colorIdentity']
        # sort by wubrg color order
        color_identidy_list.sort(key=lambda val: wubrg_order[val[0]])
        color_type_str = "".join(color_identidy_list)
        if(color_type_str not in distinct_colors):
            distinct_colors.append(color_type_str)

    for color in distinct_colors:
        print(color)


bucket_by_tricolor(card_db=mtg_db)

# print(",".join(print_output).encode('utf-8'))
input("Press Enter to close...")