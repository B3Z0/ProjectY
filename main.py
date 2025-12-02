import pygame
import sys
import random




# init the pygame beast
pygame.init()

# window size
WIDTH = 800
HEIGHT = 600

MIN_LENGTH = 4

difficulty = random.randint(0, 2)

with open("words.txt") as f:
    WORDS = [w.strip().lower() for w in f]
WORDS = [w for w in WORDS if len(w) == 5 and w.isalpha()]

secret_word = [w for w in WORDS if len(w) == (MIN_LENGTH + difficulty) and w.isalpha()]
current_guess = ['_'] * len(secret_word)
guesses: list[str] = []
max_guesses = 6 + difficulty
win_condition = difficulty + MIN_LENGTH
    
    
    
    
# create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("WSL Pygame — Let’s Gooo")



def score(guess: str, answer: str) -> list[int]:
    length = len(answer)
    score = 0
    score_list: list[int] = [0] * (length + 1)
    for i in range(length):
        if guess[i] in answer:
            score += 1
            score_list[i+1] += 1
        if guess[i] == answer[i]:
            score+=1
            score_list[i+1] += 1
    score_list[0] = score
    return score_list

def check_win(score: int, win_condition: int) -> bool:
    return score == win_condition




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
