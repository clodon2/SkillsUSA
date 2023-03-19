import arcade as arc
from math import radians, sin, cos


class BasicPlayer(arc.Sprite):
    def __init__(self):
        super().__init__("./Assets/Player/Audi.png")
        self.scale = .3
        self.angle = -90

    def update(self):
        self.center_x += -self.change_y * sin(radians(self.angle))
        self.center_y += self.change_y * cos(radians(self.angle))
        self.change_x = 0
        self.change_y = 0
