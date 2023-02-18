import logging

from .interfaces import IGameService
from .services import GameService

logger = logging.getLogger(__name__)


class CardgameAPI:
    def __init__(self, igame_service: IGameService = GameService()) -> None:
        self.__game_service = igame_service

    def create(self, *, game_name: str) -> dict:
        logger.info('method "create" called')
        return self.__game_service.create_game(name=game_name)

    def get(self, *, game_id: int) -> dict:
        logger.info('method "get" called')
        return self.__game_service.get_game(id=game_id)

    def update(self, *, game_id: int, game_name: str) -> dict:
        logger.info('method "update" called')
        return self.__game_service.update_game(id=game_id, new_name=game_name)

    def delete(self, *, game_id: int) -> dict:
        logger.info('method "id" called')
        return self.__game_service.delete_game(id=game_id)
