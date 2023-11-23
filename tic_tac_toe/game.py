import random

from tic_tac_toe.field import Field
from tic_tac_toe.player import Player, UserPlayer, ComputerPlayer
from tic_tac_toe.templates import GREETING_MESSAGE, FIELD_TEMPLATE, RULES_MESSAGE


class Game:
    def __init__(self) -> None:
        self.player_1: Player = UserPlayer(name='User')
        self.player_2: Player = ComputerPlayer(name='Computer')
        self.field = Field()

    def start(self) -> None:
        username: str = input(GREETING_MESSAGE).strip()
        self.player_1.set_name(username)

        self.set_icons()
        order: list[Player] = self.choose_order()
        print(RULES_MESSAGE.format(icon=self.player_1.icon, player=order[0].name))
        self.show_field()
        input('Press "Enter" to start the game')

        while True:
            for player in order:
                empty_cells = self.field.get_empty_cells()
                move = player.make_a_move(empty_cells)
                if move == 'end':
                    self.end()

                x, y = move.split('_')
                player.increase_counter((int(x), int(y)))
                self.field.cells[move] = player.icon
                self.show_field()

                if player.is_winner():
                    print(f'{player.name} win. Bye!')
                    self.end()

    def end(self) -> None:
        exit()

    def set_icons(self) -> None:
        player_1_icon = random.choice(('X', '0'))
        player_2_icon = 'X' if player_1_icon == '0' else '0'

        self.player_1.set_icon(player_1_icon)
        self.player_2.set_icon(player_2_icon)

    def show_field(self) -> None:
        print(FIELD_TEMPLATE.format(**self.field.cells))

    def choose_order(self) -> list[Player]:
        players = [self.player_1, self.player_2]
        random.shuffle(players)
        return players
