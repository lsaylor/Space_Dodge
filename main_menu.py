import button
import pygame
import game_1_main

WIDTH, HEIGHT = 1000, 800
MAIN_MENU = pygame.display.set_mode((WIDTH, HEIGHT))
MAIN_RUN = True
BG_MAINMENU = pygame.image.load("main_menu_bg.png")
BG_MAINMENU = pygame.transform.scale(BG_MAINMENU, (WIDTH, HEIGHT))
pygame.display.set_caption("Space Dodge: Main Menu")
GEN_HEIGHT = button.FONT.get_height()

QUIT_TEXT = "QUIT"
Q_WIDTH = len(QUIT_TEXT)
QUIT_BUTTON = button.Button(button.BUTTON_SURFACE, WIDTH/2-Q_WIDTH/2, HEIGHT-GEN_HEIGHT-200, "QUIT")

PLAY_TEXT = "PLAY"
P_WIDTH = len(PLAY_TEXT)
PLAY_BUTTON = button.Button(button.BUTTON_SURFACE,WIDTH/2-P_WIDTH/2, HEIGHT-GEN_HEIGHT-500, "PLAY")

CLOCK = pygame.time.Clock()

while MAIN_RUN:
    CLOCK.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            MAIN_RUN = False
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            QUIT_BUTTON.checkForInput(pygame.mouse.get_pos())
            if QUIT_BUTTON.in_range:
                MAIN_RUN = False
                pygame.quit()
            PLAY_BUTTON.checkForInput(pygame.mouse.get_pos())
            if PLAY_BUTTON.in_range:
                game_1_main.main()

    MAIN_MENU.blit(BG_MAINMENU, (0,0))
    QUIT_BUTTON.changeColor(pygame.mouse.get_pos())
    QUIT_BUTTON.update(MAIN_MENU)
    PLAY_BUTTON.changeColor(pygame.mouse.get_pos())
    PLAY_BUTTON.update(MAIN_MENU)
    pygame.display.update()