from math import sqrt

from levels_manager.star import Star
from levels_manager.link import Link
from levels_manager.link_types import SIMPLE
import lines as l
import pygame
import constants as ct

class Level:
    def __init__(self, all_stars: list[Star]):
        self.links = []
        self.stars = all_stars

        self.link_end = [0,0]
        self.link_start = [0,0]

    def get_stars(self):
        return self.stars
    def get_links(self):
        return self.links

    def draw(self):
        for star in self.stars:
            star.draw()
        for link in self.links:
            link.draw()

        l.addmarker(self.link_start, self.link_end, (199,212,225), l.basic)

    def update(self):
        if pygame.mouse.get_just_pressed()[0]:
            self.link_start = [pygame.mouse.get_pos()[0]/ct.SCREEN_MULT,pygame.mouse.get_pos()[1]/ct.SCREEN_MULT]
        if pygame.mouse.get_pressed()[0]:
            self.link_end = [pygame.mouse.get_pos()[0]/ct.SCREEN_MULT,pygame.mouse.get_pos()[1]/ct.SCREEN_MULT]

        first_star = None
        last_star = None
        for star in self.stars:
            if star.is_linked:
                continue
            distance_to_first_star = sqrt(
                (star.coordonates[0]-self.link_start[0])**2 + (star.coordonates[1]-self.link_start[1])**2)
            distance_to_last_star = sqrt(
                (star.coordonates[0] - self.link_end[0]) ** 2 + (star.coordonates[1] - self.link_end[1]) ** 2)
            if distance_to_first_star < 10:
                first_star = star
            if distance_to_last_star < 10:
                last_star = star

        if first_star is not None and last_star is not None:
            print("liiiiiink")
            self.links.append(Link(first_star, last_star, SIMPLE))
