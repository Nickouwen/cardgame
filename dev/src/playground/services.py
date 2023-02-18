import logging

from cardgame.interfaces import IGameService

from .interfaces import CardgameInterface
from .models import Game

logger = logging.getLogger(__name__)


class NicsGameService(IGameService):

    """
    Nic: Edit code below this
    """
    @staticmethod
    def create_game(*, name: str) -> dict:
        logger.info('Creating new game')
        game = Game()
        game.name = name
        return {
            'id': game.id,
            'name': game.name,
            'round_number': game.round_number,
            'started_at': game.started_at,
            'status': game.status,
        }

    @staticmethod
    def get_game(*, id: int) -> dict:
        logger.info('Getting game')
        return {}

    @staticmethod
    def update_game(*, id: int, new_name: str) -> dict:
        logger.info('Updating game')
        return {}

    @staticmethod
    def delete_game(*, id: int) -> dict:
        logger.info('Deleting game')
        return {}


class PlaygroundService:
    @staticmethod
    def create_game(*, name: str) -> dict:
        logger.info('Creating new game')
        return CardgameInterface.create_game(name=name)

    @staticmethod
    def get_game(*, id: int) -> dict:
        logger.info('Getting game')
        return CardgameInterface.get_game(id=id)

    @staticmethod
    def update_game(*, id: int, new_name: str) -> dict:
        logger.info('Updating game')
        return CardgameInterface.update_game(id=id, new_name=new_name)

    @staticmethod
    def delete_game(*, id: int) -> dict:
        logger.info('Deleting game')
        return CardgameInterface.delete_game(id=id)
