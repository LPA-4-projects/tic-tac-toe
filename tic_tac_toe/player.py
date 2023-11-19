import random
from abc import ABC, abstractmethod

from tic_tac_toe.counter import Counter

class Player(ABC):
    def __init__(self, name: str):
        self.name: str = name
        self.icon: str = ''
        self.counter = Counter()

    @abstractmethod
    def make_a_move(self, field: dict[str, str]) -> str:
        return NotImplemented

    def increase_counter(self, move: tuple) -> None:
        move = tuple(map(int, move))
        self.counter.increase(move)

    def is_winner(self) -> bool:
        return self.counter.has_fool_row()

    def set_icon(self, icon: str) -> None:
        self.icon = icon


class ComputerPlayer(Player):
    def make_a_move(self, field: dict[str, str]) -> str:
        choice = random.choice(list(field.keys()))
        while field[choice] != '-':
            choice = random.choice(list(field.keys()))

        return choice.replace('_', ',')


class UserPlayer(Player):
    def make_a_move(self, field: dict[str, str]) -> str:
        return input('Your turn: ').strip().lower()
