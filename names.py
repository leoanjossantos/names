import random

lista_nomes = [
    "Leandro",
    "Roselma",
    "Jessica",
    "Gil",
    "Renata",
    "Mauricio"
]

def get_name():
    chosen_name = random.choice(lista_nomes)
    return chosen_name
