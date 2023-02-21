import logging

from cardgame.interfaces import IGameService

from ..interfaces import CardgameInterface
from ..models import *

logger = logging.getLogger(__name__)


class PlaygroundService(IGameService):
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
