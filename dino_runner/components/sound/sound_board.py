import pygame

VOLUME = 0.2

def play_jump():
    jump_sound = pygame.mixer.Sound("dino_runner/Assets/Sound/SFX_Jump2.wav")
    jump_sound.set_volume(VOLUME)
    jump_sound.play()

def play_hit():
    hit_sound = pygame.mixer.Sound("dino_runner/Assets/Sound/SFX_Hit1.wav")
    hit_sound.set_volume(VOLUME)
    hit_sound.play()

def play_destroy_obstacle():
    dest_obst_sound = pygame.mixer.Sound("dino_runner/Assets/Sound/SFX_HitObstacle.wav")
    dest_obst_sound.set_volume(VOLUME)
    dest_obst_sound.play()