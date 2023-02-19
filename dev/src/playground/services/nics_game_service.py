import logging

from cardgame.interfaces import IGameService

from ..models import *

logger = logging.getLogger(__name__)


def create_deck(*, table_id: int) -> TableCardCollection:
    cards = []          # The cards that will be in this deck
    # A CardCollection object to name our deck
    cardcollection = CardCollection(name="Deck")

    # Create each card with the appropriate point value
    for i in range(1, 105):
        if i == 55:
            point_value = 7
        elif i % 11 == 0:
            point_value = 5
        elif i % 10 == 0:
            point_value = 3
        elif i % 5 == 0:
            point_value = 2
        else:
            point_value = 1
        cards.append(Card(number=i, suit=Card.NONE,
                          point_value=point_value).id)
    cardcollection.card_ids = cards
    return TableCardCollection(table_id=table_id, collection_id=cardcollection.id)


class NicsGameService(IGameService):
    """
    Nic: Edit code below this
    """
    @staticmethod
    def create_game(
        *,
        name: str,
        player1_name: str = 'Player 1',
        player2_name: str = 'Player 2'
    ) -> dict:
        logger.info('Creating new game')

        game = Game(name=name)
        table = Table(game_id=game.id)
        deck = create_deck(table_id=table.id)
        player1 = Player(name=player1_name, game_id=game.id)
        player2 = Player(name=player2_name, game_id=game.id)

        return {
            'id': game.id,
            'name': game.name,
            'round_number': game.round_number,
            'started_at': game.started_at,
            'status': game.status,
            'table_id': table.id,
            'deck_id': deck.id,
            'player1_id': player1.id,
            'player1_name': player1.name,
            'player2_id': player2.id,
            'player2_name': player2.name,
        }

    @staticmethod
    def get_game(*, id: int) -> dict:
        logger.info('Getting game')

        game = Game.games.get(id)
        if game:
            return {
                'id': game.id,
                'name': game.name,
                'round_number': game.round_number,
                'started_at': game.started_at,
                'status': game.status
            }

        return {}

    @staticmethod
    def update_game(*, id: int, new_name: str) -> dict:
        logger.info('Updating game')
        if not isinstance(id, int):
            return {}

        Game.games[id].name = new_name
        game = Game.games[id]
        return {
            'id': game.id,
            'name': game.name,
            'round_number': game.round_number,
            'started_at': game.started_at,
            'status': game.status
        }

    @staticmethod
    def delete_game(*, id: int) -> bool:
        logger.info('Deleting game')

        if id in Game.games:
            del Game.games[id]
            return True

        return False

    @staticmethod
    def create_table(*, game_id: int, table_name: str) -> dict:
        logger.info('Creating table')
        return {}

    @staticmethod
    def get_table(*, id: int) -> dict:
        logger.info('Getting table')
        return {}

    @staticmethod
    def update_table(*, id: int, new_name: str) -> dict:
        logger.info('Updating table')
        return {}

    @staticmethod
    def delete_table(*, id: int) -> bool:
        logger.info('Deleting table')
        return False

    @staticmethod
    def create_player(*, name: str) -> dict:
        logger.info('Creating player')
        return {}

    @staticmethod
    def get_player(*, id: int) -> dict:
        logger.info('Getting player')
        return {}

    @staticmethod
    def update_player(*, id: int, new_name: str) -> dict:
        logger.info('Updating player')
        return {}

    @staticmethod
    def delete_player(*, id: int) -> bool:
        logger.info('Deleting player')
        return False

    @staticmethod
    def create_cardcollection(*, name: str) -> dict:
        logger.info('Creating card collection')
        return {}

    @staticmethod
    def get_cardcollection(*, id: int) -> dict:
        logger.info('Getting card collection')
        return {}

    @staticmethod
    def update_cardcollection(*, id: int, new_name: str) -> dict:
        logger.info('Updating card collection')
        return {}

    @staticmethod
    def delete_cardcollection(*, id: int) -> bool:
        logger.info('Deleting card collection')
        return False

    @staticmethod
    def create_playercardcollection(*, name: str) -> dict:
        logger.info('Creating player card collection')
        return {}

    @staticmethod
    def get_playercardcollection(*, id: int) -> dict:
        logger.info('Getting player card collection')
        return {}

    @staticmethod
    def update_playercardcollection(*, id: int, new_name: str) -> dict:
        logger.info('Updating player card collection')
        return {}

    @staticmethod
    def delete_playercardcollection(*, id: int) -> bool:
        logger.info('Deleting player card collection')
        return False

    @staticmethod
    def create_tablecardcollection(*, name: str) -> dict:
        logger.info('Creating table card collection')
        return {}

    @staticmethod
    def get_tablecardcollection(*, id: int) -> dict:
        logger.info('Getting table card collection')
        return {}

    @staticmethod
    def update_tablecardcollection(*, id: int, new_name: str) -> dict:
        logger.info('Updating table card collection')
        return {}

    @staticmethod
    def delete_tablecardcollection(*, id: int) -> bool:
        logger.info('Deleting table card collection')
        return False

    """
    Game specific logic goes below here
    """
    @staticmethod
    def draw_card(*, table_id: int, player_id: int) -> dict:
        """
        Draws the top card from TableCardCollection 'deck'
        and adds it to the PlayerCardCollection 'hand'
        Returns: dict { key: card_attr, value: attr_value }
        """
        logger.info("Drawing a card from deck")
        return {}

    @staticmethod
    def get_hand(*, player_id: int) -> dict:
        """
        Gets the PlayerCardCollection 'hand'
        Returns: dict { key: order_number, value: card_number }
        """
        return {}

    @staticmethod
    def play_card(*, card_number: int, pile_number: int) -> bool:
        """
        Moves card with card_number to collection with pile_number
        Returns: True if this is a legal action that is completed
        """
        logger.info("Playing a card")
        return False

    @staticmethod
    def shuffle_deck(*, game_id: int) -> dict:
        """
        Shuffles the TableCardCollection 'deck'
        Returns: dict { key: order_number, value: card_number }
        """
        logger.info('Shuffling card collection')
        return {}
