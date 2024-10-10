class Cell:
    def __init__(self, state: str) -> None:
        self.state = state

    def status(self) -> str:
        return self.state


class Checkers:
    def __init__(self) -> None:
        self.board = {}
        row_pieces_even = {
            "1": "W",
            "2": "X",
            "3": "W",
            "4": "X",
            "5": "X",
            "6": "X",
            "7": "B",
            "8": "X",
        }
        row_pieces_odd = {
            "1": "X",
            "2": "W",
            "3": "X",
            "4": "X",
            "5": "X",
            "6": "B",
            "7": "X",
            "8": "B",
        }

        for row in "87654321":
            for index, col in enumerate("ABCDEFGH"):
                if index % 2 == 0:
                    state = row_pieces_even[row]
                else:
                    state = row_pieces_odd[row]

                position = col + row
                self.board[position] = Cell(state)

    def move(self, current: str, move_to: str) -> None:
        checker = self.board[current]
        self.board[move_to] = checker
        self.board[current] = Cell("X")

    def get_cell(self, position: str) -> Cell:
        return self.board[position]
