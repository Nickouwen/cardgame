from datetime import datetime

from .table_model import Table


class Game:
    STATUS_NEW = 'N'
    STATUS_INPROGRESS = 'I'
    STATUS_OVER = 'O'
    STATUS_CHOICES = [
        (STATUS_NEW, 'New Game'),
        (STATUS_INPROGRESS, 'In Progress'),
        (STATUS_OVER, 'Game Over'),
    ]

    def __init__(self, id: int, name: str) -> None:
        self.id = id
        self.name = name
        self.round_number = 0
        self.started_at = datetime.now()
        self.status = Game.STATUS_NEW
        self.table = Table()

    def __str__(self) -> str:
        return f"{self.name} - {[choice[1] for choice in Game.STATUS_CHOICES if choice[0] is self.status]}"
