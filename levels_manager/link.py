from star import Star

class Link:
    def __init__(self, start: Star, end: Star, link_type: str):
        self.start = start
        self.end = end
        self.type = link_type

    def draw(self):
        pass