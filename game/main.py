import random

greeting_message = """
Hey!
This is a 3x3 tic-tac-toe

You play with {icon} and you start
Write down a cell number
If you'd like to finish the game, type 'end'
"""

field_template = """
 {a} | {b} | {c}
___ ___ ___
 {d} | {e} | {f}
___ ___ ___
 {g} | {h} | {i}
"""

def computer_move(cells: dict[str, str]) -> str:
    choice = 'a'
    while cells[choice] != '-':
        choice = random.choice(list(cells.keys()))

    return choice


def start():

    cells = {
        'a': '-',
        'b': '-',
        'c': '-',
        'd': '-',
        'e': '-',
        'f': '-',
        'g': '-',
        'h': '-',
        'i': '-',
    }
    user_icon = random.choice(('X', '0'))
    computer_icon = 'X' if user_icon == '0' else '0'

    print(greeting_message.format(icon=user_icon))

    while True:

        prompt = input('Your turn: ').strip()
        if prompt.lower() == 'end':
            exit()

        cells[prompt] = user_icon
        print(field_template.format(**cells))

        computer_choice = computer_move(cells)
        cells[computer_choice] = computer_icon
        print(field_template.format(**cells))


if __name__ == '__main__':
    start()
