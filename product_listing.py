#!/usr/bin/env python3
"""Product listing"""
__version__ = "0.1.0"
__author__ = "Juan Carlos"
__license__ = "Unlicense"

from pprint import pprint

product = {
    "name": "Pencil",
    "colors": ["blue", "white"],
    "price": 3.23,
    "dimension": {
        "height": 12.1,
        "width": 0.8
    },
    "in_stock": True,
    "code": 45678,
    "codebar": None
}

client = {"name": "Bruno"}

purchase = {
    "client": client,
    "product": product,
    "amount": 3
}

# pprint(purchase)

total_purchase = purchase["amount"] * purchase["product"]["price"]

print(
    f" The client {purchase['client']['name']}"
    f" purchased {purchase['amount']} items of {purchase['product']['name']}"
    f" and paid the total of {total_purchase}"
)