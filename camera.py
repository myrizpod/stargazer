
import pygame
import pygame.camera
import constants as ct
import maths as t

class Camera:
    def __init__(self):
        self.pitch = 0
        self.yaw = 0
    
    def update(self):
        if pygame.mouse.get_pressed()[2] and not pygame.mouse.get_just_pressed()[2]:
            self.inputs()
        self.pitch %= 1000
        self.yaw = min(max(self.yaw,0),180)
        
    def inputs(self):
        rel = pygame.mouse.get_rel()
        if t.dist(0,0,rel[0],rel[1])>500:
            return
        print(rel)
        self.pitch-= rel[0]/10
        self.yaw-= rel[1]/10

    