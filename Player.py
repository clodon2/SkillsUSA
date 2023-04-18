import arcade as arc
import Globals
from math import radians, sin, cos, degrees


class BasicPlayer(arc.Sprite):
    def __init__(self):
        super().__init__("./Assets/Player/playercar.png")
        self.scale = .3 * Globals.SCREEN_PERCENT
        self.angle = -90
        self.velocity = 0
        self.power_up = None

        self.pymunk_phys = None
        self.last_force = None

    def accelerate(self):
        Globals.ENGINE.apply_force(self, (0, Globals.P_MOVE_FORCE))

    def backwards_accelerate(self):
        Globals.ENGINE.apply_force(self, (0, -Globals.P_MOVE_FORCE))

    def pymunk_moved(self, physics_engine, dx, dy, d_angle):
        self.velocity = self.pymunk_phys.body.force

    def update(self):
        # Keep player in bounds
        if self.center_x < 0:
            self.center_x = 0
        if self.center_y < 0:
            self.center_y = 0

        if self.center_x > Globals.CELL_GRID_WIDTH:
            self.center_x = Globals.CELL_GRID_WIDTH
        if self.center_y > Globals.CELL_GRID_HEIGHT:
            self.center_y = Globals.CELL_GRID_HEIGHT

        if self.pymunk_phys:
            self.angle += degrees(self.change_angle)
            self.pymunk_phys.body.angle += self.change_angle

            # prevent player from going outside area
            self.pymunk_phys.body._set_position((self.center_x, self.center_y))
