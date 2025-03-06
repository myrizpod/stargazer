"""The game's main file"""
#Library import

#C:\Users\Admin\AppData\Roaming\Python\Python313\Scripts\pyinstaller.exe --onefile -w main.py to get .exe

import pygame

import constants as ct
from game import Game
import background as bg


class App:

    def __init__(self):
        """
        Called on game startup, all basic stuff
        """

        #Creating basics of the game
        #self.screen_mult = 6
        self.screen_mult = 6
        ct.SCREEN_MULT = self.screen_mult
        self.screen_size = (ct.GAME_DRAW_SIZE_X * self.screen_mult, ct.GAME_DRAW_SIZE_Y * self.screen_mult)
        pygame.init()
        self.running = True
        ct.RENDER_BUFFER = pygame.Surface((ct.GAME_DRAW_SIZE_X, ct.GAME_DRAW_SIZE_Y), pygame.OPENGL)
        ct.CLOCK = pygame.time.Clock()
        self.screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption('Stargazer')

        pygame.mixer.init()

        self.game = Game()

        #Starting game loop
        self.loop()
        pygame.quit()

    def loop(self):
        """
        Global game loop
        """
        while self.running:
            ct.CLOCK.tick(30)

            self.update()
            self.draw()

        pygame.quit()


    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
            if event.type == pygame.QUIT:
                self.running = False
                return

        self.game.update()
            

    def draw(self):
        """called anytime the game will try to refresh screen
        """
        pygame.draw.rect(ct.RENDER_BUFFER,(14,4,33),pygame.Rect(0,0,320,180))
        bg.draw_background(0,0)
        self.game.draw()
        pygame.transform.scale_by(ct.RENDER_BUFFER, self.screen_mult, self.screen)
        pygame.display.update()



if __name__ == '__main__':
    App()
