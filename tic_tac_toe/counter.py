class Counter:
    def __init__(self) -> None:
        self.win_combinations = {
            'r0': 0,
            'r1': 0,
            'r2': 0,
            'c0': 0,
            'c1': 0,
            'c2': 0,
            'd1': 0,
            'd2': 0,
        }
        self.combinations_map = {
            'r0': {(0, 0), (0, 1), (0, 2)},
            'r1': {(1, 0), (1, 1), (1, 2)},
            'r2': {(2, 0), (2, 1), (2, 2)},
            'c0': {(0, 0), (1, 0), (2, 0)},
            'c1': {(0, 1), (1, 1), (2, 1)},
            'c2': {(0, 2), (1, 2), (2, 2)},
            'd1': {(0, 0), (1, 1), (2, 2)},
            'd2': {(0, 2), (1, 1), (2, 0)},
        }

    def has_fool_row(self) -> bool:
        return True if 3 in self.win_combinations.values() else False

    def increase(self, move: tuple) -> None:
        for k, v in self.combinations_map.items():
            if move in v:
                self.win_combinations[k] += 1
