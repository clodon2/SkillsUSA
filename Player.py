import arcade as arc
from math import radians, sin, cos


class BasicPlayer(arc.Sprite):
    def __init__(self):
        super().__init__()
        self.texture = arc.load_texture(":resources:images/animated_characters/female_person/femalePerson_idle.png")
        self.scale = .5

    def update(self):
        print(self.change_y, self.change_x)
        self.center_x += self.change_x
        self.center_y += self.change_y
        self.change_x = 0
        self.change_y = 0
