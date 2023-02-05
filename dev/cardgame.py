"""
cardgame.py
"""

from dev.deck.deck import Deck


user_action: str = ""


def game_over() -> bool:
    """
    :return: True if game over; else false
    """
    return user_action == "exit"


deck = Deck()
deck.shuffle()

# Main game loop
while not game_over():
    user_action = input()
    if user_action == "shuffle":
        deck.shuffle()
        print("Deck shuffled")
        print(f"Top card: {deck.peek_card()}")
    elif user_action == "draw":
        card = deck.draw_card()
        print(card)
