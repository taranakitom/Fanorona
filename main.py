import pygame, sys
from button import Button

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

BG = pygame.image.load("assets/Background.png")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

def play():
    pygame.display.set_caption("Play")

def learn():
    pygame.display.set_caption("Learn")
    page = 1
    
    while True:
        SCREEN.fill("black")
        
        LEARN_MOUSE_POS = pygame.mouse.get_pos()

        PAGE_NUMBER_TEXT = get_font(50).render(f"Page: {str(page)}", True, "#b68f40")
        PAGE_NUMBER_RECT = PAGE_NUMBER_TEXT.get_rect(center=(640, 50))

        PAGE_RECT = pygame.Rect((10, 10), (640, 360))

        LEARN_BACK = Button(image=None, pos=(200, 650), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")
        LEARN_BACKWARDS = Button(image=pygame.transform.scale(pygame.image.load("assets/arrow_left.jpg"), (100, 100)), pos=(1100, 650), 
                            text_input="", font=get_font(75), base_color="White", hovering_color="Green")
        LEARN_FORWARDS = Button(image=pygame.transform.scale(pygame.image.load("assets/arrow_right.jpg"), (100, 100)), pos=(1200, 650), 
                            text_input="", font=get_font(75), base_color="White", hovering_color="Green")

        SCREEN.blit(PAGE_NUMBER_TEXT, PAGE_NUMBER_RECT)
        SCREEN.blit(pygame.image.load(f"assets/learning_pages/{page}.jpg"), PAGE_RECT)

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
                    if page < 2:
                        pass
                    else:
                        page -= 1
                if LEARN_FORWARDS.checkForInput(LEARN_MOUSE_POS):
                    if page > 9:
                        pass
                    else:
                        page += 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if page < 2:
                        pass
                    else:
                        page -= 1
                if event.key == pygame.K_RIGHT:
                    if page > 9:
                        pass
                    else:
                        page += 1

        
        pygame.display.update()

def credits():
    pygame.display.set_caption("Credits")
    while True:
        CREDITS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        CREDITS_BACK = Button(image=None, pos=(200, 600), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

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