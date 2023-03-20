import arcade as arc
from Globals import *
from Misc_Functions import get_closest_wall
from math import sin, cos, radians


class Car(arc.Sprite):
    def __init__(self):
        super().__init__()

    def update(self):
        self.center_x = -self.change_y * sin(radians(self.angle))

        self.center_y = self.change_y * cos(radians(self.angle))


class BasicBot(arc.Sprite):
    def __init__(self, walls):
        super().__init__("./Assets/Player/Audi.png")

        self.scale = .3
        self.angle = -90

        self.walls = walls

        self.wall_closeness = 30

        self.speed = 0

        self.max_speed = BOT_MAX_SPEED

    def accelerate(self):
        if self.change_y < self.max_speed:
            self.change_y += 2

    def update(self):
        print(self.center_x, self.center_y)
        closest_wall = get_closest_wall(self, self.walls)

        cw_y_dist = self.center_y - closest_wall.center_y

        if abs(cw_y_dist) < self.wall_closeness:
            if cw_y_dist < 0:
                self.change_angle = -4
            if cw_y_dist > 0:
                self.change_angle = 4

        self.accelerate()

        self.center_x += -self.change_y * sin(radians(self.angle))
        self.center_y += self.change_y * cos(radians(self.angle))
