import pygame
import sys

# init the pygame beast
pygame.init()

# window size
WIDTH = 800
HEIGHT = 600

# create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("WSL Pygame — Let’s Gooo")

# main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen
    screen.fill((30, 30, 30))  # dark gray
    pygame.display.flip()      # draw that plasma

# clean exit
pygame.quit()
sys.exit()
