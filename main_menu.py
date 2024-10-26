import pygame
import button
import game_1_main

WIDTH, HEIGHT = 1000, 800

screen_info = pygame.display.Info()
screen_width, screen_height = screen_info.current_w, screen_info.current_h
MAIN_MENU = pygame.display.set_mode((WIDTH, HEIGHT))
BG_MAINMENU = pygame.image.load("main_menu_bg.png").convert()
BG_MAINMENU = pygame.transform.scale(BG_MAINMENU, (WIDTH, HEIGHT))




BG_BUTTONS = pygame.image.load("default_button_bg.png")
BG_BUTTONS = pygame.transform.scale(BG_BUTTONS, (button.WIDTH, button.HEIGHT))
GEN_HEIGHT = button.FONT.get_height()
QUIT_TEXT = "QUIT"
Q_WIDTH = len(QUIT_TEXT)
QUIT_BUTTON = button.Button(BG_BUTTONS, WIDTH/2-Q_WIDTH/2, HEIGHT-GEN_HEIGHT-200, "QUIT")

PLAY_TEXT = "PLAY"
P_WIDTH = len(PLAY_TEXT)
PLAY_BUTTON = button.Button(BG_BUTTONS,WIDTH/2-P_WIDTH/2, HEIGHT-GEN_HEIGHT-400, "PLAY")


TITLE_TEXT = "Space Dodge"
TITLE_FONT = pygame.font.SysFont("comicsans", 100)
T_WIDTH = len(TITLE_TEXT)
TITLE = button.Button(BG_BUTTONS,WIDTH/2-P_WIDTH/2,HEIGHT-GEN_HEIGHT-550, "Space Dodge",TITLE_FONT, "red")

OPTIONS_TEXT = "OPTIONS"
O_WIDTH = len(OPTIONS_TEXT)
OPTIONS_BUTTON = button.Button(BG_BUTTONS,WIDTH/2-P_WIDTH/2, HEIGHT-GEN_HEIGHT-300, "OPTIONS")


haspressed = True
def toggle_screen():
    global MAIN_MENU, haspressed, WIDTH, HEIGHT, BG_MAINMENU
    if haspressed:
        MAIN_MENU = pygame.display.set_mode((screen_width, screen_height))
        WIDTH = screen_width
        HEIGHT = screen_height
        haspressed = False
        print(str(screen_height))
    else:
        WIDTH = 1000
        HEIGHT = 800
        MAIN_MENU = pygame.display.set_mode((WIDTH, HEIGHT))
        haspressed = True
    BG_MAINMENU = pygame.transform.scale(BG_MAINMENU, (WIDTH, HEIGHT))


def main_menu():

    pygame.display.set_caption("Space Dodge: Main Menu")
    CLOCK = pygame.time.Clock()
    MAIN_RUN = True
    while MAIN_RUN:
        CLOCK.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                MAIN_RUN = False
                pygame.quit()
            if event.type == pygame.K_f:
                toggle_screen()
                #game_1_main.main()
            if event.type == pygame.MOUSEBUTTONDOWN:
                QUIT_BUTTON.checkForInput(pygame.mouse.get_pos())
                if QUIT_BUTTON.in_range:
                    MAIN_RUN = False
                    pygame.quit()
                PLAY_BUTTON.checkForInput(pygame.mouse.get_pos())
                if PLAY_BUTTON.in_range:
                    game_1_main.main()
                OPTIONS_BUTTON.checkForInput(pygame.mouse.get_pos())
                if OPTIONS_BUTTON.in_range:
                    options_menu()
                    MAIN_RUN = False

        MAIN_MENU.blit(BG_MAINMENU, (0,0))
        QUIT_BUTTON.changeColor(pygame.mouse.get_pos())
        QUIT_BUTTON.update(MAIN_MENU)
        OPTIONS_BUTTON.changeColor(pygame.mouse.get_pos())
        OPTIONS_BUTTON.update(MAIN_MENU)
        PLAY_BUTTON.changeColor(pygame.mouse.get_pos())
        PLAY_BUTTON.update(MAIN_MENU)
        TITLE.full_update(MAIN_MENU)
        pygame.display.update()


def options_menu():


    pygame.display.set_caption("Space Dodge: Options")
    CLOCK = pygame.time.Clock()
    OPTIONS_RUN = True

    
    BACK_BUTTON = button.Button(BG_BUTTONS, 100, 70, "MENU")


    while OPTIONS_RUN:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                OPTIONS_RUN = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                BACK_BUTTON.checkForInput(pygame.mouse.get_pos())
                if BACK_BUTTON.in_range:
                    OPTIONS_RUN = False
                    main_menu()
        

        MAIN_MENU.blit(BG_MAINMENU, (0,0))
        BACK_BUTTON.changeColor(pygame.mouse.get_pos())
        BACK_BUTTON.update(MAIN_MENU)
        pygame.display.update()


main_menu()