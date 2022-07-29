class Attackers:
    def __init__(self, hp, x, y):
        self.hp = hp
        self.x = x
        self.y = y

    def details(self):
        print("\nx co-ordinate is ", self.x, "\ny co-ordinate is ",
              self.y, "\ncurrent hit points are ", self.hp)


class Barbarians(Attackers):
    def __init__(self, hp, x, y):
        self.damage_rate = 10
        self.movement_speed = 1
        Attackers.__init__(self, hp, x, y)
    targetx = -1
    targety = -1
    target = 0

    def details(self):
        print("\nThis is a barbarian", "\nx co-ordinate is ",
              self.x, "\ny co-ordinate is ", self.y, "\ncurrent hit points are ", self.hp)

class Archers(Attackers):
    def __init__(self, hp, x, y):
        self.damage_rate = 5
        self.movement_speed = 2
        range = 9
        Attackers.__init__(self, hp, x, y)
    targetx = -1
    targety = -1
    target = 0
    target_in_range=0

    def details(self):
        print("\nThis is a Archer", "\nx co-ordinate is ",
              self.x, "\ny co-ordinate is ", self.y, "\ncurrent hit points are ", self.hp)

class Balloons(Attackers):
    def __init__(self, hp, x, y):
        self.damage_rate = 20
        self.movement_speed = 2
        Attackers.__init__(self, hp, x, y)
    targetx = -1
    targety = -1
    target = 0

    def details(self):
        print("\nThis is a Balloon", "\nx co-ordinate is ",
              self.x, "\ny co-ordinate is ", self.y, "\ncurrent hit points are ", self.hp)

class King(Attackers):
    def __init__(self, hp, x, y):
        self.damage_rate = 50
        self.movement_speed = 2
        Attackers.__init__(self, hp, x, y)

    def details(self):
        print("\nThis is the King", "\nx co-ordinate is ",
              self.x, "\ny co-ordinate is ", self.y, "\ncurrent hit points are ", self.hp)
class Queen(Attackers):
    def __init__(self, hp, x, y):
        self.damage_rate = 40
        self.movement_speed = 2
        Attackers.__init__(self, hp, x, y)
    attack_direction='w'
    def details(self):
        print("\nThis is the Archer Queen", "\nx co-ordinate is ",
              self.x, "\ny co-ordinate is ", self.y, "\ncurrent hit points are ", self.hp)
