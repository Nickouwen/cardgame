"""
cardgame.py
"""
from deck.deck import Deck
from deck.exception.card_not_found_error import CardNotFoundError
from deck.hand import Hand


user_action: str = ""


def game_over() -> bool:
    """
    :return: True if game over; else false
    """
    return user_action == "exit"


deck = Deck()
deck.shuffle()

hand = Hand()

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
    elif user_action == "deal":
        hand.add_card(deck.draw_card())
        hand.add_card(deck.draw_card())
        hand.add_card(deck.draw_card())
    elif user_action.startswith("draw"):
        number = user_action.split(maxsplit=1).pop()
        try:
            i = int(number)
            for _ in range(i):
                hand.add_card(deck.draw_card())
        except ValueError:
            print(f"Error drawing this number of cards: {number}")
    elif user_action == "show":
        for card in hand.get_hand():
            print(card)
    elif user_action.startswith("play"):
        card = user_action.split(maxsplit=1).pop()
        try:
            played_card = hand.play_card(int(card))
            print(f"Played card: {played_card}")
        except CardNotFoundError:
            print("Card not in hand")
        except ValueError:
            print(f"Error finding this card: {card}")
