import pygame
from .constants import PIECE_PADDING, PIECE_OUTLINE, GREY, SPACE_BETWEEN_PIECES, SPACE_LEFT_OF_PIECES, SPACE_ABOVE_PIECES

class Piece:
    def __init__(self, row, col, colour):
        self.row = row
        self.col = col
        self.colour = colour

        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = SPACE_BETWEEN_PIECES * self.col + SPACE_LEFT_OF_PIECES
        self.y = SPACE_BETWEEN_PIECES * self.row + SPACE_ABOVE_PIECES

    def draw(self, screen):
        radius = SPACE_BETWEEN_PIECES // 2 - PIECE_PADDING
        pygame.draw.circle(screen, GREY, (self.x, self.y), radius + PIECE_OUTLINE)
        pygame.draw.circle(screen, self.colour, (self.x, self.y), radius)

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()
    
    def __repr__(self):
        return str(self.colour)
