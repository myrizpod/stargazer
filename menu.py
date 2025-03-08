import pygame
import pygame.freetype
import constants as ct

class Menu:
    def __init__(self):
        self.objects = []

    def add_object(self, obj):
        self.objects.append(obj)

    def draw(self):
        for obj in self.objects:
            obj.draw()


class Button:
    def __init__(self, coo: list[int], text: str, action):
        self.x = coo[0]
        self.y = coo[1]
        self.text = text
        self.action = action

    def draw(self):
        font = pygame.freetype.SysFont('Comic Sans MS', 30)
        box = pygame.Rect(self.x, self.y, len(self.text)*font.size, font.size)
        pygame.draw.rect(ct.RENDER_BUFFER, ct.WHITE, box, 1, 1)
        font.render_to(ct.RENDER_BUFFER, box, self.text)


class Text:
    def __init__(self, coo: list[int], text: str):
        self.x = coo[0]
        self.y = coo[1]
        self.text = text

    def draw(self):
        font = pygame.freetype.SysFont('Comic Sans MS', 30)
        box = pygame.Rect(self.x, self.y, len(self.text)*font.size, font.size)
        font.render_to(ct.RENDER_BUFFER, box, self.text)


def pass_func():
    pass

def get_main_menu():
    menu = Menu()
    title = Text([ct.GAME_DRAW_SIZE_X/50*ct.SCREEN_MULT, ct.GAME_DRAW_SIZE_Y/90*ct.SCREEN_MULT],  "★ Star Gazer ★")
    button_play = Button([ct.GAME_DRAW_SIZE_X/50*ct.SCREEN_MULT, ct.GAME_DRAW_SIZE_Y/70*ct.SCREEN_MULT], "PLAY", pass_func) #in the future: game.change_state(MAP)
    button_settings = Button([ct.GAME_DRAW_SIZE_X/50*ct.SCREEN_MULT, ct.GAME_DRAW_SIZE_Y/60*ct.SCREEN_MULT], "Settings", pass_func) #in the future: game.change_state(SETTINGS)

    menu.add_object(title)
    menu.add_object(button_play)
    menu.add_object(button_settings)

    return menu

