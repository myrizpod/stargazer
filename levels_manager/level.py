from gui import LevelGui
from levels_manager.star import Star
from levels_manager.link import Link
from levels_manager.link_types import *
from levels_manager.level_checker import LevelChecker
import pygame
import constants as ct
import maths as t


class Level:
    def __init__(self, all_stars: list[Star], level_melody):
        self.links = []
        self.stars = all_stars
        
        self.melody = level_melody
        self.gui = LevelGui(level_melody)

        self.link_end = (0,0)
        self.link_start = (0,0)
        self.active_link = [None, None]
        self.actual_link_type = SIMPLE
        self.additional_link_type = None
        self.start_star = None
        self.last_selectioned_star = None
        self.level_checker = LevelChecker(level_melody)


        self.pointers = []

        self.start_time = None

    def get_stars(self):
        return self.stars
    def get_links(self):
        return self.links

    def draw(self):
        for star in self.stars:
            star.draw()
        for link in self.links:
            if not link.is_broken:
                link.draw()

        if pygame.mouse.get_pressed()[0]:
            Link(self.link_start, self.link_end, self.actual_link_type, self.additional_link_type).draw()

        self.level_checker.draw()
            
        self.gui.draw()
        self.hoover_note()
        
    def hoover_note(self):
        mouse_pos = (pygame.mouse.get_pos()[0] / ct.SCREEN_MULT, pygame.mouse.get_pos()[1] / ct.SCREEN_MULT)
        star = self.find_star(mouse_pos[0],mouse_pos[1])
        if star is not None:
            ct.RENDER_BUFFER.blit(self.gui.imgs_melody[star.sound_litteral.replace("#","")[:-1]], (star.coordonates[0]-2, star.coordonates[1]-7))

    def update(self):
        if pygame.mouse.get_just_pressed()[0]:
            gui_click_result = self.gui.gui_click_input()
            if gui_click_result in (SIMPLE,DOUBLE,DEMI,TRIPLE,QUARTER):
                self.actual_link_type = gui_click_result
            elif gui_click_result == "reset":
                self.links.clear()
                return False
            elif gui_click_result == "return_to_map":
                return True
            elif gui_click_result == "no_attribute":
                self.additional_link_type = None
            elif gui_click_result in (ADDITIONAL_BROKEN_1,ADDITIONAL_BROKEN_2,ADDITIONAL_BROKEN_3):
                self.additional_link_type = gui_click_result
            self.link_start = [pygame.mouse.get_pos()[0]/ct.SCREEN_MULT,pygame.mouse.get_pos()[1]/ct.SCREEN_MULT]
            click_star = self.find_star(self.link_start[0],self.link_start[1])
            if click_star is not None:
                click_star.play()
            self.find_start_star()
        if pygame.mouse.get_pressed()[0]:
            self.link_end = [pygame.mouse.get_pos()[0]/ct.SCREEN_MULT,pygame.mouse.get_pos()[1]/ct.SCREEN_MULT]
            self.find_end_star()

        elif self.active_link[0] is not None and \
                self.active_link[1] is not None and self.active_link[0]!=self.active_link[1]:
            skip  = False
            for link in self.links:
                if link.start_star in self.active_link and link.end_star in self.active_link:
                    skip = True
            if not skip:
                self.links.append(Link(self.active_link[0], self.active_link[1], self.actual_link_type, self.additional_link_type))
                self.active_link[1].play()
                self.active_link = [None, None]


        if pygame.mouse.get_just_pressed()[2]:
            self.level_checker.check(self.find_star(pygame.mouse.get_pos()[0] / ct.SCREEN_MULT,
                                    pygame.mouse.get_pos()[1] / ct.SCREEN_MULT), self.links)

        return self.level_checker.update()
    

    def find_start_star(self):
        clicked_star = self.find_star(self.link_start[0],self.link_start[1])
        if clicked_star is not None:
            self.active_link[0] = clicked_star
            self.link_start = [clicked_star.coordonates[0],clicked_star.coordonates[1]]
        else:
            self.active_link[0] = None
                
    def find_end_star(self):
        clicked_star = self.find_star(self.link_end[0],self.link_end[1])
        if clicked_star is not None:
            self.active_link[1] = clicked_star
            self.link_end = [clicked_star.coordonates[0],clicked_star.coordonates[1]]
        else:
            self.active_link[1] = None
        
    def find_star(self,x,y):
        for star in self.stars:
            if t.dist(star.coordonates[0],star.coordonates[1],x,y)<10:
                return star
        return None


    def reset_mouse(self):
        self.link_start = [pygame.mouse.get_pos()[0]/ct.SCREEN_MULT, pygame.mouse.get_pos()[1]/ct.SCREEN_MULT]