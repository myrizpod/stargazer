import pygame
import camera as cam
from levels_manager.level import Level
from levels_manager.star import Star

#States
MAIN_MENU = "mainmenu"
MAP = "mapmenu"
IN_LEVEL = "inlevel"


class Game:
    def __init__(self):
        self.camera = cam.Camera()

        stars = [Star(0, (100,100)),
                 Star(0, (150, 150)),
                 Star(0, (170, 80))
                 ]
        self.actual_level = Level(stars)
        self.state = IN_LEVEL


    def draw(self):
        if self.state == MAP:
            self.camera.update()

        if self.state == IN_LEVEL:
            self.actual_level.draw()
        pass
    
    def update(self):
        #self.camera.update(self.player)

        if self.state == IN_LEVEL:
            self.actual_level.update()
        pass