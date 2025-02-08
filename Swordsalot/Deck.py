
import os
import Card

class Deck:
    quantity = 0
    cards = []

    def __init__(self, cards: list):
        sum = 0
        for card in cards:
            sum += card.quantity
        self.quantity = sum
        self.cards = cards

    def __str__(self):
        print("This deck contains:")
        for card in self.cards:
            print(card)
        return ""


class Discard(Deck):
    pass

slash = Card.Slash(5, 5)
block = Card.Shield(5, 5)
charge = Card.Charge(2, 2)
retreat = Card.Retreat(2, 2)
strafe = Card.Strafe(2, 2)
walk = Card.Walk(2, 1)

blueDeck = Deck([slash, block, charge, retreat, strafe, walk])
print(blueDeck)
