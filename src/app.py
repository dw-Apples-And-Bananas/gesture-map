import pygame
import sys
from trail import trail
from components.mouse import Mouse
import gesture
import platform
import time


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
        self.font = pygame.font.SysFont('Arial', 18)
        self.mouse = Mouse()
        self.fingers = 0
        self.holdtime = 0
        self.holdpos = (0, 0)
        self.holding = False
        self.logtext = ""
        self.points = []
        self.loop()


    def loop(self):
        self.alive = True
        while self.alive:
            for event in pygame.event.get():
                if event.type == pygame.FINGERDOWN:
                    self.fingers += 1
                    self.holdtime = time.time()
                    self.holdpos = pygame.mouse.get_pos()
                if event.type == pygame.FINGERUP:
                    if time.time() - self.holdtime < 1 and pygame.mouse.get_pos() == self.holdpos:
                        gesture.run(f"tap{self.fingers}")
                    if self.holding:
                        self.holding = False
                        gesture.run("release")
                    self.holdtime = 0
                    self.holdpos = 0
                    self.fingers = 0
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

            if self.holdtime != 0 and time.time()-self.holdtime > 1 and mouse_pos == self.holdpos:
                gesture.run("hold")
                self.holding = True
                self.holdtime = 0

            fps_text = self.font.render("FPS: {}".format(int(self.clock.get_fps())), True, (180,180,180))
            self.screen.blit(fps_text, (10, 10))

            self.logtext = str(self.fingers)
            log_text = self.font.render(self.logtext, True, (255,255,255))
            self.screen.blit(log_text, (10, self.size[1]-30))

            if mouse_pos[0] < 10 and mouse_pos[1] < 10 and platform.system() == "Linux":
                self.alive = False

            pygame.display.update()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()


    def log(self, text):
        text = str(text)
        with open("log.txt", "a") as f:
            f.write(text+"\n")

Application()
