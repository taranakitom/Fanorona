import pygame

class Board:
    def __init__(self):
        self.board = []
        self.selected_piece = None
        self.white_left = self.black_left = 22
    
    def draw_board(self, screen):
        screen.blit(pygame.image.load("assets/board.png"), ((1280 - 821) / 2, 90))
        for row in range(5):
            for col in range(9):
                pygame.draw.rect(screen, (0, 0, 0), (82 * col + 307, 82 * row + 165, 10, 10))
