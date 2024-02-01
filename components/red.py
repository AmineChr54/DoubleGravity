import pygame
from logic import constants

SCREEN_LEFT_EDGE_X = constants.SCREEN_LEFT_EDGE_X
SCREEN_RIGHT_EDGE_X = constants.SCREEN_RIGHT_EDGE_X
SCREEN_UPPER_EDGE_Y = constants.SCREEN_UPPER_EDGE_Y
SCREEN_LOWER_EDGE_Y = constants.SCREEN_LOWER_EDGE_Y
RED_WIDTH = constants.RED_WIDTH
RED_HEIGHT = constants.RED_HEIGHT
class red():
    def __init__(self,x=100,y=500,v_down=50,v_up=0):
        self.x = x
        self.y = y
        self.v_down = v_down
        self.v_up = v_up

    def update(self):
        if self.x in range(SCREEN_RIGHT_EDGE_X,SCREEN_LEFT_EDGE_X-1-RED_WIDTH):
            pass
        if self.y in range(SCREEN_UPPER_EDGE_Y,SCREEN_LOWER_EDGE_Y-1-RED_WIDTH):
            pass
    def jump(self):
        self.v_up += 50
        self.y += 10
    def move(self):
        if pygame.KEYDOWN == pygame.K_d:
            self.x += 2
        if pygame.KEYDOWN == pygame.K_q:
            self.x -= 2
    def is_falling(self):
        return self.v_up != 0 or self.v_down != 0