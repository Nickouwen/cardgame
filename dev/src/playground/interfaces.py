"""
interfaces.py
"""
from cardgame.apis import CardgameAPI


class CardgameInterface:

    @staticmethod
    def create_game(*, name: str) -> dict:
        return CardgameAPI().create(game_name=name)

    @staticmethod
    def get_game(*, id: int) -> dict:
        return CardgameAPI().get(game_id=id)

    @staticmethod
    def update_game(*, id: int, new_name: str) -> dict:
        return CardgameAPI().update(game_id=id, game_name=new_name)

    @staticmethod
    def delete_game(*, id: int) -> dict:
        return CardgameAPI().delete(game_id=id)
