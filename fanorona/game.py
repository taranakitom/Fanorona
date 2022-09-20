import pygame
from .board import Board
from .constants import BLACK, WHITE, BLUE, GREY_RED, BLACK_RED, WHITE_RED, COL_RECTS, ROW_RECTS, DOT_SIZE, SPACE_BETWEEN_PIECES, SPACE_LEFT_OF_PIECES, SPACE_ABOVE_PIECES, PIECE_PADDING, PIECE_OUTLINE

class Game:
    def __init__(self, screen):
        self._init()
        self.screen = screen
    
    def update(self):
        self.board.draw(self.screen)
        self.draw_valid_moves()
        self.draw_selected()
        pygame.display.update()

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = WHITE
        self.valid_moves = {}
        self.previous_piece = None
        self.previous_move = None
        self.places_been = []
    
    def reset(self):
        self._init()
    
    def select(self, row, col):
        # if selecting where to move it
        if self.selected:
            result = self._move(row, col)
            if not result: # if not moving to a 0
                self.selected = None
                self.select(row, col) # select that piece instead
        
        # if selecting a piece
        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.colour == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece, self.turn, self.previous_piece, self.previous_move, self.places_been)
            return True
        
        return False

    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if piece == 0 and (row, col) in self.valid_moves:
            self.previous_piece = (row, col)
            self.places_been.append((self.selected.row, self.selected.col))
            self.previous_move = (self.selected.row - row, self.selected.col - col)
            self.board.move(self.selected, row, col)
            self.selected = None
            taken = self.valid_moves[(row, col)]
            if taken:
                self.board.remove(taken)
            self.change_turn(row, col)
        else:
            return False

        return True

    def draw_valid_moves(self):
        for move in self.valid_moves:
            row, col = move
            pygame.draw.circle(self.screen, BLUE, (SPACE_LEFT_OF_PIECES + SPACE_BETWEEN_PIECES * col, SPACE_ABOVE_PIECES + SPACE_BETWEEN_PIECES * row), DOT_SIZE)
        
    def draw_selected(self):
        if self.selected != None:
            radius = SPACE_BETWEEN_PIECES // 2 - PIECE_PADDING
            pygame.draw.circle(self.screen, GREY_RED, (self.selected.x, self.selected.y), radius + PIECE_OUTLINE)
            if self.turn == WHITE:
                pygame.draw.circle(self.screen, WHITE_RED, (self.selected.x, self.selected.y), radius)
            else:
                pygame.draw.circle(self.screen, BLACK_RED, (self.selected.x, self.selected.y), radius)

    def change_turn(self, row, col):
        if len(self.valid_moves[(row, col)]) == 0:
            self.previous_piece = None
            self.previous_move = None
            self.places_been = []
            if self.turn == WHITE:
                self.turn = BLACK
            else:
                self.turn = WHITE
            self.valid_moves = {}
        else:
            self.valid_moves = {}
            moves = self.board.get_valid_moves(self.board.get_piece(row, col), self.turn, self.previous_piece, self.previous_move, self.places_been)
            for move in moves:
                if len(moves[move]) > 0:
                    return
            self.previous_piece = None
            self.previous_move = None
            self.places_been = []
            if self.turn == WHITE:
                self.turn = BLACK
            else:
                self.turn = WHITE
        