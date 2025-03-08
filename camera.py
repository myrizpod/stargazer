
import pygame
import pygame.camera
import constants as ct
import maths as t

class Camera:
    def __init__(self):
        self.pitch = 0
        self.yaw = 0
    
    def update(self):
        if pygame.mouse.get_pressed()[1]:
            self.inputs()
        print(self.pitch,self.yaw)
        
    def inputs(self):
        rel = pygame.mouse.get_rel()
        self.pitch+= rel[0]
        self.yaw+= rel[1]

    