import logging

from .services import GameService

logger = logging.getLogger('__name__')


class CardgameAPI:

    @staticmethod
    def create(*, game_name: str) -> dict:
        logger.info('method "create" called')
        return GameService.create_game(name=game_name)

    @staticmethod
    def get(*, game_id: int) -> dict:
        logger.info('method "get" called')
        return GameService.get_game(id=game_id)

    @staticmethod
    def update(*, game_id: int, game_name: str) -> dict:
        logger.info('method "update" called')
        return GameService.update_game(new_name=game_name)

    @staticmethod
    def delete(*, game_id: int) -> dict:
        logger.info('method "id" called')
        return GameService.delete_game(id=game_id)
