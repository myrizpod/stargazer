import pygame
import constants as ct
import math
    
class Background:
    def __init__(self):
        background_img = pygame.image.load("resources/images/background_noise.png").convert_alpha()
        noise_img = pygame.image.load("resources/images/white_noise.png").convert_alpha()
        self.PERLIN_NOISE_BUFFER = pygame.Surface((1024, 1024), pygame.OPENGL)
        self.PERLIN_NOISE_BUFFER.blit(background_img)
        
        self.WHITE_NOISE_BUFFER = pygame.Surface((1024, 1024), pygame.OPENGL)
        self.WHITE_NOISE_BUFFER.blit(noise_img)
        
        self.noise_value_list = [[(self.PERLIN_NOISE_BUFFER.get_at((x,y))[0],self.PERLIN_NOISE_BUFFER.get_at((x,y))[1],self.PERLIN_NOISE_BUFFER.get_at((x,y))[2],self.WHITE_NOISE_BUFFER.get_at((x,y))[0]) for x in range(1024)] for y in range(1024)]


    def draw_background(self,pitch,yaw):
        for x in range(0,320):
            for y in range(0,180):
                frame_time = int(pygame.time.get_ticks()/100)
                p =self.noise_value_list[int(x+pitch*0.6)%615][int(y+yaw*0.6)%615][0]/255 + self.noise_value_list[int(x+pitch*0.6+frame_time)%615][int(y+yaw*0.6+frame_time)%615][1]/255
                
                n = self.noise_value_list[int(x+pitch*0.25)%256][int(y+yaw*0.25)%256][3]
                #if n>0:
                    #ct.RENDER_BUFFER.set_at((x,y),ct.GRAYS[n%3])
                    
                if p<0.15:
                    if n>0:
                        ct.RENDER_BUFFER.set_at((x,y),ct.BG_LIGHT_PURPLE[n%3])
                    else:
                        ct.RENDER_BUFFER.set_at((x,y),ct.BG_DARK_PURPLE)
                elif p<0.3:
                    if (x+y)%2==0:
                        if n>0:
                            ct.RENDER_BUFFER.set_at((x,y),ct.GRAYS[n%3])
                        else:
                            ct.RENDER_BUFFER.set_at((x,y),ct.BG_BLACK)
                    else:
                        if n>0:
                            ct.RENDER_BUFFER.set_at((x,y),ct.BG_LIGHT_PURPLE[n%3])
                        else:
                            ct.RENDER_BUFFER.set_at((x,y),ct.BG_DARK_PURPLE)
                elif p<0.7:
                    if n>0:
                        ct.RENDER_BUFFER.set_at((x,y),ct.GRAYS[n%3])
                    else:
                        ct.RENDER_BUFFER.set_at((x,y),ct.BG_BLACK)
                elif p<0.85:
                    if (x+y)%2==0:
                        if n>0:
                            ct.RENDER_BUFFER.set_at((x,y),ct.GRAYS[n%3])
                        else:
                            ct.RENDER_BUFFER.set_at((x,y),ct.BG_BLACK)
                    else:
                        if n>0:
                            ct.RENDER_BUFFER.set_at((x,y),ct.BG_LIGHT_BLUE[n%3])
                        else:
                            ct.RENDER_BUFFER.set_at((x,y),ct.BG_DARK_BLUE)
                        
                else:
                    if n>0:
                        ct.RENDER_BUFFER.set_at((x,y),ct.BG_LIGHT_BLUE[n%3])
                    else:
                        ct.RENDER_BUFFER.set_at((x,y),ct.BG_DARK_BLUE)

    