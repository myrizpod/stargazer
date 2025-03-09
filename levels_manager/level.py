from levels_manager.star import Star
from levels_manager.link import Link
from levels_manager.link_types import *
import pygame
import constants as ct
import maths as t
import gui

class Level:
    def __init__(self, all_stars: list[Star], level_melody):
        self.links = []
        self.stars = all_stars
        
        self.melody = level_melody
        self.gui = gui.LevelGui(self.melody)

        self.link_end = [0,0]
        self.link_start = [0,0]
        self.active_link = [None, None]
        self.actual_link_type = SIMPLE
        self.additional_link_type = None
        self.start_star = None

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
            Link(self.link_start, self.link_end, self.actual_link_type, self.additional_link_type).draw()
            #l.addmarker(self.link_start, self.link_end, ct.WHITE, l.addbroken,3,l.dash)
            #better_link_start,better_link_end = l.link_displace(self.link_start, self.link_end)
            #l.addmarker(better_link_start if self.activelink[0]!=None else self.link_start , better_link_end if self.activelink[1]!=None else self.link_end , ct.WHITE, l.addbroken,3,l.dash)
            
        self.gui.draw()

    def update(self):
        if pygame.mouse.get_just_pressed()[0]:
            gui_click_result = self.gui.gui_click_input()
            if gui_click_result in (SIMPLE,DOUBLE,DEMI,TRIPLE,QUARTER):
                self.actual_link_type = gui_click_result
            elif gui_click_result == "no_attribute":
                self.additional_link_type = None
            elif gui_click_result in (ADDITIONAL_BROKEN_1,ADDITIONAL_BROKEN_2,ADDITIONAL_BROKEN_3):
                self.additional_link_type = gui_click_result
            self.link_start = [pygame.mouse.get_pos()[0]/ct.SCREEN_MULT,pygame.mouse.get_pos()[1]/ct.SCREEN_MULT]
            click_star = self.find_star(self.link_start[0],self.link_start[1])
            if click_star!= None:
                click_star.play()
            self.find_start_star()
        if pygame.mouse.get_pressed()[0]:
            self.link_end = [pygame.mouse.get_pos()[0]/ct.SCREEN_MULT,pygame.mouse.get_pos()[1]/ct.SCREEN_MULT]
            self.find_end_star()

        elif self.active_link[0] is not None and \
                self.active_link[1] is not None and self.active_link[0]!=self.active_link[1]:
            skip  = False
            for link in self.links:
                if link.start in self.active_link and link.end in self.active_link:
                    skip = True
            if not skip:
                self.links.append(Link(self.active_link[0].coordonates, self.active_link[1].coordonates, self.actual_link_type, self.additional_link_type))
                self.active_link = [None, None]
                
        self.melody.playing_loop()
        #self.constellation_reading_loop()
        if pygame.mouse.get_just_pressed()[2]:
            #click_star = self.find_star([pygame.mouse.get_pos()[0]/ct.SCREEN_MULT,pygame.mouse.get_pos()[1]/ct.SCREEN_MULT])
            #self.melody.play()
            self.read_constellation()
    
    
    
    
    def find_start_star(self):
        clicked_star = self.find_star(self.link_start[0],self.link_start[1])
        if clicked_star != None:
                self.active_link[0] = clicked_star
                self.link_start = [clicked_star.coordonates[0],clicked_star.coordonates[1]]
        else:
            self.active_link[0] = None
                
    def find_end_star(self):
        clicked_star = self.find_star(self.link_end[0],self.link_end[1])
        if clicked_star != None:
                self.active_link[1] = clicked_star
                self.link_end = [clicked_star.coordonates[0],clicked_star.coordonates[1]]
        else:
            self.active_link[1] = None
        
    def find_star(self,x,y):
        for star in self.stars:
            if t.dist(star.coordonates[0],star.coordonates[1],x,y)<10:
                return star
        return None
    
    
    def read_constellation(self):
        self.start_time = pygame.time.get_ticks()
        self.pointers = [[]]
        
    def constellation_reading_loop(self):
        if self.pointer<self.duration:
            previous_pointer = self.pointer
            self.pointer = (pygame.time.get_ticks() - self.start_time)/1000
            for t in self.notes.keys():
                if previous_pointer <= t <= self.pointer:
                    for note in self.notes[t].split(","):
                        s.SOUNDS[note].play()
