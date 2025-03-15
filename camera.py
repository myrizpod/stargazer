
import pygame
import pygame.camera
import constants as ct
import maths as t

class Camera:
    def __init__(self):
        self.pitch = 0
        self.yaw = 180
    
    def update(self):
        if pygame.mouse.get_pressed()[2]:
            self.inputs()
        else:
            pygame.mouse.get_rel()
        self.pitch %= ct.MAP_SIZE
        self.yaw = min(max(self.yaw,0),180)
        
    def inputs(self):
        rel = pygame.mouse.get_rel()
        print(rel)
        self.pitch-= rel[0]/10
        self.yaw-= rel[1]/10

    