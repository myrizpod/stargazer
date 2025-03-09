import pygame
import constants as ct
from sound_manager import sound_height as sh
import levels_manager.link_types as lt

class LevelGui:
    def __init__(self,melody):
        self.melody = melody
        self.img_gui = pygame.image.load("resources/images/level_gui.png")
        self.img_return_button = pygame.image.load("resources/images/back_arrow.png")
        self.img_restart_button = pygame.image.load("resources/images/restart_arrow.png")
        self.imgs_melody = {}
        for e in ("a","b","c","d","e","f","g"):
            self.imgs_melody[e.upper()] = pygame.image.load("resources/images/note_"+ e +".png")

    def draw(self):
        ct.RENDER_BUFFER.blit(self.img_gui, (0, 150))
        ct.RENDER_BUFFER.blit(self.img_return_button, (5, 5))
        ct.RENDER_BUFFER.blit(self.img_restart_button, (ct.GAME_DRAW_SIZE_X-32, 0))
        self.render_partition()
        self.over_note()
        
    def render_partition(self):
        pygame.draw.rect(ct.RENDER_BUFFER,(207,150,140),(193,154,self.melody.duration*8,25))
        for y in range(5):
            pygame.draw.line(ct.RENDER_BUFFER,(143,87,101),(194,156+y*4),(191+self.melody.duration*8,156+y*4))
        for t in self.melody.notes.keys():
            for note in self.melody.notes[t].split(","):
                pygame.draw.rect(ct.RENDER_BUFFER,(143,87,101),(195+t*8,173-sh.HEIGHT[note]*2,3,3))

    def over_note(self):
        mouse_pos = (pygame.mouse.get_pos()[0] / ct.SCREEN_MULT, pygame.mouse.get_pos()[1] / ct.SCREEN_MULT)
        if mouse_pos[0] > 195 and mouse_pos[1] > 154:
            for t in self.melody.notes.keys():
                for note in self.melody.notes[t].split(","):
                    x = 195 + t * 8
                    y = 173 - sh.HEIGHT[note] * 2
                    if x < mouse_pos[0] < x + 3 and y <mouse_pos[1] < y + 3:
                        pygame.draw.rect(ct.RENDER_BUFFER, ct.WHITE, (x-2, y-7, 6, 6))
                        ct.RENDER_BUFFER.blit(self.imgs_melody[note.replace("#","")[:-1]], (x-2, y-7))

    def gui_click_input(self):
        rect_width = 18
        mouse_pos = (pygame.mouse.get_pos()[0] / ct.SCREEN_MULT, pygame.mouse.get_pos()[1] / ct.SCREEN_MULT)

        if 0 < mouse_pos[1] < 20 and 0 < mouse_pos[0] < 30:
            return "return_to_map"
        if 0 < mouse_pos[1] < 32 and ct.GAME_DRAW_SIZE_X-32 < mouse_pos[0] < ct.GAME_DRAW_SIZE_X:
            return "reset"

        if 154 > mouse_pos[1]:
            return None
        elif 15 < mouse_pos[0] < 15 + rect_width:
            return lt.QUARTER
        elif 33 < mouse_pos[0] < 33 + rect_width:
            return lt.DEMI
        elif 51 < mouse_pos[0] < 51 + rect_width:
            return lt.SIMPLE
        elif 69 < mouse_pos[0] < 69 + rect_width:
            return lt.DOUBLE
        elif 87 < mouse_pos[0] < 87 + rect_width:
            return lt.TRIPLE

        elif 108 < mouse_pos[0] < 108 + rect_width:
            return "no_attribute"
        elif 125 < mouse_pos[0] < 125 + rect_width:
            return lt.ADDITIONAL_BROKEN_1
        elif 142 < mouse_pos[0] < 142 + rect_width:
            return lt.ADDITIONAL_BROKEN_2
        elif 159 < mouse_pos[0] < 159 + rect_width:
            return lt.ADDITIONAL_BROKEN_3
