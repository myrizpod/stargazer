from levels_manager.star import Star
import lines as l

class Link:
    def __init__(self, start: Star, end: Star, link_type: str):
        start.set_link()
        end.set_link()
        self.start = start
        self.end = end
        self.type = link_type

    def draw(self):
        l.addmarker(self.start.coordonates, self.end.coordonates, (199, 212, 225), l.basic)