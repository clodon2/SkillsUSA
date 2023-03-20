import arcade as arc
from Globals import *
from math import radians, sin, cos


class BasicPlayer(arc.Sprite):
    def __init__(self):
        super().__init__("./Assets/Player/Audi.png")
        self.scale = .3
        self.angle = -90

    def update(self):
        self.center_x += -self.change_y * sin(radians(self.angle))
        self.center_y += self.change_y * cos(radians(self.angle))

        # Keep player in bounds
        if self.center_x < 0:
            self.center_x = 0
        if self.center_y < 0:
            self.center_y = 0

        if self.center_x > CELL_GRID_WIDTH:
            self.center_x = CELL_GRID_WIDTH
        if self.center_y > CELL_GRID_HEIGHT:
            self.center_y = CELL_GRID_HEIGHT

        self.change_x = 0
        self.change_y = 0
