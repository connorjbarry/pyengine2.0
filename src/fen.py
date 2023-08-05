
from piece import *

class Fen:
    def __init__(self) -> None:
        self.starting_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
        self.piece_from_symbol = {
            "p": Pawn,
            "n": Knight,
            "b": Bishop,
            "r": Rook,
            "q": Queen,
            "k": King
        }

    def build_board_from_fen(self, fen=None):
        if fen is None:
            fen = self.starting_fen

        fen_parts = fen.split(" ")
        if len(fen_parts) != 6:
            raise ValueError("Invalid FEN string")
        
        board_layout = fen_parts[0]
        board_rows = board_layout.split("/")
        if len(board_rows) != 8:
            raise ValueError("Invalid FEN string")

        board = []
        for row in board_rows:
            board_row = []
            for char in row:
                if char.isdigit():
                    for _ in range(int(char)):
                        board_row.append(0)
                else:
                    board_row.append(self.get_piece_id_from_char(char))
            board.append(board_row)

        return board
    
    def get_piece_id_from_char(self, char):
        piece_color = "white" if char.isupper() else "black"
        char = char.lower()

        color = self.piece_from_symbol[char](piece_color).color
        id = self.piece_from_symbol[char](piece_color).id

        if id == 0:
            return id

        return color | id