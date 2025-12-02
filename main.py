import pygame
import sys
import random




# init the pygame beast
pygame.init()

# window size
WIDTH = 800
HEIGHT = 600

difficulty = random.randint(0, 2)

with open("words.txt") as f:
    WORDS = [w.strip().lower() for w in f]
WORDS = [w for w in WORDS if len(w) == 5 and w.isalpha()]

secret_word = [w for w in WORDS if len(w) == (4 + difficulty) and w.isalpha()]
current_guess = ['_'] * len(secret_word)
guesses: list[str] = []
max_guesses = 6 + difficulty
    
    
    
    
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
