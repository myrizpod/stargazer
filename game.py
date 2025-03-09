import camera as cam
from levels_manager.level import Level
from levels_manager.star import Star
from menu import get_main_menu
import readers as r
import melodies as m
import background as bg

#States
MAIN_MENU = "mainmenu"
MAP = "mapmenu"
IN_LEVEL = "inlevel"




class Game:
    def __init__(self):
        
        LEVEL1 = Level(r.read_level("resources/levels/tutorial.txt"),m.Melody(r.read_melody("resources/melodies/tutorial.txt")))
        
        self.camera = cam.Camera()
        self.background = bg.Background()

        self.actual_level = LEVEL1
        self.actual_menu = get_main_menu()
        self.state = IN_LEVEL


    def draw(self):
        if self.state == MAIN_MENU:
            self.actual_menu.draw()
        elif self.state == IN_LEVEL:
            self.background.draw_background(0,0)
            self.actual_level.draw()
        else:
            self.background.draw_background(self.camera.pitch,self.camera.yaw)
    
    def update(self):
        if self.state == IN_LEVEL:
            self.actual_level.update()
        elif self.state == MAP:
            self.camera.update()