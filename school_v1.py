#!/usr/bin/env python3
"""Shows children's report by activity

Print the list of children grouped by each room attended by each activity
"""
__version__ = "0.1.0"

# Data
room1 = ["Erik", "Maria", "Gustavo", "manuel", "Sofia", "Joana"]
room2 = ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]

class_english = ["Erik", "Maria", "Joana", "Carlos", "Antonio"]
class_music = ["Erik", "Carlos", "Maria"]
class_dance = ["Gustavo", "Sofia", "Joana", "Antonio"]

activities = [
    ("English", class_english),
    ("Music", class_music),
    ("Dance", class_dance),
]

# List students in each activiry by room

for name_activiry, activiry in activities:

    print(f"Student's {name_activiry} activiry\n")
    print("-" * 40)

    activity_room1 = []
    activiry_room2 = []

    for student in activiry:
        if student in room1:
            activity_room1.append(student)
        elif student in room2:
            activiry_room2.append(student)

    print("Room1", activity_room1)
    print("Room2", activiry_room2)

    print()
    print("#" * 40)