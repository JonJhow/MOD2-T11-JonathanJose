import random

from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS

Y_POS = 325


class Cactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        
        if self.image == SMALL_CACTUS:
            self.rect.y = Y_POS
        elif self.image == LARGE_CACTUS:
            self.rect.y = Y_POS - (LARGE_CACTUS[0].get_height() - SMALL_CACTUS[0].get_height())