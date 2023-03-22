import arcade as arc
from Globals import *
from math import radians, sin, cos


class BasicPlayer(arc.Sprite):
    def __init__(self):
        super().__init__("./Assets/Player/playercar.png")
        self.scale = .3
        self.angle = -90
        self.speed = 0
        self.power_up = None

    def accelerate(self):
        if self.speed < PLAYER_MAX_SPEED:
            self.speed += PLAYER_ACCELERATION_SPEED
        if self.speed > PLAYER_MAX_SPEED:
            self.speed = PLAYER_MAX_SPEED

    def backwards_accelerate(self):
        if self.speed > -PLAYER_BACK_MAX_SPEED:
            self.speed -= PLAYER_BACK_ACCELERATION_SPEED
        if self.speed < -PLAYER_BACK_MAX_SPEED:
            self.speed = -PLAYER_BACK_MAX_SPEED

    def update(self):

        if abs(self.speed) < 0.1:
            self.speed = 0

        self.center_x += -self.speed * sin(radians(self.angle))
        self.center_y += self.speed * cos(radians(self.angle))

        # drifting around turns if above certain speed
        if self.speed > PLAYER_DRIFT_SPEED:
            self.center_y += self.change_angle / (PLAYER_MAX_SPEED - self.speed / PLAYER_DRIFT_SPEED) * sin(radians(self.angle))

        # Keep player in bounds
        if self.center_x < 0:
            self.center_x = 0
        if self.center_y < 0:
            self.center_y = 0

        if self.center_x > CELL_GRID_WIDTH:
            self.center_x = CELL_GRID_WIDTH
        if self.center_y > CELL_GRID_HEIGHT:
            self.center_y = CELL_GRID_HEIGHT

        if self.speed > 0:
            self.speed -= PLAYER_DEACCELERATION_SPEED
        elif self.speed < 0:
            self.speed += PLAYER_DEACCELERATION_SPEED
