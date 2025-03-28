import pygame

screen_width = 1024
screen_height = 768
screen = pygame.display.set_mode((screen_width, screen_height), flags=pygame.SRCALPHA, vsync=1)

#load images
bunny_spritesheet = pygame.image.load("media/BunnyParts-Sheet.png").convert_alpha()
bunny_jump_spritesheet = pygame.image.load("media/BunnyJump-Sheet.png").convert_alpha()
bunny_hit_spritesheet = pygame.image.load("media/BunnyHit-Sheet.png").convert_alpha()