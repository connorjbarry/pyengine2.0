from piece import *

class Square:
    def __init__(self, row, col, piece_id=None) -> None:
        self.row = row
        self.col = col
        self.piece = self._get_piece_from_binary(piece_id)
        
    def __repr__(self) -> str:
        return f'{self.piece}'
    
    def __eq__(self, other) -> bool:
        return self.row == other.row and self.col == other.col

    def has_piece(self):
        if type(self.piece) == int:
            return False
        return self.piece != NullPiece().id
    
    def _get_piece_from_binary(self, piece_id):
        if piece_id == NullPiece().id:
            return 0

        piece_map = {
            None: None,
            8 | 2: Pawn("white"),
            8 | 3: Knight("white"),
            8 | 5: Bishop("white"),
            8 | 6: Rook("white"),
            8 | 7: Queen("white"),
            8 | 1: King("white"),
            16 | 2: Pawn("black"),
            16 | 3: Knight("black"),
            16 | 5: Bishop("black"),
            16 | 6: Rook("black"),
            16 | 7: Queen("black"),
            16 | 1: King("black")
        }

        return piece_map[piece_id]

    