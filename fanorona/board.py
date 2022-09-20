import pygame
from .piece import Piece
from .constants import BLACK, WHITE, SPACE_EITHER_SIDE, SPACE_TOP_BOTTOM, DOT_SIZE, SPACE_BETWEEN_PIECES, COL_AMOUNT, ROW_AMOUNT, SPACE_LEFT_OF_PIECES, SPACE_ABOVE_PIECES

class Board:
    def __init__(self):
        self.board = []
        self.white_left = self.black_left = 22
        self.create_board()
    
    def draw_board(self, screen):
        screen.blit(pygame.image.load("assets/board.png"), (SPACE_EITHER_SIDE, SPACE_TOP_BOTTOM))
        for row in range(ROW_AMOUNT):
            for col in range(COL_AMOUNT):
                pygame.draw.circle(screen, BLACK, (SPACE_LEFT_OF_PIECES + SPACE_BETWEEN_PIECES * col, SPACE_ABOVE_PIECES + SPACE_BETWEEN_PIECES * row), DOT_SIZE)
    
    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)
    
    def get_piece(self, row, col):
        return self.board[row][col]

    def create_board(self):
        for row in range(ROW_AMOUNT):
            self.board.append([])
            for col in range(COL_AMOUNT):
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
        for row in range(ROW_AMOUNT):
            for col in range(COL_AMOUNT):
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

    def get_diagonals(self, row, col):
        # order = return canupleft, canupright, candownleft, candownright
        if row % 2 != 0: # if even row
            if col % 2 != 0: #if even col
                return True, True, True, True
            else: # if odd col
                return False, False, False, False
        else: # if odd row
            if col % 2 != 0: # if even col
                return False, False, False, False
            else: # if odd col
                if row == 0: # if first row
                    if col > 0 and col < 8:
                        return False, False, True, True
                    elif col == 0:
                        return False, False, False, True
                    else: # if last col
                        return False, False, True, False
                elif row == 2: # if middle row
                    if col > 0 and col < 8:
                        return True, True, True, True
                    elif col == 0:
                        return False, True, False, True
                    else: # if last col
                        return True, False, True, False
                else: # if last row
                    if col > 0 and col < 8:
                        return True, True, False, False
                    elif col == 0:
                        return False, True, False, False
                    else: # if last col
                        return True, False, False, False

    def get_valid_moves(self, piece, turn, previous_piece, previous_move, places_been):
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        up = piece.row - 1
        down = piece.row + 1

        canupleft, canupright, candownleft, candownright = self.get_diagonals(piece.row, piece.col)

        # "You must keep moving the same piece"
        if previous_piece != None and self.get_piece(previous_piece[0], previous_piece[1]) != piece:
            return moves

        if self.get_piece(piece.row, left) == 0 and left >= 0:
            taken = []
            for other_piece in self.board[piece.row]:
                if other_piece == 0:
                    continue
                if other_piece.col == piece.col:
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
                        taken = [] # clear the taken pieces
            
            moves.update({(piece.row, left): taken})

        if self.get_piece(piece.row, right) == 0 and right <= 8:
            taken = []
            for other_piece in self.board[piece.row]:
                if other_piece == 0:
                    continue
                if other_piece.col == piece.col:
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
                        taken = [] # clear the taken pieces
            
            moves.update({(piece.row, right): taken})

        if self.get_piece(up, piece.col) == 0 and up >= 0:
            taken = []
            for row in self.board:
                other_piece = row[piece.col]
                if other_piece == 0:
                    continue
                if other_piece.row == piece.row:
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
                        taken = [] # clear the taken pieces
            
            moves.update({(up, piece.col): taken})

        if self.get_piece(down, piece.col) == 0 and down <= 4:
            taken = []
            for row in self.board:
                other_piece = row[piece.col]
                if other_piece == 0:
                    continue
                if other_piece.row == piece.row:
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
                        taken = [] # clear the taken pieces
            
            moves.update({(down, piece.col): taken})
        
        if canupleft:
            if self.get_piece(up, left) == 0:
                taken = []
                x = 0 - piece.row
                for row in self.board:
                    other_piece = row[piece.col + x]
                    x += 1
                    if other_piece == 0:
                        continue
                    if other_piece.row == piece.row: # if it's the piece you're moving
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
                            taken = [] # clear the taken pieces

                moves.update({(up, left): taken})

        if canupright:
            if self.get_piece(up, right) == 0:
                taken = []
                x = piece.row
                for row in self.board:
                    other_piece = row[piece.col + x]
                    x -= 1
                    if other_piece == 0:
                        continue
                    if other_piece.row == piece.row: # if it's the piece you're moving
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
                            taken = [] # clear the taken pieces

                moves.update({(up, right): taken})

        if candownleft:
            if self.get_piece(down, left) == 0:
                taken = []
                x = piece.row
                for row in self.board:
                    other_piece = row[piece.col + x]
                    x -= 1
                    if other_piece == 0:
                        continue
                    if other_piece.row == piece.row: # if it's the piece you're moving
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
                            taken = [] # clear the taken pieces

                moves.update({(down, left): taken})
        
        if candownright:
            if self.get_piece(down, right) == 0:
                taken = []
                x = 0 - piece.row
                for row in self.board:
                    other_piece = row[piece.col + x]
                    x += 1
                    if other_piece == 0:
                        continue
                    if other_piece.row == piece.row: # if it's the piece you're moving
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
                            taken = [] # clear the taken pieces

                moves.update({(down, right): taken})

        taking_move = False
        for move in moves:
            if len(moves[move]) > 0: # if there is a taking move
                taking_move = True
        if taking_move:
            for move in list(moves):
                if len(moves[move]) == 0: # if the move takes nothing
                    moves.pop(move)
        
        if len(places_been) > 0: 
            # cant move to the same place twice on a turn
            for place in places_been:
                if place in moves:
                    moves.pop(place)
            
            # cant move in the same direction twice in a row
            if previous_move[0] == 0 and previous_move[1] == -1 and (piece.row, left) in moves:
                moves.pop((piece.row, left))
            elif previous_move[0] == 0 and previous_move[1] == 1 and (piece.row, right) in moves:
                moves.pop((piece.row, right))
            elif previous_move[0] == -1 and previous_move[1] == 0 and (up, piece.col) in moves:
                moves.pop((up, piece.col))
            elif previous_move[0] == 1 and previous_move[1] == 0 and (down, piece.col) in moves:
                moves.pop((down, piece.col))
            elif previous_move[0] == 1 and previous_move[1] == 1 and (up, left) in moves:
                moves.pop((up, left))
            elif previous_move[0] == 1 and previous_move[1] == -1 and (up, right) in moves:
                moves.pop((up, right))
            elif previous_move[0] == -1 and previous_move[1] == 1 and (down, left) in moves:
                moves.pop((down, left))
            elif previous_move[0] == -1 and previous_move[1] == -1 and (down, right) in moves:
                moves.pop((down, right))

        return moves
