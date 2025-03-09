import pygame
import constants as ct
import sounds as s

class Star:
    def __init__(self, sound: int, coo: tuple[int, int]):
        print(sound)
        self.sound = s.SOUNDS[sound]
        self.coordonates = coo

    def draw(self):
        pygame.draw.circle(ct.RENDER_BUFFER, ct.WHITE, self.coordonates, 5)
        
    def play(self):
        self.sound.play()
