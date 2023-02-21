import logging

from ..models.card_model import Card
from ..models.cardcollection_model import CardCollection
from ..models.game_model import Game
from ..models.player_model import Player
from ..models.table_model import Table

logger = logging.getLogger(__name__)


class NicsGameService:
    """
    Nic: Edit code below this
    """
    _games = []

    def create_game(
        self,
        name: str,
        player1_name: str = 'Player 1',
        player2_name: str = 'Player 2'
    ) -> Game:
        """
        Create a game that has a table with a deck and 2 players, each with a
        hand of 10 cards dealt from the deck
        """
        logger.info('Creating new game')

        game = Game(id=1, name="Test Game")
        game.table.players.append(Player(player1_name))
        game.table.players.append(Player(player2_name))
        self._games.append(game)

        return game

    def draw_card(self, deck: CardCollection, hand: CardCollection) -> Card:
        """
        Removes the top card from CardCollection 'deck'
        and adds it to the CardCollection 'hand'
        """
        logger.info("Drawing a card from deck")

        return Card(number=1, suit=Card.SPADES, point_value=0)

    def get_hand(self, player: Player) -> CardCollection:
        """
        Gets the player's CardCollection 'hand'
        """
        return CardCollection()

    def play_card(self, card: Card, pile: CardCollection) -> bool:
        """
        Moves card from whichever hand it is in and adds it to
        the card pile on the table
        """
        logger.info("Playing a card")
        return False

    def shuffle_deck(self, deck: CardCollection) -> None:
        """
        Shuffles the CardCollection 'deck'
        """
        logger.info('Shuffling card collection')
