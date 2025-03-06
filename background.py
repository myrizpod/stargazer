import pygame
import constants as ct
import math

def draw_background(pitch,yaw):
        for x in range(0,320):
            for y in range(0,180):
                p =(math.sin(x/10)*math.cos(y/10)+1)/2
                if p<0.2:
                    ct.RENDER_BUFFER.set_at((x,y),ct.BG_DARK_PURPLE)
                elif p<0.4:
                    if (x+y)%2==0:
                        ct.RENDER_BUFFER.set_at((x,y),ct.BG_BLACK)
                    else:
                        ct.RENDER_BUFFER.set_at((x,y),ct.BG_DARK_PURPLE)
                elif p<0.6:
                    ct.RENDER_BUFFER.set_at((x,y),ct.BG_BLACK)
                elif p<0.8:
                    if (x+y)%2==0:
                        ct.RENDER_BUFFER.set_at((x,y),ct.BG_BLACK)
                    else:
                        ct.RENDER_BUFFER.set_at((x,y),ct.BG_DARK_BLUE)
                else:
                    ct.RENDER_BUFFER.set_at((x,y),ct.BG_DARK_BLUE)
    
    