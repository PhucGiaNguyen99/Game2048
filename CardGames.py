# Using Monte Carlo for the cards games

# Calculate the probability that at least 2 Kings will appear next to each other in the shuffled deck
""" The probability is equal to 1- P(no consecutive Kings)
49P4 x 48!
so, the result is 1- above/52!
"""
import copy
from random import random


# Method to check if 2 Kings are next to each other
def KingKing(deck):
    for i in range(len(deck) - 1):
        if deck[i][1] == 'K' and deck[i + 1][1] == 'K':
            return True


def MonteCarlo(orig_deck, n):
    res = 0
    for i in range(n):
        deck = copy.deepcopy(orig_deck)
        random.shuffle(deck)
        if KingKing(deck):
            res += 1
    return res / n * 100


# Calculate the probability that at least one King and one Quuen will be next to each other or one card away?

# Calculate how many case that King is next to Queen or King and Queen with distance of 1
def King_queen(deck):
    n = len(deck)
    for i in range(n - 1):
        if deck[i][1] + deck[i + 1][1] in ['KQ', 'QK']:
            return True
        # Not the 2 positions before the last element
        if i != n - 2:
            if deck[i][1] + deck[i + 2][1] in ['KQ', 'QK']:
                return True
