
import pygame
import sounds as s

class Melody:
    def __init__(self,notes):
        self.notes = notes
        self.pointer = 69
        self.duration = max(self.notes.keys())+1
        
    
    def play(self):
        self.start_time = pygame.time.get_ticks()
        self.pointer = 0
        
    def playing_loop(self):
        if self.pointer<self.duration:
            previous_pointer = self.pointer
            self.pointer = (pygame.time.get_ticks() - self.start_time)/1000
            for t in self.notes.keys():
                if previous_pointer <= t <= self.pointer:
                    for note in self.notes[t].split(","):
                        s.SOUNDS[note].play()
