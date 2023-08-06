import random


class AI:
    def __init__(self, board) -> None:
        self.board = board

    def get_random_move(self, moves):
        return random.choice(moves)