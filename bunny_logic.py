import pygame, math, random
from display import *

#Break apart sprite sheet into different frames in a list
bunny_jump_frames = []
bunny_hit_frames = []
bunny_parts = []

for i in range(9):
    bunny_jump_frames.append(pygame.surface.Surface((70,70), flags=pygame.SRCALPHA))
    bunny_jump_frames[i].blit(bunny_spritesheet, (-i*70,0))
for i in range(18):
    bunny_hit_frames.append(pygame.surface.Surface((70, 70), flags=pygame.SRCALPHA))
    bunny_hit_frames[i].blit(bunny_hit_spritesheet, (-i * 70, 0))
for i in range(3):
    bunny_parts.append(pygame.surface.Surface((70, 70), flags=pygame.SRCALPHA))
    bunny_parts[i].blit(bunny_spritesheet, (-i * 70, 0))

class Bunny():
    def __init__(self,position):
        #Handle image info
        scale = 1.5

        #Bunny itself
        self.head_img = bunny_parts[0]
        self.body_img = bunny_parts[1]
        self.tail_img = bunny_parts[2]
        self.head_img = pygame.transform.scale_by(self.head_img,scale)
        self.body_img = pygame.transform.scale_by(self.body_img, scale)
        self.tail_img = pygame.transform.scale_by(self.tail_img, scale)


        #Hit animation
        self.hit_frames = bunny_hit_frames
        for i in range(len(self.hit_frames)):
            self.hit_frames[i] = pygame.transform.scale_by(self.hit_frames[i], scale)

        #Handle rect info
        self.rect = self.body_img.get_frect()
        self.rect.scale_by(1.1, 1.1)
        self.rect.x = position[0]
        self.rect.y = position[1]

        #Handle other variables
        self.xaccel = 20
        self.yaccel = -20
        self.caught = 0
        self.time = pygame.time.get_ticks()

    def update(self):
        #Physics
        #self.yaccel += 0.4
        self.xaccel *= 0.99
        self.yaccel *= 0.99

        self.rect.x += self.xaccel
        self.rect.y += self.yaccel

        #Caught Animation
        if self.caught != 0 and self.caught != 18:
            self.caught += 1
        if self.caught >= 18:
            if pygame.time.get_ticks() - self.time >= 200:
                self.time = pygame.time.get_ticks()
                self.caught = random.randint(18,18)

        self.xaccel = 0
        self.yaccel = 0


    def hit(self):
        if not self.caught:
            self.xaccel = random.randint(-4,4)
            self.yaccel = -10
            self.caught = True

    def draw(self, screen):
        if self.caught != 0:
            screen.blit(self.hit_frames[math.floor(self.caught/3)+9], (self.rect.x, self.rect.y))
            screen.blit(self.tail_img, (self.rect.x - (self.xaccel/100)*10, self.rect.y - (self.yaccel/100)*10))
            screen.blit(self.body_img, (self.rect.x, self.rect.y))
            screen.blit(self.head_img, (self.rect.x-(self.xaccel/100)*10, self.rect.y-(self.yaccel/100)*10))
            screen.blit(self.hit_frames[math.floor(self.caught/3)], (self.rect.x, self.rect.y))
        else:
            screen.blit(self.tail_img, (self.rect.x - self.xaccel * 0.5, self.rect.y - self.yaccel * 0.5))
            screen.blit(self.body_img, (self.rect.x, self.rect.y))
            screen.blit(self.head_img, (self.rect.x - self.xaccel * 0.5, self.rect.y - self.yaccel * 0.5))

#TODO: CHANGE HIT ANIMATION IMAGE TO BE INSIDE OF UPDATE INSTEAD OF DRAW