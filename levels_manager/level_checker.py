from levels_manager.star import Star
import sound_manager.melodies as m
import constants as ct
import pygame

class LevelChecker:
    def __init__(self, melody):
        self.constelation_melody = melody
        self.tried_melody = None
        self.victory_timer = 0
        self.victory_img = pygame.image.load("resources/images/victory.png")


    def draw(self):
        if self.victory_timer>=1:
            self.victory_timer+=1
            if self.constelation_melody is not None:
                if self.victory_timer >= self.constelation_melody.duration*15:
                    ct.RENDER_BUFFER.blit(self.victory_img,(0,0))
        if self.tried_melody is not None:
            draw_melody(self.tried_melody.notes)


    def update(self):
        if self.tried_melody is not None:
            self.tried_melody.playing_loop()
            if self.victory_timer >= self.constelation_melody.duration*25:
                return True


    def check(self, star: Star, links):
        if star is None:
            return
        e = constelation_reader(star, links)
        self.tried_melody = m.Melody(e)
        self.tried_melody.play()
        if e == self.constelation_melody.notes:
            self.victory()


    def victory(self):
        self.victory_timer = 1


# def draw_melody(notes):
#     start_time = pygame.time.get_ticks()
#     pointer = 0
#     duration = max(notes.keys()) + 1
#
#     def playing_loop(self):
#         if pointer < duration:
#             previous_pointer = self.pointer
#             self.pointer = (pygame.time.get_ticks() - self.start_time)/500
#             for t in self.notes.keys():
#                 if previous_pointer <= t <= self.pointer:
#                     for note in self.notes[t].split(","):
#                         s.SOUNDS[note].play()


def constelation_reader(start_star, links):
    read_dict = {0:start_star.sound_litteral}
    nb_note = 0
    max_note = 10
    pointers = [[start_star,0,None]]
    virtual_links = copy_links(links)
    while nb_note < max_note and pointers!=[]:
        nb_note += 1
        alternative = [pointers[k] for k in range(len(pointers))]
        for pointer in alternative:
            for link in virtual_links:
                if link.is_broken:
                    continue
                if link == pointer[2]:
                    link.use_link()
                    continue
                if link.start_star == pointer[0]:
                    read_dict[float(pointer[1]+link.type[2])] = link.end_star.sound_litteral
                    pointers.append([link.end_star,pointer[1]+link.type[2],link])
                elif link.end_star == pointer[0]:
                    read_dict[float(pointer[1]+link.type[2])] = link.start_star.sound_litteral
                    pointers.append([link.start_star,pointer[1]+link.type[2],link])

            pointers.remove(pointer)
    return read_dict

def copy_links(links):
    l_list = []
    for link in links:
        l_list.append(link.copy())
    return l_list

