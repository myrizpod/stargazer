from levels_manager.star import Star

class Level:
    def __init__(self, all_stars: list[Star]):
        self.links = []
        self.stars = all_stars

    def get_stars(self):
        return self.stars
    def get_links(self):
        return self.links

    def draw(self):
        for star in self.stars:
            star.draw()
        for link in self.links:
            link.draw()
