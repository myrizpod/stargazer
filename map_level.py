from levels_manager.level import Level
import pygame
import constants as ct
import random as r

class MapLevel:
    def __init__(self):
        self.all_levels = {}
        self.all_images = []
        for i in range(3):
            self.all_images.append(pygame.image.load("resources/images/star_small_"+str(i+1)+".png"))

    def add(self, x, y, level: Level):
        img_per_star = {}
        for star in level.stars:
            img_per_star[star] = r.choice(self.all_images)
        self.all_levels[level] = [(x, y), img_per_star]


    def draw(self, pitch, yaw):
        new_level = None
        for level, value in self.all_levels.items():
            for star in level.stars:
                ct.RENDER_BUFFER.blit(value[1][star],
                        [(star.coordonates[0]/5 - pitch + value[0][0])%ct.MAP_SIZE, star.coordonates[1]/5 - yaw + value[0][1]])

            mouse_coo = [pygame.mouse.get_pos()[0] / ct.SCREEN_MULT, pygame.mouse.get_pos()[1] / ct.SCREEN_MULT]
            if value[0][0] < (mouse_coo[0] + pitch)%ct.MAP_SIZE < value[0][0] + 100 and value[0][1] < mouse_coo[1] + yaw < value[0][1] + 100:
                pygame.draw.rect(ct.RENDER_BUFFER, ct.WHITE, ((value[0][0]-pitch)%ct.MAP_SIZE, value[0][1]-yaw, 100, 100), 1, 1)
                if pygame.mouse.get_pressed()[0]:
                    new_level = level
        return new_level




