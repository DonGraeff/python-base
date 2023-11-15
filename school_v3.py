#!/usr/bin/env python3
"""Shows children's report by activity

Print the list of children grouped by each room attended by each activity
"""
__version__ = "0.1.2"

# Data
rooms = {
"room1": ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"],
"room2": ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]
}

classes = {
"english_class": ["Erik", "Maia", "Joana", "Carlos", "Antonio"],
"music_class": ["Erik", "Carlos", "Maria"],
"dance_class": ["Gustavo", "Sofia", "Joana", "Antonio"],
}

activities = {
"English": classes["english_class"],
"Music": classes["music_class"],
"Dance": classes["dance_class"],
}

# List students in each activiry by room

for name_activiry, activiry in activities.items():

    print(f"Student's {name_activiry} activiry\n")
    print("-" * 40)

    # Room1 has intersection with activiry
    activity_room1 = set(rooms["room1"]) & set(activiry)
    activiry_room2 = set(rooms["room2"]) & set(activiry)

    print("Room1", activity_room1)
    print("Room2", activiry_room2)

    print()
    print("#" * 40)