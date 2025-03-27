import pygame

screen_width = 1024
screen_height = 768
screen = pygame.display.set_mode((screen_width, screen_height), flags=pygame.SRCALPHA, vsync=1)

#load images
bunny_spritesheet = pygame.image.load("media/bunny-sprite-sheet.png").convert_alpha()