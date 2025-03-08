import pygame
import constants as ct
import math
    
class Background:
    def __init__(self):
        background_img = pygame.image.load("resources/background_noise.png").convert_alpha()
        self.NOISE_BUFFER = pygame.Surface((1024, 1024), pygame.OPENGL)
        self.NOISE_BUFFER.blit(background_img)
        self.noise_value_list = [[(self.NOISE_BUFFER.get_at((x,y))[1],self.NOISE_BUFFER.get_at((x,y))[2]) for x in range(1024)] for y in range(1024)]
            

    def draw_background(self,pitch,yaw):
        for x in range(0,320):
            for y in range(0,180):
                frame_time = pygame.time.get_ticks()/100
                p =self.noise_value_list[int(x+pitch)%1024][int(y+yaw)%1024][0]/255 + self.noise_value_list[int(x+pitch+frame_time)%1024][int(y+yaw+frame_time)%1024][1]/255
                if p<0.15:
                    ct.RENDER_BUFFER.set_at((x,y),ct.BG_DARK_PURPLE)
                elif p<0.3:
                    if (x+y)%2==0:
                        ct.RENDER_BUFFER.set_at((x,y),ct.BG_BLACK)
                    else:
                        ct.RENDER_BUFFER.set_at((x,y),ct.BG_DARK_PURPLE)
                elif p<0.7:
                    ct.RENDER_BUFFER.set_at((x,y),ct.BG_BLACK)
                elif p<0.85:
                    if (x+y)%2==0:
                        ct.RENDER_BUFFER.set_at((x,y),ct.BG_BLACK)
                    else:
                        ct.RENDER_BUFFER.set_at((x,y),ct.BG_DARK_BLUE)
                else:
                    ct.RENDER_BUFFER.set_at((x,y),ct.BG_DARK_BLUE)

    