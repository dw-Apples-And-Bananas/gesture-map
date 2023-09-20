import pygame
import sys
from trail import trail
from components.mouse import Mouse


class Application():
    def __init__(self):
        pygame.init()
        # self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.screen = pygame.display.set_mode((800,600))
        pygame.display.set_caption("Gesture Map")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('Arial', 20)
        self.mouse = Mouse()
        self.loop()

    def loop(self):
        self.alive = True
        while self.alive:
            for event in pygame.event.get():
                self.mouse.update(event)
                if event.type == pygame.QUIT:
                    self.alive = False

            mouse_pressed = pygame.mouse.get_pressed()[0]
            mouse_pos = pygame.mouse.get_pos()

            if self.mouse.tapped():
                print("tap")

            self.screen.fill((0,0,0))

            trail(self.screen, mouse_pressed, mouse_pos)

            fps_text = self.font.render("FPS: {}".format(int(self.clock.get_fps())), True, (180,180,180))
            self.screen.blit(fps_text, (10, 10))

            pygame.display.update()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()
            

Application()
