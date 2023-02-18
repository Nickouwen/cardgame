import logging

from django.db import transaction

from .models import Game, Table

logger = logging.getLogger(__name__)


class GameService:
    @staticmethod
    def create_game(*, name: str) -> dict:
        logger.info('Creating new game')
        with transaction.atomic():
            game = Game()
            game.name = name
            game.save()

            table = Table()
            table.game = game
            table.save()

        return {
            'name': name,
        }

    @staticmethod
    def get_game(*, id: int) -> dict:
        logger.info('Getting game')
        game = Game.objects.get(pk=id)
        return {
            'name': game.name
        }

    @staticmethod
    def update_game(*, id: int, new_name: str) -> dict:
        logger.info('Updating game')
        game = Game.objects.filter(pk=id)
        old_name = game.name
        game.update(name=new_name)

        return {
            'old_name': old_name,
            'name': game.name
        }

    @staticmethod
    def delete_game(*, id: int) -> dict:
        logger.info('Deleting game')
        game = Game.objects.filter(pk=id)
        game.delete()

        return {
            'id': id
        }
