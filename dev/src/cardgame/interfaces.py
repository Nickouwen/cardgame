from abc import ABC, abstractmethod


class IGameService(ABC):
    @staticmethod
    @abstractmethod
    def create_game(*, name: str) -> dict:
        pass

    @staticmethod
    @abstractmethod
    def get_game(*, id: int) -> dict:
        pass

    @staticmethod
    @abstractmethod
    def update_game(*, id: int, new_name: str) -> dict:
        pass

    @staticmethod
    @abstractmethod
    def delete_game(*, id: int) -> dict:
        pass
