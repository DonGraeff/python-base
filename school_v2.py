#!/usr/bin/env python3
"""Shows children's report by activity

Print the list of children grouped by each room attended by each activity
"""
__author__ = "Juan Carlos"
__version__ = "0.1.0"
__license__ = "Unlicense"

# Data
room1 = ["Erik", "Maria", "Gustavo", "manuel", "Sofia", "Joana"]
room2 = ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]

english_class = ["Erik", "Maria", "Joana", "Carlos", "Antonio"]
music_class = ["Erik", "Carlos", "Maria"]
dance_class = ["Gustavo", "Sofia", "Joana", "Antonio"]

activities = [
    ("English", english_class),
    ("Music", music_class),
    ("Dance", dance_class),
]

# List students in each activiry by room

for name_activiry, activiry in activities:

    print(f"Student's {name_activiry} activiry\n")
    print("-" * 40)

    # Room1 has intersection with activiry
    activity_room1 = set(room1) & set(activiry)
    activiry_room2 = set(room2) & set(activiry)

    print("Room1", activity_room1)
    print("Room2", activiry_room2)

    print()
    print("#" * 40)