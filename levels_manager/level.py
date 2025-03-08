from math import sqrt

from levels_manager.star import Star
from levels_manager.link import Link
from levels_manager.link_types import SIMPLE
import lines as l
import pygame
import constants as ct
import tools as t

class Level:
    def __init__(self, all_stars: list[Star]):
        self.links = []
        self.stars = all_stars

        self.link_end = [0,0]
        self.link_start = [0,0]
        self.activelink = [None,None]

    def get_stars(self):
        return self.stars
    def get_links(self):
        return self.links

    def draw(self):
        for star in self.stars:
            star.draw()
        for link in self.links:
            link.draw()

        #l.addmarker(self.link_start, self.link_end, ct.WHITE, l.basic)
        if pygame.mouse.get_pressed()[0]:
            l.addmarker(self.link_start, self.link_end, ct.WHITE, l.addbroken,3,l.dash) 

    def update(self):
        if pygame.mouse.get_just_pressed()[0]:
            self.link_start = [pygame.mouse.get_pos()[0]/ct.SCREEN_MULT,pygame.mouse.get_pos()[1]/ct.SCREEN_MULT]
            self.find_start_star()
        if pygame.mouse.get_pressed()[0]:
            self.link_end = [pygame.mouse.get_pos()[0]/ct.SCREEN_MULT,pygame.mouse.get_pos()[1]/ct.SCREEN_MULT]
            self.find_end_star()
        elif self.activelink[0]!=None and self.activelink[1]!=None and self.activelink[0]!=self.activelink[1]:
            skip  = False
            for link in self.links:
                if link.start in self.activelink and link.end in self.activelink:
                    skip = True
            if not skip:
                self.links.append(Link(self.activelink[0], self.activelink[1], SIMPLE))
                self.activelink = [None,None]
            
    def find_start_star(self):
        for star in self.stars:
            if t.dist(star.coordonates[0],star.coordonates[1],self.link_start[0],self.link_start[1])<10:
                self.activelink[0] = star
                self.link_start = [star.coordonates[0],star.coordonates[1]]
                return
        self.activelink[0] = None
                
    def find_end_star(self):
        for star in self.stars:
            if t.dist(star.coordonates[0],star.coordonates[1],self.link_end[0],self.link_end[1])<10:
                self.activelink[1] = star
                self.link_end = [star.coordonates[0],star.coordonates[1]]
                return
        self.activelink[1] = None
