#Rolling a Dice - Functions

import random


def  roll():
    first_number = random.randint(0,6)
    second_number = random.randint(0,6)
    return first_number,second_number

roll()
