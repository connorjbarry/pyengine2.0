import pygame
import sys
import logging
import coloredlogs

from game_const import *
from game import Game
from square import Square
from move import Move


coloredlogs.install(fmt='%(asctime)s | %(levelname)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S', level='DEBUG')
logging.disable(logging.CRITICAL)


class Main:

    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.selected_square = ()
        self.player_clicks = []
        pygame.display.set_caption("Chess")
        self.game = Game()

    def loop(self):
        game = self.game
        screen = self.screen
        board = self.game.board
        drag_client = self.game.drag_client


        logging.info("Generating Initial State Moves...")
        moves = board.mg.generate_moves(board)
        
        logging.info("Starting Game Loop...")
        logging.info(f"{board.turn}'s turn")


        while True:
            game.show_bg(screen)
            game.highlight_moves(screen, moves, self.selected_square)
            game.show_pieces(screen)

            if drag_client.is_dragging:
                drag_client.update_blit(screen)

            for event in pygame.event.get():

                if event.type == pygame.MOUSEBUTTONDOWN:
                    drag_client.update(event.pos)

                    clicked_row = drag_client.mouseY // TILE_SIZE
                    clicked_col = drag_client.mouseX // TILE_SIZE

                    if self.selected_square == (clicked_row, clicked_col):
                        self.selected_square = ()
                        self.player_clicks = []
                    else:
                        self.selected_square = (clicked_row, clicked_col)
                        self.player_clicks.append(self.selected_square)

                    if len(self.player_clicks) == 1 and not board.squares[clicked_row][clicked_col].has_piece():
                        self.selected_square = ()
                        self.player_clicks = []

                    if len(self.player_clicks) > 1:
                        first_piece_color = board.get_piece_color(self.player_clicks[0][0], self.player_clicks[0][1])
                        second_piece_color = board.get_piece_color(self.player_clicks[1][0], self.player_clicks[1][1])

                        if first_piece_color == second_piece_color:
                            self.selected_square = self.player_clicks[1]
                            self.player_clicks = [self.selected_square]

                    if board.squares[clicked_row][clicked_col].has_piece():
                        piece = board.squares[clicked_row][clicked_col].piece
                        drag_client.save_initial_click(event.pos)
                        drag_client.drag_piece(piece)
                        temp_piece = piece
                    
                    if len(self.player_clicks) == 2 and not drag_client.is_dragging:
                        initial = Square(self.player_clicks[0][0], self.player_clicks[0][1])
                        final = Square(self.player_clicks[1][0], self.player_clicks[1][1])

                        move = Move(initial, final)

                        if initial != final and temp_piece.color_name == board.turn:
                            if move in moves:
                                board.move(move)
                                logging.warning(f'Move made -- {move}')
                                self.selected_square = ()
                                self.player_clicks = []
                                temp_piece = None
                                logging.info("Re-generating moves...")
                                moves = board.mg.generate_moves(board)
                
                elif event.type == pygame.MOUSEMOTION:
                    if drag_client.is_dragging:
                        drag_client.update(event.pos)
                        game.show_bg(screen)
                        game.highlight_moves(screen, moves, self.selected_square)
                        game.show_pieces(screen)
                        drag_client.update_blit(screen)

                elif event.type == pygame.MOUSEBUTTONUP:
                    
                    if drag_client.is_dragging:
                        drag_client.update(event.pos)

                        released_row = drag_client.mouseY // TILE_SIZE
                        released_col = drag_client.mouseX // TILE_SIZE

                        initial = Square(drag_client.initial_row, drag_client.initial_col)
                        final = Square(released_row, released_col)

                        move = Move(initial, final)

                        if initial != final and drag_client.piece.color_name == board.turn:
                            if move in moves:
                                board.move(move)
                                logging.warning(f'Move made -- {move}')
                                game.show_bg(screen)
                                game.highlight_moves(screen, moves, self.selected_square)
                                game.show_pieces(screen)
                                self.selected_square = ()
                                self.player_clicks = []
                                logging.info("Re-generating moves...")
                                moves = board.mg.generate_moves(board)
                    
                    drag_client.undrag_piece()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_u:
                        board.undo_move()
                        logging.warning(f'Undoing move -- {move}')
                        self.selected_square = ()
                        self.player_clicks = []
                        logging.info("Re-generating moves...")
                        moves = board.mg.generate_moves(board)

                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.flip()

main = Main()
main.loop()