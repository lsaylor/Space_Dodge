import button
import game_1_main
import pygame
import time


WIDTH, HEIGHT = 1000, 800
MAIN_MENU = pygame.display.set_mode((WIDTH, HEIGHT))
MAIN_RUN = True
BACKGROUND_MAINMENU = pygame.image.load("menu_background.png")
pygame.display.set_caption("Space Dodge: Main Menu")

QUIT_TEXT = "QUIT"
Q_WIDTH = len(QUIT_TEXT)
Q_HEIGHT = button.FONT.get_height()
QUIT_BUTTON = button.Button(button.BUTTON_SURFACE, WIDTH/2-Q_WIDTH/2, HEIGHT-Q_HEIGHT-200, "QUIT")

def draw(main_bg, bg_quit):
    main_bg.blit(BACKGROUND_MAINMENU, (0,0))
    bg_quit.update()


while MAIN_RUN:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            MAIN_RUN = False

    draw(BACKGROUND_MAINMENU, QUIT_BUTTON)
    