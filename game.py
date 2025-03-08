import camera as cam
from levels_manager.level import Level
from levels_manager.star import Star
from menu import get_main_menu

#States
MAIN_MENU = "mainmenu"
MAP = "mapmenu"
IN_LEVEL = "inlevel"


class Game:
    def __init__(self):
        self.camera = cam.Camera()

        stars = [Star(0, (100,100)),
                 Star(0, (150, 150)),
                 Star(0, (170, 80))
                 ]
        self.actual_level = Level(stars)
        self.actual_menu = get_main_menu()
        self.state = MAP


    def draw(self):
        if self.state == MAIN_MENU:
            self.actual_menu.draw()
        elif self.state == IN_LEVEL:
            self.actual_level.draw()
    
    def update(self):
        if self.state == IN_LEVEL:
            self.actual_level.update()
        elif self.state == MAP:
            self.camera.update()
        pass