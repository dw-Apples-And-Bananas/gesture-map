import time
import pygame


class Mouse():
    def __init__(self):
        self.downTime = 0
        self.upTime = 0
        self.down = False
        self.up = False

    def tapped(self):
        tapped = self.tap
        if tapped: self.tap = False
        return tapped


    def update(self, event):
        self.tap = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.downTime = time.time()
            self.down, self.up = True, False
        elif event.type == pygame.MOUSEBUTTONUP:
            if time.time() - self.downTime < 0.5:
                self.tap = True
            self.downTime = 0
            self.down, self.up = False, True


