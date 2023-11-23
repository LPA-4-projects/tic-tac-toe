import random
from abc import ABC, abstractmethod

from tic_tac_toe.counter import Counter

class Player(ABC):
    def __init__(self, name: str):
        self.name: str = name
        self.icon: str = ''
        self.counter = Counter()

    @abstractmethod
    def make_a_move(self, empty_cells: list[str]) -> str:
        return NotImplemented

    def increase_counter(self, move: tuple[int, int]) -> None:
        self.counter.increase(move)

    def is_winner(self) -> bool:
        return self.counter.has_full_row()

    def set_icon(self, icon: str) -> None:
        self.icon = icon

    def set_name(self, name: str) -> None:
        self.name = name


class ComputerPlayer(Player):

    def make_a_move(self, empty_cells: list[str]) -> str:
        return random.choice(empty_cells)


class UserPlayer(Player):

    def make_a_move(self, empty_cells: list[str]) -> str:
        move = self._move('Make your move')

        while not self._is_correct(move, empty_cells):
            move = self._move('Wrong input. Please try again')

        return move

    def _move(self, message: str) -> str:
        move = input(f'{message}: ').strip().lower()
        return move.replace(' ', '_')

    def _is_correct(self, move: str, empty_cells: list[str]) -> bool:
        if move == 'end':
            return True

        if move in empty_cells:
            return True

        return False
