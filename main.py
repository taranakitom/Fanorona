import pygame, sys
from button import Button
from fanorona.board import Board

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
FPS = 60

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

BG = pygame.image.load("assets/Background.png")

clock = pygame.time.Clock()

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

def get_mouse_row_col(pos):
    x, y = pos
    row = y // 82 - 2
    col = x // 82 - 3
    return row, col

def play():
    pygame.display.set_caption("Play")
    player = 1
    board = Board()
    while True:
        clock.tick(FPS)

        SCREEN.fill("black")

        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        if player == 1:
            PLAYER1_TEXT = get_font(75).render("1", True, "Green")
            PLAYER2_TEXT = get_font(75).render("2", True, "White")
        else:
            PLAYER1_TEXT = get_font(75).render("1", True, "White")
            PLAYER2_TEXT = get_font(75).render("2", True, "Green")
        
        PLAYER1_RECT = PLAYER1_TEXT.get_rect(center=(1100, 650))
        PLAYER2_RECT = PLAYER2_TEXT.get_rect(center=(1200, 650))

        PLAY_BACK = Button(image=None, pos=(200, 650), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        SCREEN.blit(PLAYER1_TEXT, PLAYER1_RECT)
        SCREEN.blit(PLAYER2_TEXT, PLAYER2_RECT)

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        board.draw(SCREEN)

        for button in [PLAY_BACK]:
            button.changeColor(PLAY_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                row, col = get_mouse_row_col(PLAY_MOUSE_POS)
                piece = board.get_piece(row, col)
                
        
        pygame.display.update()
        
def learn():
    pygame.display.set_caption("Learn")
    page = 1
    
    while True:
        clock.tick(FPS)

        SCREEN.fill("black")
        
        LEARN_MOUSE_POS = pygame.mouse.get_pos()

        PAGE_NUMBER_TEXT = get_font(50).render(f"Page: {str(page)}", True, "#b68f40")
        PAGE_NUMBER_RECT = PAGE_NUMBER_TEXT.get_rect(center=(640, 50))

        LEARN_BACK = Button(image=None, pos=(200, 650), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")
        LEARN_BACKWARDS = Button(image=pygame.transform.scale(pygame.image.load("assets/arrow_left.jpg"), (100, 100)), pos=(1100, 650), 
                            text_input="", font=get_font(75), base_color="White", hovering_color="Green")
        LEARN_FORWARDS = Button(image=pygame.transform.scale(pygame.image.load("assets/arrow_right.jpg"), (100, 100)), pos=(1200, 650), 
                            text_input="", font=get_font(75), base_color="White", hovering_color="Green")

        SCREEN.blit(PAGE_NUMBER_TEXT, PAGE_NUMBER_RECT)
        SCREEN.blit(pygame.image.load(f"assets/learning_pages/{page}.png"), ((SCREEN_WIDTH - 1100) / 2, 90))

        LEARN_BACK.changeColor(LEARN_MOUSE_POS)
        LEARN_BACK.update(SCREEN)

        for button in [LEARN_BACK, LEARN_BACKWARDS, LEARN_FORWARDS]:
            button.changeColor(LEARN_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if LEARN_BACK.checkForInput(LEARN_MOUSE_POS):
                    main_menu()
                if LEARN_BACKWARDS.checkForInput(LEARN_MOUSE_POS):
                    if page <= 1:
                        pass
                    else:
                        page -= 1
                if LEARN_FORWARDS.checkForInput(LEARN_MOUSE_POS):
                    if page >= 9:
                        pass
                    else:
                        page += 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if page <= 1:
                        pass
                    else:
                        page -= 1
                if event.key == pygame.K_RIGHT:
                    if page >= 9:
                        pass
                    else:
                        page += 1

        
        pygame.display.update()

def credits():
    pygame.display.set_caption("Credits")
    while True:
        clock.tick(FPS)

        SCREEN.fill("black")

        CREDITS_MOUSE_POS = pygame.mouse.get_pos()

        CREDITS_RECT = pygame.Rect((10, 10), (640, 360))

        CREDITS_BACK = Button(image=None, pos=(200, 650), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        SCREEN.blit(pygame.image.load(f"assets/credits.png"), CREDITS_RECT)

        CREDITS_BACK.changeColor(CREDITS_MOUSE_POS)
        CREDITS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if CREDITS_BACK.checkForInput(CREDITS_MOUSE_POS):
                    main_menu()
        
        pygame.display.update()

def main_menu():
    pygame.display.set_caption("Main menu")
    while True:
        clock.tick(FPS)

        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("FANORONA", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250), 
                            text_input="PLAY", font=get_font(75), base_color="White", hovering_color="Green")
        LEARN_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 400), 
                            text_input="LEARN", font=get_font(75), base_color="White", hovering_color="Green")
        CREDITS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 550), 
                            text_input="CREDITS", font=get_font(75), base_color="White", hovering_color="Green")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, LEARN_BUTTON, CREDITS_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if LEARN_BUTTON.checkForInput(MENU_MOUSE_POS):
                    learn()
                if CREDITS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    credits()

        pygame.display.update()

main_menu()