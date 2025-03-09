from levels_manager.level import Level
import pygame
import constants as ct

class MapLevel:
    def __init__(self):
        self.all_levels = {}

    def add(self, x, y, level: Level):
        self.all_levels[level] = (x, y)

    def draw(self, pitch, yaw):
        new_level = None
        for level, coo in self.all_levels.items():
            for star in level.stars:
                pygame.draw.circle(ct.RENDER_BUFFER, ct.WHITE, [(star.coordonates[0]/5 - pitch + coo[0])%ct.MAP_SIZE, star.coordonates[1]/5 - yaw + coo[1]], 3)

            mouse_coo = [pygame.mouse.get_pos()[0] / ct.SCREEN_MULT, pygame.mouse.get_pos()[1] / ct.SCREEN_MULT]
            if coo[0] < (mouse_coo[0] + pitch)%ct.MAP_SIZE < coo[0] + 100 and coo[1] < mouse_coo[1] + yaw < coo[1] + 100:
                pygame.draw.rect(ct.RENDER_BUFFER, ct.WHITE, ((coo[0]-pitch)%ct.MAP_SIZE, coo[1]-yaw, 100, 100), 1, 1)
                if pygame.mouse.get_pressed()[0]:
                    new_level = level
        return new_level




