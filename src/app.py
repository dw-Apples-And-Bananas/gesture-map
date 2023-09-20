import pygame
import sys
from trail import trail
from components.mouse import Mouse
import gesture
import platform


class Application():
    def __init__(self):
        pygame.init()
        # self.screen = pygame.display.set_mode((200, 200))
        if platform.system() == "Linux":
            self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode((800,600))
        pygame.display.set_caption("Gesture Map")
        self.size = pygame.display.get_window_size()
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('Arial', 24)
        self.mouse = Mouse()
        self.points = []
        self.log = ""
        self.loop()

    def loop(self):
        self.alive = True
        while self.alive:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.log = str(event)
                if event.type == pygame.MOUSEBUTTONUP:
                    if len(self.points) > 0:
                        gesture_list = gesture.get(self.points)
                        if gesture_list != []:
                            gesture.run(gesture_list[0])
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

            log_text = self.font.render(self.log, True, (255,255,255))
            self.screen.blit(log_text, (10, self.size[1]-30))

            if mouse_pos[0] < 10 and mouse_pos[1] < 10 and platform.system() == "Linux":
                self.alive = False

            pygame.display.update()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()

Application()
