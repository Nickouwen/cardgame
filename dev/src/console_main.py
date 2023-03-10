import logging

from playground.services.nics_game_service import NicsGameService

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)
    logger.setLevel(level='DEBUG')

    def game_over(user_action) -> bool:
        """
        :return: True if game over; else false
        """
        return user_action == "exit"

    game_name = input("Enter a name for the new game: ")
    player1_name = input("Enter a name for player 1: ")
    player2_name = input("Enter a name for player 2: ")

    game_service = NicsGameService()
    game = game_service.create_game(
        name=game_name,
        player1_name=player1_name,
        player2_name=player2_name
    )

    # Main game loop
    user_action = ""
    current_player = game.table.players[0]

    while not game_over(user_action):
        print(f"It is {current_player.name}'s turn.")
        user_action = input("Enter an action: ")
        if user_action == "shuffle":
            logger.info('Shuffling')
            game.table.deck = game_service.shuffle_deck(game.table.deck)
        elif user_action == "draw":
            logger.info('Drawing 1')
            card = game_service.draw_card(game.table.deck, current_player)
        elif user_action.startswith("draw"):
            number = user_action.split(maxsplit=1).pop()
            logger.info(f'Drawing {number}')
            try:
                i = int(number)
                for _ in range(i):
                    game_service.draw_card(
                        game.table.deck, current_player.hand)
            except ValueError:
                print(f"Error drawing this number of cards: {number}")
        elif user_action == "deal":
            logger.info('Dealing')
            for i in range(1, 11):
                game_service.draw_card(game.table.deck, current_player.hand)
        elif user_action == "show":
            logger.info('Showing hand')
            print(current_player.hand)
        elif user_action.startswith("play"):
            logger.info('Playing card')
            action = user_action.split()
            if len(action) == 3:
                card_number = int(user_action.split()[1])
                pile_number = int(user_action.split()[2])
                if current_player.hand.cards.get(card_number):
                    game_service.play_card(current_player.hand[card_number],
                                           game.table.piles[pile_number])
