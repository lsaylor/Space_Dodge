'''
this is a button object that creates two different rects using pygame,
one being the image the user wants to use as the button background,
the other as the text of the button. 
it has three methods:

.update
(updates the screen and renders the image, and then the text)

.checkForInput
(checks to see if the button has been pressed)

.changeColor
'''
# ---dependencies--- #
import pygame
#intializing pygame dependencies
pygame.init()
pygame.font.init()
# ---creating global variables--- #
#global variables for fonts/font colors
FONT = pygame.font.SysFont("comicsans", 50)
COLOR_TEXT = "white"
HIGHLIGHT_COLOR_TEXT = "green"
#global dimensions for windows and defining main window (MENU) variables
WIDTH = 100
HEIGHT = 50
MENU = pygame.display.set_mode((WIDTH, HEIGHT))
#specifics for button. Replace BUTTON_IMAGE with "imagename.jpeg/png" to load a custom image
BUTTON_IMAGE = "default_button_bg.png"
BUTTON_SURFACE = pygame.image.load(BUTTON_IMAGE)
BUTTON_SURFACE = pygame.transform.scale(BUTTON_SURFACE, (WIDTH, HEIGHT))


class Button():
    def __init__(self, BUTTON_SURFACE, x_pos, y_pos, text_input):
        self.image = BUTTON_SURFACE
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_input = text_input
        self.text = FONT.render(self.text_input, True, COLOR_TEXT)
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
        self.in_range = False
        self.button_pressed = False

    def update(self, parent_menu):
        #from main_menu import MAIN_MENU
        parent_menu.blit(self.text, self.text_rect)
    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.in_range = True

    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = FONT.render(self.text_input, True, HIGHLIGHT_COLOR_TEXT)
        else:
            self.text = FONT.render(self.text_input, True, COLOR_TEXT)



#test code
'''
button = Button(BUTTON_SURFACE, 400, 300, "Hello World")
test = True
while test:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            test = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            button.checkForInput(pygame.mouse.get_pos())
    MENU.fill("white")
    button.update()
    button.changeColor(pygame.mouse.get_pos())
    pygame.display.update()
'''