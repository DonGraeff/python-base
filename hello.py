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
__version__ = "0.0.1"
__author__ = "Juan Carlos"
__license__ = "Unlicense"

from os import getenv

current_languague = getenv("LANG","en_US")[:5]

msg = "Hello, World!"

if current_languague == "pt_BR":
    msg = "Olá, Mundo!"
elif current_languague == "it_IT":
    msg= "Ciao, Mondo!"
elif current_languague == "es_SP":
    msg= "Hola, Mundo!"
elif current_languague == "fr_FR":
    msg= "Bonjour Monde"

print (msg)
