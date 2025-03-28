import pygame, time
from bunny_logic import *
from display import *

start = time.time()
clock = pygame.time.Clock()

new_bunny = Bunny((0,668))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            new_bunny.hit()
    dt = time.time() - start
    start = time.time()

    # fill background
    screen.fill((27, 66, 52))
    new_bunny.update()
    new_bunny.draw(screen)


    pygame.display.flip()
    clock.tick(60)

pygame.quit()
