import arcade as arc
import Globals
from math import degrees


class BasicPlayer(arc.Sprite):
    def __init__(self, control="keyboard"):
        super().__init__("./Assets/Player/playercar.png")
        self.control = control
        self.color = ()

        if self.control == "keyboard":
            self.w_pressed = False
            self.s_pressed = False
            self.a_pressed = False
            self.d_pressed = False

            self.up_pressed = False
            self.down_pressed = False
            self.left_pressed = False
            self.right_pressed = False

        else:
            self.thumbstick_rotation = 0
            self.right_trigger_pressed = False
            self.left_trigger_pressed = False

        self.powerup_pressed = False

        self.move_up = False
        self.move_down = False
        self.move_left = False
        self.move_right = False

        self.scale = .3 * Globals.SCREEN_PERCENT
        self.angle = -90
        self.velocity = 0
        self.power_up = None

        self.pymunk_phys = None
        self.last_force = None

    def accelerate(self, force_multiplier=1):
        Globals.ENGINE.apply_force(self, (0, Globals.P_MOVE_FORCE * force_multiplier))

    def backwards_accelerate(self, force_multiplier=1):
        Globals.ENGINE.apply_force(self, (0, -Globals.P_MOVE_FORCE * force_multiplier))

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
