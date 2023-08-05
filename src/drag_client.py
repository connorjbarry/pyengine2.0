import pygame
from game_const import *

class Drag:
    
    def __init__(self) -> None:
        self.piece = None
        self.is_dragging = False
        self.mouseX = 0
        self.mouseY = 0
        self.initial_row = 0
        self.initial_col = 0

    def update_blit(self, surface):
        self.piece.set_texture(size=128)

        img = pygame.image.load(self.piece.texture)
        img_center = (self.mouseX, self.mouseY)
        self.piece.texture_rect = img.get_rect(center=img_center)

        surface.blit(img, self.piece.texture_rect)

    def update(self, pos):
        self.mouseX, self.mouseY = pos

    def save_initial_click(self, pos):
        self.initial_row = pos[1] // TILE_SIZE
        self.initial_col = pos[0] // TILE_SIZE

    def drag_piece(self, piece):
        self.piece = piece
        self.is_dragging = True

    def undrag_piece(self):
        self.piece = None
        self.is_dragging = False
