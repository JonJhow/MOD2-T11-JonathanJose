import pygame
from pygame.sprite import Sprite

from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING, DEFAULT_TYPE, SHIELD_TYPE, DUCKING_SHIELD, JUMPING_SHIELD, RUNNING_SHIELD, HAMMER_TYPE, DUCKING_HAMMER, JUMPING_HAMMER, RUNNING_HAMMER, BLACK_HEART_TYPE, RUNNING_BH, JUMPING_BH, DUCKING_BH
from dino_runner.components import sound_board

X_POS = 80
Y_POS = 310
JUMP_VEL = 8.5

DUCK_IMG = {DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD, HAMMER_TYPE: DUCKING_HAMMER, BLACK_HEART_TYPE: DUCKING_BH}
JUMP_IMG = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD, HAMMER_TYPE: JUMPING_HAMMER, BLACK_HEART_TYPE: JUMPING_BH}
RUN_IMG = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD, HAMMER_TYPE: RUNNING_HAMMER, BLACK_HEART_TYPE: RUNNING_BH}


class Dinosaur:
    def __init__(self):
        self.type= DEFAULT_TYPE
        self.image = RUN_IMG[self.type][0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y - Y_POS
        self.step_index = 0
        self.dino_run = True
        self.dino_jump = False
        self.dino_drop = False
        self.dino_duck = False
        self.is_dino_ducking = False
        self.jump_vel = JUMP_VEL
        self.setup_state()

    def setup_state(self):
        self.has_power_up = False
        self.hammer = False
        self.black_heart = False
        self.show_text = False

    def update(self, user_input):
        if self.dino_run:
            self.run()
        elif self.dino_jump:
            self.jump()
        elif self.dino_drop:
            self.jump_drop()
        elif self.dino_duck:
            self.duck()

        if user_input[pygame.K_UP] and not self.dino_jump and not self.black_heart:
            sound_board.play_jump()
            self.dino_run = False
            self.dino_duck = False
            self.dino_jump = True
            self.dino_drop = False
        elif user_input[pygame.K_DOWN] and self.dino_jump:
            self.dino_jump = False
            self.dino_drop = True
        elif user_input[pygame.K_DOWN] and not self.dino_jump and not self.dino_drop and not self.black_heart:
            if not self.is_dino_ducking:
                sound_board.play_duck()
            self.is_dino_ducking = True
            self.dino_run = False
            self.dino_duck = True
            self.dino_jump = False
            self.dino_drop = False
        elif not self.dino_jump and not self.dino_duck and not self.dino_drop:
            self.is_dino_ducking = False
            self.dino_run = True
            self.dino_duck = False
            self.dino_jump = False
            self.dino_drop = False

        if self.dino_jump == False:
            self.jump_vel = JUMP_VEL

        if self.step_index >= 9:
            self.step_index = 0

    def run(self):
        self.image = RUN_IMG[self.type][self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        self.step_index += 1

    def jump(self):
        self.image = JUMP_IMG[self.type]
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8

        if self.jump_vel < -JUMP_VEL:
            self.dino_rect.y = Y_POS
            self.dino_jump = False

        self.step_index += 1

    def jump_drop(self):
        self.image = JUMP_IMG[self.type]
        drop_vel = 11
        self.dino_rect.y += drop_vel * 4
        drop_vel += 2

        if self.dino_rect.y >= Y_POS:
            self.dino_rect.y = Y_POS
            self.dino_drop = False

        self.step_index += 1

    def duck(self):
        self.image = DUCK_IMG[self.type][self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS + 30
        self.step_index += 1
        self.dino_duck = False

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))