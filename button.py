

import pygame
import sys

pygame.init()

fps = 60
timer = pygame.time.Clock()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Button!")
font = pygame.font.SysFont("cambria", 18)


'''This is a class to make an interactable button object on the screen'''
class Button:
    # Initialization for the button
    def __init__(self, text, x_pos, y_pos, 
                 button_width, button_height, enabled):
        self.text = text
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.button_width = button_width
        self.button_height = button_height
        self.enabled = enabled
        self.draw()

    # Draw function to make the buttom appear on the screen
    def draw(self):
        button_text = font.render(self.text, True, 'black')
        button_rect = pygame.rect.Rect((self.x_pos, self.y_pos), (self.button_width, self.button_height))
        # If the button is enabled, it can be interacted with
        if self.enabled: 
            # This interacts with clicks   
            if self.check_click():
                pygame.draw.rect(screen, 'black', button_rect, 0, 5)
            # This interacts with mouse hover
            elif self.check_hover():
                pygame.draw.rect(screen, 'dark gray', button_rect, 0, 5)
            # This is how the button appears otherwise
            else:
                pygame.draw.rect(screen, 'light gray', button_rect, 0, 5)
        # If the button is disabled, it appears different
        # And cannot be interacted with
        else:
            pygame.draw.rect(screen, 'red', button_rect, 0, 5)
        pygame.draw.rect(screen, 'black', button_rect, 2, 5)
        screen.blit(button_text, (self.x_pos + 3, self.y_pos + 3))

    # Handle mouse click event
    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        left_click = pygame.mouse.get_pressed()[0]
        button_rect = pygame.rect.Rect((self.x_pos, self.y_pos), (self.button_width, self.button_height))
        if left_click and button_rect.collidepoint(mouse_pos) and self.enabled:
            return True
        else:
            return False
    
    # Handle mouse hover event
    def check_hover(self):
        mouse_pos = pygame.mouse.get_pos()
        button_rect = pygame.rect.Rect((self.x_pos, self.y_pos), (self.button_width, self.button_height))
        if button_rect.collidepoint(mouse_pos):
            return True
        else:
            return False
        


'''

run = True

while run:
    screen.fill('white')
    timer.tick(fps)

    my_button = Button('Click Me!', 10, 10, 250, 25, True)
    my_button2 = Button('Click Me Too!', 10, 40, 250, 25, True)
    my_button3 = Button('Click Me Three!', 10, 70, 250, 25, False)



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()

pygame.quit()

'''