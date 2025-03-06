import pygame
import camera as cam
from levels_manager.level import Level
from levels_manager.star import Star

class Game:
    def __init__(self):
        self.camera = cam.Camera()

        stars = [Star(0, (100,100)),
                 Star(0, (150, 150))
                 ]
        self.actual_level = Level(stars)


    
    def draw(self):
        self.actual_level.draw()
        pass
    
    def update(self):
        #self.camera.update(self.player)
        self.actual_level.update()
        pass