
import pygame
import camera as cam

class Game:
    def __init__(self):
        self.camera = cam.Camera()
    
    def draw(self):
        pass
    
    def update(self):
        self.camera.update(self.player)