import pygame
from display import *

#Break apart sprite sheet into different frames in a list
bunny_frames = []

for i in range(9):
    bunny_frames.append(pygame.surface.Surface((41,50), flags=pygame.SRCALPHA))
    bunny_frames[i].blit(bunny_spritesheet, (-i*41,0))


class Bunny():
    def __init__(self,position):
        self.frames = bunny_frames
        for i in range(len(self.frames)):
            self.frames[i] = pygame.transform.scale_by(self.frames[i], 1.5)
        self.image = self.frames[0]
        self.rect = self.image.get_frect()
        self.rect.scale_by(1.1, 1.1)
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.xaccel = 20
        self.yaccel = -20

    def update(self):
        self.yaccel += 0.4
        self.xaccel *= 0.99
        self.yaccel *= 0.98

        self.rect.x += self.xaccel
        self.rect.y += self.yaccel

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))