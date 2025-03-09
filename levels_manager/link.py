import lines as l
import constants as ct
import levels_manager.star

class Link:
    def __init__(self, start, end, link_type, additional_type = None):
        if type(start) == levels_manager.star.Star:
            self.start_star = start
            self.start = start.coordonates
        else:
            self.start = start
        if type(end) == levels_manager.star.Star:
            self.end_star = end
            self.end = end.coordonates
        else:
            self.end = end
        self.start_pos,self.end_pos = l.link_displace(self.start,self.end)
        self.type = link_type
        self.additional_type = additional_type

    def draw(self):
        if self.additional_type is None:
            l.add_marker(self.start_pos, self.end_pos, ct.WHITE, self.type[1],None,None)
        else:
            l.add_marker(self.start_pos, self.end_pos, ct.WHITE, self.additional_type[1], self.type[1], self.additional_type[2])