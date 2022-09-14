import pygame
from .board import Board

class Game:
    def __init__(self, screen):
        self._init()
        self.screen = screen
    
    def update(self):
        self.board.draw(self.screen)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = (255, 255, 255)
        self.valid_moves = {}
    
    def reset(self):
        self._init()
    
    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)
        
        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.colour == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece, self.turn)
            return True
        
        return False

    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            taken = self.valid_moves[(row, col)]
            if taken:
                self.board.remove(taken)
            self.change_turn(row, col)
        else:
            return False

        return True

    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.screen, (0, 0, 255), (82 * col + 314, 82 * row + 170), 10)
        

    def change_turn(self, row, col):
        if len(self.valid_moves[(row, col)]) == 0:
            if self.turn == (255, 255, 255):
                self.turn = (0, 0, 0)
            else:
                self.turn = (255, 255, 255)
        self.valid_moves = {}
        