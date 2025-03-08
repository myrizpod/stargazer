from levels_manager.star import Star
import lines as l
import constants as ct

class Link:
    def __init__(self, start: Star, end: Star, link_type: str):
        self.start = start
        self.end = end
        self.start_pos,self.end_pos = l.link_displace(self.start.coordonates,self.end.coordonates) 
        self.type = link_type

    def draw(self):
        l.addmarker(self.start_pos, self.end_pos, ct.WHITE, l.basic)