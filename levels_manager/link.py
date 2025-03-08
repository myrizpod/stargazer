import lines as l
import constants as ct

class Link:
    def __init__(self, start: list[int], end: list[int], link_type, additional_type = None):
        self.start = start
        self.end = end
        self.type = link_type
        self.additional_type = additional_type

    def draw(self):
        if self.additional_type is None:
            l.add_marker(self.start, self.end, ct.WHITE, self.type[1])
        else:
            l.add_marker(self.start, self.end, ct.WHITE, self.additional_type, self.type[1], 3)