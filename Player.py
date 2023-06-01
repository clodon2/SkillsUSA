import arcade as arc
import Globals
from math import degrees
from Misc_Functions import random_color


class BasicPlayer(arc.Sprite):
    def __init__(self, control="keyboard", player_num=0, camera=None):
        if player_num == 1:
            texture_path = "./Assets/Player/greencar.png"
        elif player_num == 2:
            texture_path = "./Assets/Player/pinkcar.png"
        elif player_num == 3:
            texture_path = "./Assets/Enemy/enemycar.png"
        else:
            texture_path = "./Assets/Player/playercar.png"
        super().__init__(texture_path)

        self.camera = PlayerCamera(camera)

        self.control = control

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


class PlayerCamera:
    def __init__(self, cam):
        self.camera = cam
        self.view_left = 0
        self.view_bottom = 0

        self.width_percent = self.camera.viewport_width / Globals.SCREEN_WIDTH
        self.height_percent = self.camera.viewport_height / Globals.SCREEN_HEIGHT

        self.left_margin = 168.75 * self.width_percent
        self.right_margin = 900 * self.width_percent
        self.bottom_margin = 360 * self.height_percent
        self.top_margin = 360 * self.height_percent

    def set_margins(self):
        self.width_percent = self.camera.viewport_width / Globals.SCREEN_WIDTH
        self.height_percent = self.camera.viewport_height / Globals.SCREEN_HEIGHT

        self.left_margin = 168.75 * self.width_percent
        self.right_margin = 900 * self.width_percent
        self.bottom_margin = 360 * self.height_percent
        self.top_margin = 360 * self.height_percent
