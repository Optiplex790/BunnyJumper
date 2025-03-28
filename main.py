import pygame, time
from bunny_logic import *
from display import *

start = time.time()
clock = pygame.time.Clock()

bunny_group = []

for i in range(3):
    bunny_group.append(Bunny((i*70,668), (10, -20)))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False
    dt = time.time() - start
    start = time.time()

    if pygame.mouse.get_pressed()[0]:
        mousepos = pygame.mouse.get_pos()
        for bunny in bunny_group:
            if bunny.rect.collidepoint(mousepos):
                bunny.hit()

    # fill background
    screen.blit(background1_img, (0,0))


    for bunny in bunny_group:
        bunny.update()
    for bunny in bunny_group:
        bunny.draw(screen)

    #Draw overlay
    screen.blit(overlay1_img, (0,0))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
