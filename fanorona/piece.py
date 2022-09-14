import pygame

class Piece:
    PADDING = 15
    OUTLINE = 2

    def __init__(self, row, col, colour):
        self.row = row
        self.col = col
        self.colour = colour

        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = 82 * self.col + 312
        self.y = 82 * self.row + 170

    def draw(self, screen):
        radius = 82 // 2 - self.PADDING
        pygame.draw.circle(screen, (128, 128, 128), (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(screen, self.colour, (self.x, self.y), radius)

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()
    
    def __repr__(self):
        return str(self.colour)
