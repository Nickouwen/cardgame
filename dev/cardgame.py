"""
cardgame.py
"""

from dev.deck.deck import Deck


deck = Deck()
deck.shuffle()

card = deck.draw_card()

print(card)
