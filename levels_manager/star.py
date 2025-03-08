import pygame
import constants as ct

class Star:
    def __init__(self, sound: int, coo: tuple[int, int]):
        self.sound = sound
        self.coordonates = coo

    def draw(self):
        pygame.draw.circle(ct.RENDER_BUFFER, ct.WHITE, self.coordonates, 5)
