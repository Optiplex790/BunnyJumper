import pygame, time
from levels import *
from display import *

start = time.time()
clock = pygame.time.Clock()
pygame.display.set_icon(icon)
pygame.display.set_caption("Bunny Jumper")

level_transition = 0
level_timer = 0
level_animation = 0
current_frame = 0

bunny_group, special_logic, background_image = level1()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False
    dt = time.time() - start
    start = time.time()

    #Special level logic, if special is equal to -1 there is no special logic
    if special_logic != -1:
        if special_logic == 1:
            if pygame.mouse.get_pressed()[0]:
                level_transition = 1
        if special_logic == 2:
            level_animation = 1

    if level_transition != 0:
        #Draw level transitions
        #Level 0 to 1 transition
        if level_transition == 1:
            #Level timer should be animation frames * 3 - 1
            level_timer += 1
            screen.blit(background1_list[math.floor(level_timer/3)])
            if level_timer == 188:
                bunny_group, special_logic, background_image = level2()
                level_timer = 0
                level_transition = 0
                current_frame = 0
    elif level_animation != 0 :
        #Level 1's (tutorial) animation
        if level_animation == 1:
            level_timer += 1
            #Does text box going up
            if 100 <= level_timer < 204:
                current_frame = math.floor((level_timer-100)/3)
                screen.blit(background_image[current_frame], (0,0))

            if current_frame == 34 and pygame.mouse.get_pressed()[0]:
                level_timer = 0
                current_frame += 1
            if 35 <= current_frame < 64:
                current_frame = math.floor(level_timer/3)+35
                screen.blit(background_image[current_frame], (0, 0))
            if current_frame == 64:
                level_timer = 1000
    else:
        # fill background if not in a transition state
        screen.blit(background_image[current_frame], (0, 0))
    print(current_frame)

    #Bunny logic
    if pygame.mouse.get_pressed()[0]:
        mousepos = pygame.mouse.get_pos()
        for bunny in bunny_group:
            if bunny.rect.collidepoint(mousepos):
                bunny.hit()

    for bunny in bunny_group:
        bunny.update()
    for bunny in bunny_group:
        bunny.draw(screen)

    #Draw overlay
    screen.blit(overlay1_img, (0,0))
    #pygame.draw.circle(screen, (255,0,0), (512, 384), 3)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

#TODO: LEVEL SYSTEM, MENU, SETTINGS, DRAWINGS, AUDIO
