import os

class Piece:
    def __init__(self, id, name, color, value, texture=None, texture_rect=None):
        self.id = id
        self.name = name
        self.color = None if color == None else 8 if color == "white" else 16
        self.color_name = color
        self.typeMask = 0b111
        self.whiteMask = 0b01000
        self.blackMask = 0b10000
        self.colorMask = self.whiteMask | self.blackMask
        self.board_rep = self.color | self.id if self.color != None else 0

        value_sign = 1 if color == "white" else -1
        self.value = value * value_sign

        self.moves = []
        self.moved = False

        self.texture = texture
        self.set_texture()
        self.texture_rect = texture_rect
    
    def __repr__(self) -> str:
        return f'{self.color | self.id}'
    
    def __eq__(self, other) -> bool:
        if type(self) == int or type(other) == int:
            return False
        return self.id == other.id and self.color == other.color

    def set_texture(self, size=80):
        color = "white" if self.color == 8 else "black"
        if self.name == "null":
            self.texture = None
        self.texture = os.path.join(
            f'assets/images/imgs-{size}px/{color}_{self.name}.png'
        )

    def add_moves(self, move):
        self.moves.append(move)
    

class NullPiece(Piece):
    def __init__(self):
        super().__init__(0, "null", None, 0.0)

class Pawn(Piece):
    def __init__(self, color):
        self.dir = -1 if color == "white" else 1
        super().__init__(2, "pawn", color, 1.0)

class Knight(Piece):
    def __init__(self, color):
        super().__init__(3, "knight", color, 3.0)

class Bishop(Piece):
    def __init__(self, color):
        super().__init__(5, "bishop", color, 3.001)

class Rook(Piece):
    def __init__(self, color):
        super().__init__(6, "rook", color, 5.0)

class Queen(Piece):
    def __init__(self, color):
        super().__init__(7, "queen", color, 9.0)

class King(Piece):
    def __init__(self, color):
        super().__init__(1, "king", color, 10000.0)