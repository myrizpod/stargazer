from levels_manager.level import Level
import pygame
import constants as ct
import random as r

class MapLevel:
    def __init__(self):
        self.all_levels = {}
        self.all_images = []
        self.bg_elts = []
        for i in range(0,1536,64):
            self.bg_elts.append(r.randint(0,1))
        self.load_img()
            
    def load_img(self):
        self.bg_images = [pygame.image.load("resources/images/background_"+str(i+1)+".png") for i in range(2)]
        self.selected_stars = pygame.image.load("resources/images/star_large.png")
        self.unselected_stars = pygame.image.load("resources/images/star_mid.png")
            

    def add(self, x, y, level: Level):
        self.all_levels[level] = [(x, y)]


    def draw(self, pitch, yaw):
        new_level = None
        for level, value in self.all_levels.items():
            for star in level.stars:
                ct.RENDER_BUFFER.blit(self.unselected_stars,
                        [(star.coordonates[0]/5 - pitch + value[0][0])%ct.MAP_SIZE - 1, star.coordonates[1]/5 - yaw + value[0][1] - 1])

            mouse_coo = [pygame.mouse.get_pos()[0] / ct.SCREEN_MULT, pygame.mouse.get_pos()[1] / ct.SCREEN_MULT]
            if value[0][0] < (mouse_coo[0] + pitch)%ct.MAP_SIZE < value[0][0] + 50 and value[0][1] < mouse_coo[1] + yaw < value[0][1] + 50:
                for star in level.stars:
                    ct.RENDER_BUFFER.blit(self.selected_stars,
                        [(star.coordonates[0]/5 - pitch + value[0][0])%ct.MAP_SIZE - 3, star.coordonates[1]/5 - yaw + value[0][1] - 3])
                if pygame.mouse.get_pressed()[0]:
                    new_level = level
                    
        pygame.draw.rect(ct.RENDER_BUFFER,(14,15,44),(0,430-yaw*1.5,320,20))
        for i in range(len(self.bg_elts)):
            ct.RENDER_BUFFER.blit(self.bg_images[self.bg_elts[i]],((i*64 - pitch*1.5)%ct.MAP_SIZE-64,400 - yaw*1.5))
            
        
        
        return new_level




