import lines as l
import constants as ct

class Link:
    def __init__(self, start: list[int], end: list[int], link_type, additional_type = None):
        self.start = start
        self.end = end
        self.start_pos,self.end_pos = l.link_displace(self.start,self.end)
        self.type = link_type
        self.additional_type = additional_type

    def draw(self):
        if self.additional_type is None:
            l.add_marker(self.start_pos, self.end_pos, ct.WHITE, self.type[1])
        else:
            l.add_marker(self.start_pos, self.end_pos, ct.WHITE, self.additional_type[1], self.type[1], self.additional_type[2])