import pygame
from pygame.locals import *
from trail import trail

pygame.init()
screen = pygame.display.set_mode((0,0), FULLSCREEN)
clock = pygame.time.Clock()

font = pygame.font.SysFont('Arial', 20)

running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    mouse_pressed = pygame.mouse.get_pressed()[0]
    mouse_pos = pygame.mouse.get_pos()

    screen.fill((0,0,0))

    trail(screen, mouse_pressed, mouse_pos)

    fps_text = font.render("FPS: {}".format(int(clock.get_fps())), True, (180,180,180))
    screen.blit(fps_text, (10, 10))

    pygame.display.update()
    clock.tick(60)


pygame.quit()
