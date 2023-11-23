class Field:
    def __init__(self) -> None:
        self.cells = {
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

    def get_empty_cells(self) -> list[str]:
        return list(filter(lambda x: self.cells[x] == '-', self.cells.keys()))
