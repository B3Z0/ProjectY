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
answer_length = (MIN_LENGTH + difficulty)

with open("words.txt") as f:
    WORDS = [w.strip().lower() for w in f]
WORDS = [w for w in WORDS if len(w) == answer_length and w.isalpha()]

secret_words = [w for w in WORDS if len(w) == answer_length and w.isalpha()]
secret_word = random.choice(secret_words)
guess: str = ""
guesses: list[str] = []
max_guesses = 6 + difficulty
win_condition = difficulty + MIN_LENGTH
clock = pygame.time.Clock()
    
    
    
# create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("WSL Pygame — Let’s Gooo")



def score_function(guess: str, answer: str) -> list[int]:
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

def check_answer(guess: str, answer: str):
    if len(guess) != len(answer):
        print("Guess length incorrect")
        return
    elif guess not in WORDS:
        print("Word not in dictionary")
        return
    else:
        score = score_function(guess, answer)
        check_win(score[0], win_condition)
    
def fill_guess(secret_word: str, guess: str, event: pygame.event.Event) -> str:
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RETURN:
            check_answer(guess, secret_word)
        elif event.key == pygame.K_BACKSPACE:
            if len(guess) > 0:
                guess = guess[:-1]
        else:
            if len(guess) < len(secret_word):
                if event.unicode.isalpha():
                    guess += event.unicode.lower()
                    
    return guess

# main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False
        
        guess = fill_guess(secret_word, guess, event)
        

    print(guess)
    # fill the screen
    screen.fill((30, 30, 30))  # dark gray
    pygame.display.flip()      # draw that plasma
    clock.tick(30)


# clean exit
pygame.quit()
sys.exit()
