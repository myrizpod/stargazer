from levels_manager.star import Star
import lines as l
import constants as ct

class Link:
    def __init__(self, start: Star, end: Star, link_type: str):
        self.start = start
        self.end = end
        self.type = link_type

    def draw(self):
        l.addmarker(self.start.coordonates, self.end.coordonates, ct.WHITE, l.basic)