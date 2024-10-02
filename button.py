import pygame
import game_1_main
pygame.font.init()
WIDTH = 1000
HEIGHT = 800
MENU = pygame.display.setmode(WIDTH, HEIGHT)
FONT = pygame.font.SysFont("comicsans", 50)
pygame.display.set_caption("Space Dodge")

class Button():
    def __init__(self, image, x_pos, y_pos, text_input):
        self.image = image
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        