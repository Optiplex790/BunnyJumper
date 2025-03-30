import pygame

screen_width = 1024
screen_height = 768
screen = pygame.display.set_mode((screen_width, screen_height), flags=pygame.SRCALPHA, vsync=1)

def animation_list(frames, width, height, image):
    img_list = []

    for i in range(frames):
        img_list.append(pygame.surface.Surface((width, height), flags=pygame.SRCALPHA))
        img_list[i].blit(image, (-i * width, 0))

    return img_list

#load images
icon = pygame.image.load("media/icon.png").convert_alpha()
bunny_spritesheet = pygame.image.load("media/BunnyParts-Sheet.png").convert_alpha()
bunny_hit_spritesheet = pygame.image.load("media/BunnyHit-Sheet.png").convert_alpha()

#Backgrounds
background1_img = pygame.image.load("media/Background1-Sheet.png").convert_alpha()
background2_img = pygame.image.load("media/Background2-Sheet.png").convert()
background1_list = animation_list(63, 1024, 768, background1_img)
background2_list = animation_list(65, 1024, 768, background2_img)

#Overlays
overlay1_img = pygame.image.load("media/Overlay1.png").convert_alpha()