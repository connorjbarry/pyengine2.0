
class Move:

    def __init__(self, initial, final, board=None) -> None:
        self.initial = initial
        self.final = final
        self.captured_piece = board[final.row][final.col].piece if board else None

    def __repr__(self) -> str:
        return f'{self.initial.col}, {self.initial.row} -> {self.final.col}, {self.final.row}'

    def __str__(self) -> str:
        return f'{self.initial.col}, {self.initial.row} -> {self.final.col}, {self.final.row}'
    
    def __eq__(self, other) -> bool:
        return self.initial == other.initial and self.final == other.final