from sqlalchemy import false

import lines as l
import constants as ct
import levels_manager.star
import levels_manager.link_types as lt


class Link:
    def __init__(self, start, end, link_type, additional_type = None, life = 0):
        self.start_star = None
        self.end_star = None
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
        self.additional_type_life = -1
        if additional_type is not None and additional_type[0] == "broken":
            self.additional_type_life = self.additional_type[2]

        self.is_broken = False


    def copy(self):
        new_link = Link(self.start, self.end, self.type, self.additional_type, self.additional_type_life)
        new_link.is_broken = self.is_broken
        new_link.start_star = self.start_star
        new_link.end_star = self.end_star
        return new_link

    def draw(self):
        if self.additional_type is None:
            l.add_marker(self.start_pos, self.end_pos, ct.WHITE, self.type[1],None,None)
        else:
            l.add_marker(self.start_pos, self.end_pos, ct.WHITE, self.additional_type[1], self.type[1], self.additional_type[2])

    def use_link(self):
        if self.additional_type is not None:
            if self.additional_type[0] == "broken":
                self.additional_type_life -= 1
                if self.additional_type == lt.ADDITIONAL_BROKEN_3:
                    self.additional_type = lt.ADDITIONAL_BROKEN_2
                elif self.additional_type == lt.ADDITIONAL_BROKEN_2:
                    self.additional_type = lt.ADDITIONAL_BROKEN_1
        if self.additional_type_life == 0:
            self.is_broken = True

    def reset(self):
        if self.additional_type is not None:
            if self.additional_type[0] == "broken":
                self.additional_type_life = self.additional_type[2]
        self.is_broken = False