import random

from tic_tac_toe.player import Player, UserPlayer, ComputerPlayer
from tic_tac_toe.templates import GREETING_MESSAGE, FIELD_TEMPLATE


class Game:
    def __init__(self) -> None:
        self.player_1: Player = UserPlayer(name='user')
        self.player_2: Player = ComputerPlayer(name='computer')
        self.field = {
            '0_0': '-',
            '0_1': '-',
            '0_2': '-',
            '1_0': '-',
            '1_1': '-',
            '1_2': '-',
            '2_0': '-',
            '2_1': '-',
            '2_2': '-',
        }

    def start(self) -> None:
        self.set_icons()
        print(GREETING_MESSAGE.format(icon=self.player_1.icon))

        while True:
            for player in {self.player_1, self.player_2}:
                move = player.make_a_move(self.field)
                if move == 'end':
                    self.end()

                x, y = move.split(',')
                player.increase_counter((x, y))
                self.field[f'{x}_{y}'] = player.icon
                self.show_field()

                if player.is_winner():
                    print('The game is over. Bye!')
                    self.end()

    def end(self) -> None:
        exit()

    def set_icons(self) -> None:
        player_1_icon = random.choice(('X', '0'))
        player_2_icon = 'X' if player_1_icon == '0' else '0'

        self.player_1.set_icon(player_1_icon)
        self.player_2.set_icon(player_2_icon)

    def show_field(self) -> None:
        print(FIELD_TEMPLATE.format(**self.field))
