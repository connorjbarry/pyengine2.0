from game_const import *
from square import Square
from piece import NullPiece
from fen import *
from movegen import MoveGen

class Board: 
    def __init__(self) -> None:
        self.squares = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        self.last_move = None
        self._create_board()
        self._place_pieces()
        self.turn = "white"
        self.mg = MoveGen()
        self.movelog = []

    def move(self, move):
        initial = move.initial
        final = move.final

        piece = self.squares[initial.row][initial.col].piece

        move.captured_piece = self.squares[final.row][final.col].piece
        self.squares[final.row][final.col].piece = piece
        self.squares[initial.row][initial.col].piece = NullPiece().id

        self.movelog.append(move)

        piece.moved = True

        self.last_move = move

        self.turn = "black" if self.turn == "white" else "white"

    def undo_move(self):
        if len(self.movelog) == 0:
            return
        
        move = self.movelog.pop()
        piece = self.squares[move.final.row][move.final.col].piece
        self.squares[move.initial.row][move.initial.col].piece = piece
        self.squares[move.final.row][move.final.col].piece = move.captured_piece

        piece.moved = False

        self.last_move = None

        self.turn = "black" if self.turn == "white" else "white"


    def _create_board(self):
        for row in range(ROWS):
            for col in range(COLS):
                self.squares[row][col] = Square(row, col, NullPiece().id)

    def _place_pieces(self):
        fen = Fen()
        board = fen.build_board_from_fen()

        for row in range(ROWS):
            for col in range(COLS):
                self.squares[row][col] = Square(row, col, board[row][col])
    
    def get_piece_color(self, row, col):
        if self.squares[row][col].has_piece():
            return self.squares[row][col].piece.color
        else: return None