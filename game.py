
import pygame
import camera as cam
from levels_manager.level import Level
from levels_manager.star import Star


class Game:
    def __init__(self):
        self.camera = cam.Camera()
    
    def draw(self):
        stars = [Star(0, (100,100))
                 ]
        default_level = Level(stars)

        default_level.draw()
        pass
    
    def update(self):
        #self.camera.update(self.player)
        pass