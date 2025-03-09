import pygame
import constants as ct
from sound_manager import sounds as s

import random as r

class Star:
    def __init__(self, sound: int, coo: tuple[int, int]):
        print(sound)
        self.sound = s.SOUNDS[sound]
        self.coordonates = coo
        chosen_star = r.choice((["resources/images/star_large.png",6],["resources/images/star_mid.png",4]))
        self.img = pygame.image.load(chosen_star[0])
        self.img_offset = chosen_star[1]

    def draw(self):
        ct.RENDER_BUFFER.blit(self.img,(self.coordonates[0]-self.img_offset,self.coordonates[1]-self.img_offset))
        
    def play(self):
        self.sound.play()
