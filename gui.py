import pygame
import constants as ct
import sound_height as sh
import levels_manager.link_types as lt

class LevelGui:
    def __init__(self,melody):
        self.melody = melody
        self.img = pygame.image.load("resources/level_gui.png")
        
    def draw(self):
        ct.RENDER_BUFFER.blit(self.img,(0,150))
        self.render_partition()
        
        
    def render_partition(self):
        pygame.draw.rect(ct.RENDER_BUFFER,(207,150,140),(193,154,self.melody.duration*8,25))
        for y in range(5):
            pygame.draw.line(ct.RENDER_BUFFER,(143,87,101),(194,156+y*4),(191+self.melody.duration*8,156+y*4))
        for t in self.melody.notes.keys():
            for note in self.melody.notes[t].split(","):
                pygame.draw.rect(ct.RENDER_BUFFER,(143,87,101),(195+t*8,173-sh.HEIGHT[note]*2,3,3))
                
    def gui_click_input(self):
        rect_width = 18
        mouse_pos = (pygame.mouse.get_pos()[0]/ct.SCREEN_MULT,pygame.mouse.get_pos()[1]/ct.SCREEN_MULT)
        if 154>mouse_pos[1]:
            return None
        elif 15<mouse_pos[0]<15+rect_width:
            return lt.QUARTER
        elif 33<mouse_pos[0]<33+rect_width:
            return lt.DEMI
        elif 51<mouse_pos[0]<51+rect_width:
            return lt.SIMPLE
        elif 69<mouse_pos[0]<69+rect_width:
            return lt.DOUBLE
        elif 87<mouse_pos[0]<87+rect_width:
            return lt.TRIPLE
        
        elif 108<mouse_pos[0]<108+rect_width:
            return "no_attribute"
        elif 125<mouse_pos[0]<125+rect_width:
            return lt.ADDITIONAL_BROKEN_1
        elif 142<mouse_pos[0]<142+rect_width:
            return lt.ADDITIONAL_BROKEN_2
        elif 159<mouse_pos[0]<159+rect_width:
            return lt.ADDITIONAL_BROKEN_3