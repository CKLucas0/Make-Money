#imports
from random import randint

#variable
money = 0
multiplier = 1

#functions
def earn(label):
    global money , multiplier
    money += multiplier
    label.config(text=f"Money: {money}$")