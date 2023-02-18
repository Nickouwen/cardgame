import logging

from playground.services.nics_game_service import \
    NicsGameService as GameService

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
    game = GameService.create_game(
        name=game_name,
        player1_name=player1_name,
        player2_name=player2_name
    )

    # Main game loop
    user_action = ""

    while not game_over(user_action):
        user_action = input("Enter an action: ")
        if user_action == "shuffle":
            logger.info('Shuffling')
            deck = GameService.shuffle_deck(game_id=game['id'])
        elif user_action == "draw":
            logger.info('Drawing 1')
            card = GameService.draw_card(
                table_id=game['table_id'], player_id=game['player1_id'])
        elif user_action.startswith("draw"):
            number = user_action.split(maxsplit=1).pop()
            logger.info(f'Drawing {number}')
            try:
                i = int(number)
                for _ in range(i):
                    GameService.draw_card(
                        table_id=game['table_id'], player_id=game['player1_id'])
            except ValueError:
                print(f"Error drawing this number of cards: {number}")
        elif user_action == "deal":
            logger.info('Dealing')
            for i in range(1, 11):
                GameService.draw_card(
                    table_id=game['table_id'], player_id=game['player1_id'])
        elif user_action == "show":
            logger.info('Showing hand')
            GameService.get_hand(player_id=game['player1_id'])
        elif user_action.startswith("play"):
            logger.info('Playing card')
            action = user_action.split()
            if len(action) == 3:
                card_number = int(user_action.split()[1])
                pile_number = int(user_action.split()[2])
                GameService.play_card(card_number=card_number,
                                      pile_number=pile_number)
