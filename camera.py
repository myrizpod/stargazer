
import pygame
import constants as ct
import tools as t


class Camera:
    def __init__(self):
        self.pitch = 0
        self.yaw = 0
    
    def update(self,target):
        self.inputs()
        
    def inputs(self):
        keys = pygame.key.get_pressed()
        v = [0,0]
        if keys[pygame.K_UP]:
            v[1]-=1
        if keys[pygame.K_LEFT]:
            v[0]-=1
        if keys[pygame.K_DOWN]:
            v[1]+=1
        if keys[pygame.K_RIGHT]:
            v[0]+=1
        v = t.normalize(v,self.speed)
        self.pitch+=v[0]
        self.yaw+=v[1]

    