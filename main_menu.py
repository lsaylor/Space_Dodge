import button
import game_1_main
import pygame
import time


WIDTH, HEIGHT = 1000, 800
MAIN_MENU = pygame.display.set_mode((WIDTH, HEIGHT))
MAIN_RUN = True
BACKGROUND_MAINMENU = pygame.image.load("default_button_bg.png")
pygame.display.set_caption("Space Dodge: Main Menu")
QUIT_BUTTON = button.Button(button.BUTTON_SURFACE, WIDTH/2 - len("QUIT")/2, HEIGHT - button.FONT.get_height() - 200, "QUIT")

def draw(background, quit):
    MAIN_MENU.blit(BACKGROUND_MAINMENU, (0,0))
    QUIT_BUTTON.update()


while MAIN_RUN:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            MAIN_RUN = False

    draw(BACKGROUND_MAINMENU, QUIT_BUTTON)
    