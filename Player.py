import arcade as arc
import Globals
from math import radians, sin, cos, degrees


class BasicPlayer(arc.Sprite):
    def __init__(self):
        super().__init__("./Assets/Player/playercar.png")
        self.scale = .3 * Globals.SCREEN_PERCENT
        self.angle = -90
        self.speed = 0
        self.power_up = None

    def accelerate(self):
        if self.speed < Globals.PLAYER_MAX_SPEED:
            self.speed += Globals.PLAYER_ACCELERATION_SPEED
        if self.speed > Globals.PLAYER_MAX_SPEED:
            self.speed = Globals.PLAYER_MAX_SPEED

    def backwards_accelerate(self):
        if self.speed > -Globals.PLAYER_BACK_MAX_SPEED:
            self.speed -= Globals.PLAYER_BACK_ACCELERATION_SPEED
        if self.speed < -Globals.PLAYER_BACK_MAX_SPEED:
            self.speed = -Globals.PLAYER_BACK_MAX_SPEED

    def update(self):
        if abs(self.speed) < 0.1:
            self.speed = 0

        # Keep player in bounds
        if self.center_x < 0:
            self.center_x = 0
        if self.center_y < 0:
            self.center_y = 0

        if self.center_x > Globals.CELL_GRID_WIDTH:
            self.center_x = Globals.CELL_GRID_WIDTH
        if self.center_y > Globals.CELL_GRID_HEIGHT:
            self.center_y = Globals.CELL_GRID_HEIGHT

        if self.speed > 0:
            self.speed -= Globals.PLAYER_DEACCELERATION_SPEED
        elif self.speed < 0:
            self.speed += Globals.PLAYER_DEACCELERATION_SPEED

        self.angle += degrees(self.change_angle)
        self.pymunk.body.angle += self.change_angle

        # prevent player from going outside area
        self.pymunk.body._set_position((self.center_x, self.center_y))
