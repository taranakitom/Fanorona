import pygame
from .piece import Piece
from .constants import BLACK, WHITE, SCREEN_WIDTH, BOARD_WIDTH

class Board:
    def __init__(self):
        self.board = []
        self.white_left = self.black_left = 22
        self.create_board()
    
    def draw_board(self, screen):
        screen.blit(pygame.image.load("assets/board.png"), ((SCREEN_WIDTH - BOARD_WIDTH) / 2, 90))
        for row in range(5):
            for col in range(9):
                pygame.draw.circle(screen, BLACK, (82 * col + 314, 82 * row + 170), 10)
    
    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)
    
    def get_piece(self, row, col):
        return self.board[row][col]

    def create_board(self):
        for row in range(5):
            self.board.append([])
            for col in range(9):
                if row < 2:
                    self.board[row].append(Piece(row, col, BLACK))
                elif row > 2:
                    self.board[row].append(Piece(row, col, WHITE))
                else:
                    if col == 0 or col == 2 or col == 5 or col == 7:
                        self.board[row].append(Piece(row, col, BLACK))
                    elif col == 4:
                        self.board[row].append(0)
                    else:
                        self.board[row].append(Piece(row, col, WHITE))
                
    def draw(self, screen):
        self.draw_board(screen)
        for row in range(5):
            for col in range(9):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(screen)

    def remove(self, pieces):
        for piece in pieces:
            if piece.colour == WHITE:
                self.white_left -= 1
            else:
                self.black_left -= 1
            self.board[piece.row][piece.col] = 0
            
    def winner(self):
        if self.white_left <= 0:
            return "Black"
        elif self.black_left <= 0:
            return "White"
        
        return None

    def get_valid_moves(self, piece, turn, previous_piece, previous_move):
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        up = piece.row - 1
        down = piece.row + 1

        upleft = (up, left)
        upright = (up, right)
        downleft = (down, left)
        downright = (down, right)

        if previous_piece != None and self.get_piece(previous_piece[0], previous_piece[1]) != piece:
            return moves

        if self.get_piece(piece.row, left) == 0 and left >= 0:
            taken = []
            for other_piece in self.board[piece.row]:
                if other_piece == 0:
                    continue
                passed = other_piece.col > piece.col # if other_piece is past piece
                if passed: 
                    if other_piece.colour != turn: # if other_piece is an opp
                        taken.append(other_piece) # add to taken
                    else: # it's your piece
                        break # exit the for loop
                else: 
                    if other_piece.colour != turn: # if other_piece is an opp
                        taken.append(other_piece) # add to taken
                    else: # it's your piece
                        if other_piece.col == piece.col:
                            continue
                        else:
                            taken = [] # clear the taken pieces
            
            moves.update({(piece.row, left): taken})

        if self.get_piece(piece.row, right) == 0 and right <= 8:
            taken = []
            for other_piece in self.board[piece.row]:
                if other_piece == 0:
                    continue
                passed = other_piece.col > piece.col # if other_piece is past piece
                if passed: 
                    if other_piece.colour != turn: # if other_piece is an opp
                        taken.append(other_piece) # add to taken
                    else: # it's your piece
                        break # exit the for loop
                else: 
                    if other_piece.colour != turn: # if other_piece is an opp
                        taken.append(other_piece) # add to taken
                    else: # it's your piece
                        if other_piece.col == piece.col:
                            continue
                        else:
                            taken = [] # clear the taken pieces
            
            moves.update({(piece.row, right): taken})

        if self.get_piece(up, piece.col) == 0 and up >= 0:
            taken = []
            for row in self.board:
                other_piece = row[piece.col]
                if other_piece == 0:
                    continue
                passed = other_piece.row > piece.row # if other_piece is past piece
                if passed: 
                    if other_piece.colour != turn: # if other_piece is an opp
                        taken.append(other_piece) # add to taken
                    else: # it's your piece
                        break # exit the for loop
                else:
                    if other_piece.colour != turn: # if other_piece is an opp
                        taken.append(other_piece) # add to taken
                    else: # it's your piece
                        if other_piece.row == piece.row:
                            continue
                        else:
                            taken = [] # clear the taken pieces
            
            moves.update({(up, piece.col): taken})

        if self.get_piece(down, piece.col) == 0 and down <= 4:
            taken = []
            for row in self.board:
                other_piece = row[piece.col]
                if other_piece == 0:
                    continue
                passed = other_piece.row > piece.row # if other_piece is past piece
                if passed: 
                    if other_piece.colour != turn: # if other_piece is an opp
                        taken.append(other_piece) # add to taken
                    else: # it's your piece
                        break # exit the for loop
                else: 
                    if other_piece.colour != turn: # if other_piece is an opp
                        taken.append(other_piece) # add to taken
                    else: # it's your piece
                        if other_piece.row == piece.row:
                            continue
                        else:
                            taken = [] # clear the taken pieces
            
            moves.update({(down, piece.col): taken})
        
        if previous_move != None:
            if previous_move[0] == 0:
                pos = 1
            else:
                pos = 0

            if previous_move[pos] == left and (piece.row, left) in moves:
                moves.pop((piece.row, left))
            elif previous_move[pos] == right and (piece.row, right) in moves:
                moves.pop((piece.row, right))
            elif previous_move[pos] == up and (up, piece.col) in moves:
                moves.pop((up, piece.col))
            elif previous_move[pos] == down and (down, piece.col) in moves:
                moves.pop((down, piece.col))

        return moves
