#!/usr/bin/env python3
"""Hello World Multi Languages.

Depending on the language configured in the environment the program shows the 
corresponding message.

Usage:

Have the variable LANG configurated:
EX:
    export  LANG=pt_BR

Execution:
    Python3 hello.py
    or
    ./hello.py
"""
__version__ = "0.1.2"
__author__ = "Juan Carlos"
__license__ = "Unlicense"

import os

current_languague = os.getenv("LANG","en_US")[:5]

msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Olá, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_SP": "Hola, Mundo!",
    "fr_FR": "Bonjour, Monde!",
}
print(msg[current_languague])
