import camera as cam
from map_level import MapLevel
from menu import get_main_menu
import background as bg
from constants import AllLevels

#States
MAIN_MENU = "mainmenu"
MAP = "mapmenu"
IN_LEVEL = "inlevel"

class Game:
    def __init__(self):
        self.camera = cam.Camera()
        self.background = bg.Background()

        self.actual_level = AllLevels.ALL_LEVELS[0][0]
        self.actual_menu = get_main_menu()
        self.state = MAP
        self.map = MapLevel()

        for level in AllLevels.ALL_LEVELS:
            self.map.add(level[1][0], level[1][1], level[0])

    def draw(self):
        if self.state == MAIN_MENU:
            self.actual_menu.draw()
        elif self.state == IN_LEVEL:
            self.background.draw_background(0,0)
            self.actual_level.draw()
        elif self.state == MAP:
            self.background.draw_background(self.camera.pitch,self.camera.yaw)
            level = self.map.draw(self.camera.pitch, self.camera.yaw)
            if level is not None:
                self.actual_level = level
                self.state = IN_LEVEL
                self.actual_level.reset_mouse()


    def update(self):
        if self.state == IN_LEVEL:
            return_to_map = self.actual_level.update()
            if return_to_map:
                self.state = MAP
        elif self.state == MAP:
            self.camera.update()