import pygame
import sys
from trail import trail
from components.mouse import Mouse
import gesture
import platform


class Application():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800,600))
        # if platform.system() == "Linux":
        #     self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        # else:
        #     self.screen = pygame.display.set_mode((800,600))
        pygame.display.set_caption("Gesture Map")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('Arial', 20)
        self.mouse = Mouse()
        self.points = []
        self.loop()

    def loop(self):
        self.alive = True
        while self.alive:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pass
                if event.type == pygame.MOUSEBUTTONUP:
                    print(gesture.get(self.points))
                    # print(f"start: {self.points[0]}\nend: {self.points[-1]}")
                    self.points = []
                self.mouse.update(event)
                if event.type == pygame.QUIT:
                    self.alive = False
            mouse_pressed = pygame.mouse.get_pressed()[0]
            mouse_pos = pygame.mouse.get_pos()
            if mouse_pressed:
                self.points.append(mouse_pos)
            self.screen.fill((0,0,0))
            trail(self.screen, mouse_pressed, mouse_pos)

            fps_text = self.font.render("FPS: {}".format(int(self.clock.get_fps())), True, (180,180,180))
            self.screen.blit(fps_text, (10, 10))

            if mouse_pos == (0,0):
                self.alive = False

            pygame.display.update()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()

Application()
