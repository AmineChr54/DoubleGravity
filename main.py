import pygame
import logic.constants as constants
from levels import level1

# Constants
SCREEN_WIDTH = constants.SCREEN_WIDTH
SCREEN_HEIGHT = constants.SCREEN_HEIGHT
GAME_SPEED_DELAY = constants.GAME_SPEED_DELAY


# Initializations
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True
dt = 0

# GameStates
STATES = {IN_GAME := "IN_GAME", PAUSED := "PAUSED", MAIN_MENU := "MAIN_MENU", lEVELS_MENU := "lEVELS_MENU", SETTINGS_MENU := "SETTINGS_MENU"}

# Loading




# GlobalVariables
GAME_STATE = IN_GAME


def start_game():
    pass

start_game()

while running:
    pygame.time.delay(GAME_SPEED_DELAY)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if GAME_STATE == IN_GAME and pygame.KEYDOWN == pygame.K_z:
                level1.red.jump()
                print(level1.red.x, level1.red.y)
            elif GAME_STATE == IN_GAME and pygame.KEYDOWN in {pygame.K_d, pygame.K_q}:
                level1.red.move()
                print(level1.red.x, level1.red.y)

    screen.fill("purple")

    if GAME_STATE == IN_GAME:
        level1.show(screen)
    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()