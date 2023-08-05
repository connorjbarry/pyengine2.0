import pygame

from game_const import *
from board import Board
from drag_client import Drag

class Game:
    def __init__(self) -> None:
        self.board = Board()
        self.drag_client = Drag()

    def show_bg(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                if (row + col) % 2 == 0:
                    color = pygame.Color("gray")
                else: 
                    color = pygame.Color("white")
        
                rect = (col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                pygame.draw.rect(surface, color, rect)

    def show_pieces(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                if self.board.squares[row][col].has_piece():
                    piece = self.board.squares[row][col].piece

                    if piece is not self.drag_client.piece:
                        piece.set_texture(size=80)
                        img = pygame.image.load(piece.texture)
                        img_center = col * TILE_SIZE + TILE_SIZE // 2, row * TILE_SIZE + TILE_SIZE // 2
                        piece.texture_rect = img.get_rect(center=img_center)

                        surface.blit(img, piece.texture_rect)

    def highlight_moves(self, screen, moves, selectedSquare):
        if selectedSquare == (): return
        r, c = selectedSquare
        if self.board.squares[r][c].has_piece() and self.board.squares[r][c].piece.color_name == self.board.turn:
            s = pygame.Surface((TILE_SIZE, TILE_SIZE))
            s.set_alpha(100)
            s.fill(pygame.Color("blue"))
            screen.blit(s, (c * TILE_SIZE, r * TILE_SIZE))

            s.set_alpha(75)
            s.fill(pygame.Color('red'))
            for move in moves:
                if move.initial.row == r and move.initial.col == c:
                    screen.blit(s, (move.final.col * TILE_SIZE, move.final.row * TILE_SIZE))
            