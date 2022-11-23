import random

from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD


class Bird(Obstacle):
    def __init__(self):
        self.image = BIRD
        self.type = 0
        self.fly_position = random.randint(1, 3)
        super().__init__(self.image, self.type)
        
    def fly(self, game):
        self.type = 0 if game.player.step_index > 5 else 1

        if self.fly_position == 1:
            self.rect.y = 340 if self.type == 0 else 326
        elif self.fly_position == 2:
            self.rect.y = 270 if self.type == 0 else 256
        elif self.fly_position == 3:
            self.rect.y = 230 if self.type == 0 else 216