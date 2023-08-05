from move import Move
from square import Square
from piece import *
from game_const import *

class MoveGen:
    def __init__(self) -> None:
        pass

    def _is_valid_square(self, row, col):
        if row < 0 or row >= 8 or col < 0 or col >= 8:
            return False
        return True
    
    def _is_valid_square_with_black_piece(self, row, col, board):
        if not self._is_valid_square(row, col):
            return False

        if board.squares[row][col].has_piece() and board.squares[row][col].piece.color_name == "black":
            return True

        return False
    
    def _is_valid_square_with_white_piece(self, row, col, board):
        if not self._is_valid_square(row, col):
            return False

        if board.squares[row][col].has_piece() and board.squares[row][col].piece.color_name == "white":
            return True

        return False

    def generate_moves(self, board):
        moves = []
        for row in range(ROWS):
            for col in range(COLS):
                piece = board.squares[row][col].piece
            
                if isinstance(piece, Piece) and (piece == Pawn("white") or piece == Pawn("black")):
                    moves.extend(self.generate_pawn_moves(row, col, board))

                elif isinstance(piece, Piece) and (piece == Rook("white") or piece == Rook("black")):
                    moves.extend(self.generate_sliding_moves(row, col, board, SLIDING_DIRS[0:4]))

                elif isinstance(piece, Piece) and (piece == Bishop("white") or piece == Bishop("black")):
                    moves.extend(self.generate_sliding_moves(row, col, board, SLIDING_DIRS[4:8]))
                
                elif isinstance(piece, Piece) and (piece == Queen("white") or piece == Queen("black")):
                    moves.extend(self.generate_sliding_moves(row, col, board, SLIDING_DIRS[0:8]))

                elif isinstance(piece, Piece) and (piece == Knight("white") or piece == Knight("black")):
                    moves.extend(self.generate_knight_moves(row, col, board))

                # elif isinstance(piece, Piece) and (piece == King("white") or piece == King("black")):
                #     moves.extend(self.generate_king_moves(row, col, board))

        return moves
                

    def generate_pawn_moves(self, row, col, board):
        moves = []
        if board.turn == "white":
            # white pawn goes up board -> row - move
            if not board.squares[row - 1][col].has_piece():
                moves.append(Move(Square(row, col), Square(row - 1, col)))
                if row == 6 and not board.squares[row - 2][col].has_piece():
                    moves.append(Move(Square(row, col), Square(row - 2, col)))
            
            if self._is_valid_square_with_black_piece(row - 1, col - 1, board):
                moves.append(Move(Square(row, col), Square(row - 1, col - 1)))

            if self._is_valid_square_with_black_piece(row - 1, col + 1, board):
                moves.append(Move(Square(row, col), Square(row - 1, col + 1)))

        else:
            # black pawn goes down board -> row + move
            if not board.squares[row + 1][col].has_piece():
                moves.append(Move(Square(row, col), Square(row + 1, col)))
                if row == 1 and not board.squares[row + 2][col].has_piece():
                    moves.append(Move(Square(row, col), Square(row + 2, col)))

            if self._is_valid_square_with_white_piece(row + 1, col - 1, board):
                moves.append(Move(Square(row, col), Square(row + 1, col - 1)))

            if self._is_valid_square_with_white_piece(row + 1, col + 1, board):
                moves.append(Move(Square(row, col), Square(row + 1, col + 1)))

        return moves
    
    def generate_sliding_moves(self, row, col, board, dirs):
        moves = []
        for dir in dirs:
            for length in range(1,8):
                end_row = row + dir[0] * length
                end_col = col + dir[1] * length

                if not self._is_valid_square(end_row, end_col):
                    break

                end_piece = board.squares[end_row][end_col].piece

                if end_piece == NullPiece().id:
                    moves.append(Move(Square(row, col), Square(end_row, end_col)))
                
                elif end_piece.color_name != board.turn:
                    moves.append(Move(Square(row, col), Square(end_row, end_col)))
                    break
                
                else: break
        return moves
    
    def generate_knight_moves(self, row, col, board):
        moves = []

        for dir in KNIGHT_DIRS:
            end_row = row + dir[0]
            end_col = col + dir[1]

            if not self._is_valid_square(end_row, end_col):
                continue

            end_piece = board.squares[end_row][end_col].piece

            if end_piece == NullPiece().id:
                moves.append(Move(Square(row, col), Square(end_row, end_col)))
            
            if board.squares[end_row][end_col].has_piece() and end_piece.color_name != board.turn:
                moves.append(Move(Square(row, col), Square(end_row, end_col)))

        return moves
    
    def generate_king_moves(self, row, col, board):
        pass