from email.base64mime import header_length
from urllib.request import HTTPDefaultErrorHandler


class Building:
    def __init__(self, hp, x, y):
        self.hp = hp
        self.x = x
        self.y = y

    def details(self):
        print("\nx co-ordinate is ", self.x, "\ny co-ordinate is ",
              self.y, "\ncurrent hit points are ", self.hp)


class Hut(Building):
    def __init__(self, hp, x, y, id):
        self.x_len = 2
        self.y_len = 2
        self.id = id
        Building.__init__(self, hp, x, y)
    building_type = "Hut"

    def details(self):
        print("\nThis is a Hut,size of this hut is 2x2", "\nx co-ordinate is ",
              self.x, "\ny co-ordinate is ", self.y, "\ncurrent hit points are ", self.hp)


class Town_Hall(Building):
    def __init__(self, hp, x, y):
        self.x_len = 3
        self.y_len = 4
        Building.__init__(self, hp, x, y)
    building_type = "Town_hall"

    def details(self):
        print("\nThis is a Town_Hall,size of this town hall is 4x3", "\nx co-ordinate is ",
              self.x, "\ny co-ordinate is ", self.y, "\ncurrent hit points are ", self.hp)


class Wall(Building):
    def __init__(self, hp, x, y):
        self.x_len = 1
        self.y_len = 1
        Building.__init__(self, hp, x, y)
    building_type = "Wall"

    def details(self):
        print("\nThis is a Wall,size of this wall is 1x1", "\nx co-ordinate is ",
              self.x, "\ny co-ordinate is ", self.y, "\ncurrent hit points are ", self.hp)


class Cannon(Building):
    def __init__(self, hp, x, y, attack, id):
        self.x_len = 1
        self.y_len = 1
        self.range = 8
        self.rate_of_damage = 10
        self.id = id
        self.state = 0
        Building.__init__(self, hp, x, y)
    building_type = "Cannon"

    def details(self):
        print("\nThis is a Cannon,size of this cannon is 1x1", "\nx co-ordinate is ",
              self.x, "\ny co-ordinate is ", self.y, "\ncurrent hit points are ", self.hp)
class Wizard_Tower(Building):
    def __init__(self, hp, x, y, attack, id):
        self.x_len = 1
        self.y_len = 1
        self.range = 8
        self.rate_of_damage = 10
        self.id = id
        self.state = 0
        Building.__init__(self, hp, x, y)
    building_type = "Wizard_Tower"

    def details(self):
        print("\nThis is a Wizard Tower,size of this Wizard Tower is 1x1", "\nx co-ordinate is ",
              self.x, "\ny co-ordinate is ", self.y, "\ncurrent hit points are ", self.hp)