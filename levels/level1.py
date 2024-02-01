import pygame
import logic.constants as constants
import components.red as red

SCREEN_WIDTH = constants.SCREEN_WIDTH
SCREEN_HEIGHT = constants.SCREEN_HEIGHT
SCREEN_LEFT_EDGE_X = constants.SCREEN_LEFT_EDGE_X
SCREEN_RIGHT_EDGE_X = constants.SCREEN_RIGHT_EDGE_X
SCREEN_UPPER_EDGE_Y = constants.SCREEN_UPPER_EDGE_Y
SCREEN_LOWER_EDGE_Y = constants.SCREEN_LOWER_EDGE_Y


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
game_background_image = pygame.image.load("assets/images/game.jpg").convert(screen)
red_image = pygame.image.load("assets/images/red.jpg").convert(screen)
blue_image = pygame.image.load("assets/images/blue.jpg").convert(screen)
horizontal_wall_image = pygame.image.load("assets/images/horizontalWall.jpg").convert(screen)
vertical_wall_image = pygame.image.load("assets/images/verticalWall.jpg").convert(screen)

red= red.red()
def show(screen):
    screen.blit(game_background_image, (0, 0))
    screen.blit(red_image, (red.x, red.y))
