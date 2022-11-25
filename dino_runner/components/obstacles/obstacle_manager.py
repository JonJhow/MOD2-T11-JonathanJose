import pygame
import random

from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird


class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        self.obstacle_index = 0

    def update(self, game):
        if len(self.obstacles) == 0:            
            self.obstacle_index = random.randint(0, 2)
            if self.obstacle_index == 0:
                self.obstacles.append(Cactus(SMALL_CACTUS))
            elif self.obstacle_index == 1:
                self.obstacles.append(Cactus(LARGE_CACTUS))
            elif self.obstacle_index == 2:
                self.obstacles.append(Bird())
                    
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.has_power_up:
                    pygame.time.delay(500)
                    game.playing = False
                    game.death_count += 1
                    break
                else:
                    self.obstacles.remove(obstacle)

    def reset_obstacles(self):
        self.obstacles = []

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)