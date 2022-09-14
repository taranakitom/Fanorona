import pygame
from .piece import Piece

class Board:
    def __init__(self):
        self.board = []
        self.selected_piece = None
        self.white_left = self.black_left = 22
        self.create_board()
    
    def draw_board(self, screen):
        screen.blit(pygame.image.load("assets/board.png"), ((1280 - 821) / 2, 90))
        for row in range(5):
            for col in range(9):
                pygame.draw.rect(screen, (0, 0, 0), (82 * col + 307, 82 * row + 165, 10, 10))
    
    def create_board(self):
        for row in range(5):
            self.board.append([])
            for col in range(9):
                if row < 2:
                    self.board[row].append(Piece(row, col, (0, 0, 0)))
                elif row > 2:
                    self.board[row].append(Piece(row, col, (255, 255, 255)))
                else:
                    if col == 0 or col == 2 or col == 5 or col == 7:
                        self.board[row].append(Piece(row, col, (0, 0, 0)))
                    elif col == 4:
                        self.board[row].append(0)
                    else:
                        self.board[row].append(Piece(row, col, (255, 255, 255)))
                
    def draw(self, screen):
        self.draw_board(screen)
        for row in range(5):
            for col in range(9):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(screen)