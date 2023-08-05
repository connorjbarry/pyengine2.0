WIDTH = 800
HEIGHT = 800

COLS = 8
ROWS = 8

TILE_SIZE = WIDTH // COLS

SLIDING_DIRS = [
    (-1, 0), # up
    (0, 1), # right
    (1, 0), # down
    (0, -1), # left
    (-1, 1), # up right
    (1, 1), # down right
    (1, -1), # down left
    (-1, -1), # up left
]

KNIGHT_DIRS = [
    (-2, -1), # up left
    (-2, 1), # up right
    (-1, 2), # right up
    (1, 2), # right down
    (2, 1), # down right
    (2, -1), # down left
    (1, -2), # left down
    (-1, -2), # left up
]