import arcade
import arcade as arc
from Globals import *
import Levels as lvl
from World_Objects import Drill
from math import radians


class MainMenu(arc.View):
    def __init__(self):
        super().__init__()
        self.width = SCREEN_WIDTH
        self.height = SCREEN_HEIGHT

        self.scene = None

    def on_draw(self):
        self.scene.draw()

    def on_update(self, delta_time: float):
        self.scene.update()


class GameView(arc.View):
    def __init__(self):
        super().__init__()
        self.width = SCREEN_WIDTH
        self.height = SCREEN_HEIGHT

        self.scene = None

        self.camera = None
        self.view_left = 0
        self.view_bottom = 0
        self.end_of_map = CELL_GRID_WIDTH
        self.map_height = CELL_GRID_HEIGHT

        self.player = None

        # input stuff
        self.controller = None

        self.right_trigger_pressed = False
        self.left_trigger_pressed = False

        self.w_pressed = False
        self.s_pressed = False
        self.a_pressed = False
        self.d_pressed = False

        self.up_pressed = False
        self.down_pressed = False
        self.left_pressed = False
        self.right_pressed = False

        self.move_up = False
        self.move_down = False
        self.move_left = False
        self.move_right = False

        self.physics_engine = None

        # grid/automata stuff
        self.level_update_timer = 0
        self.grid = []

    def process_keychange(self):
        # print(self.controller.x)

        # Process left/right
        if self.w_pressed or self.up_pressed or self.right_trigger_pressed:
            self.move_up = True
        else:
            self.move_up = False

        if self.s_pressed or self.down_pressed or self.left_trigger_pressed:
            self.move_down = True
        else:
            self.move_down = False

        if self.a_pressed or self.left_pressed or (self.controller and self.controller.x < -DEADZONE):
            self.move_left = True
        else:
            self.move_left = False

        if self.d_pressed or self.right_pressed or (self.controller and self.controller.x > DEADZONE):
            self.move_right = True
        else:
            self.move_right = False

        if self.move_right and not self.move_left:
            self.player.change_angle = -PLAYER_ROTATION_SPEED
        elif self.move_left and not self.move_right:
            self.player.change_angle = PLAYER_ROTATION_SPEED
        elif not self.move_left and not self.move_right:
            self.player.change_angle = 0

        if self.move_up and not self.move_down:
            self.player.change_y = PLAYER_MOVEMENT_SPEED
        elif self.move_down and not self.move_up:
            self.player.change_y -= PLAYER_MOVEMENT_SPEED
        elif not self.move_up and not self.move_down:
            self.player.change_y = 0

    def on_key_press(self, key, modifiers):
        if key == arc.key.W:
            self.w_pressed = True
        if key == arc.key.S:
            self.s_pressed = True
        if key == arc.key.A:
            self.a_pressed = True
        if key == arc.key.D:
            self.d_pressed = True

        if key == arc.key.UP:
            self.up_pressed = True
        if key == arc.key.DOWN:
            self.down_pressed = True
        if key == arc.key.LEFT:
            self.left_pressed = True
        if key == arc.key.RIGHT:
            self.right_pressed = True

        if key == arc.key.ESCAPE:
            quit()
        # DEV INPUTS
        if key == arc.key.SPACE:
            for i in self.scene["powerups"]:
                print(i, "easjg")
            new_drill = Drill(launch_angle=self.player.angle)
            new_drill.center_x = self.player.center_x
            new_drill.center_y = self.player.center_y
            self.scene.add_sprite("powerups", sprite=new_drill)


        # run cellular automata for 1 step
        if key == arc.key.N:
            lvl.update_level(self)

        # generate new track
        if key == arc.key.R:
            lvl.new_track(self)

        # clears current grid
        if key == arc.key.C:
            self.scene["cells"].clear()

    def on_key_release(self, key, modifiers):
        if key == arc.key.W:
            self.w_pressed = False
        if key == arc.key.S:
            self.s_pressed = False
        if key == arc.key.A:
            self.a_pressed = False
        if key == arc.key.D:
            self.d_pressed = False

        if key == arc.key.UP:
            self.up_pressed = False
        if key == arc.key.DOWN:
            self.down_pressed = False
        if key == arc.key.LEFT:
            self.left_pressed = False
        if key == arc.key.RIGHT:
            self.right_pressed = False

        self.process_keychange()

    # noinspection PyMethodMayBeStatic
    def on_joybutton_press(self, joystick, button):

        if button == 7:  # Right Trigger
            self.right_trigger_pressed = True
        elif button == 6:  # Left Trigger
            self.left_trigger_pressed = True

    # noinspection PyMethodMayBeStatic
    def on_joybutton_release(self, joystick, button):

        if button == 7:  # Right Trigger
            self.right_trigger_pressed = False
        elif button == 6:  # Left Trigger
            self.left_trigger_pressed = False

    def on_show_view(self):
        arc.set_viewport(0, self.window.width, 0, self.window.height)

        controllers = arcade.get_game_controllers()

        if controllers:
            self.controller = controllers[0]
            self.controller.open()
            self.controller.push_handlers(self)

        self.load_level()

    def load_level(self):
        lvl.new_track(self)

    def on_draw(self):
        self.camera.use()

        arc.draw_rectangle_filled(self.camera.position.x + self.camera.viewport_width / 2,
                                  self.camera.position.y + self.camera.viewport_height / 2,
                                  self.camera.viewport_width, self.camera.viewport_height, arc.color.BLACK)
        self.scene["powerups"].update_animation()
        self.scene.draw()

    def center_camera_to_player(self):
        # Scroll left
        left_boundary = self.view_left + LEFT_VIEWPORT_MARGIN
        if self.player.left < left_boundary:
            self.view_left -= left_boundary - self.player.left

        # Scroll right
        right_boundary = self.view_left + self.width - RIGHT_VIEWPORT_MARGIN
        if self.player.right > right_boundary:
            self.view_left += self.player.right - right_boundary

        # Scroll up
        top_boundary = self.view_bottom + self.height - TOP_VIEWPORT_MARGIN
        if self.player.top > top_boundary:
            self.view_bottom += self.player.top - top_boundary

        # Scroll down
        bottom_boundary = self.view_bottom + BOTTOM_VIEWPORT_MARGIN
        if self.player.bottom < bottom_boundary:
            self.view_bottom -= bottom_boundary - self.player.bottom

        # keeps camera in left bound of map
        if self.view_left < 0:
            self.view_left = 0

        # keeps camera in right bound of map
        if (self.view_left + self.width) > self.end_of_map:
            self.view_left = self.end_of_map - self.width

        # keeps camera in bottom bound of map
        if self.view_bottom < 0:
            self.view_bottom = 0

        # keeps camera in top bound of map
        if self.view_bottom > self.map_height:
            self.view_bottom = self.map_height

        # Scroll to the proper location
        position = self.view_left, self.view_bottom
        self.camera.move_to(position, CAMERA_SPEED)

        # OLD
        '''''
        screen_center_x = self.player.center_x - (self.camera.viewport_width / 2)
        screen_center_y = self.player.center_y - (
            self.camera.viewport_height / 2
        )

        self.camera.move_to((screen_center_x, screen_center_y))
        '''''

    def on_update(self, delta_time: float):
        self.process_keychange()
        self.scene.update()
        self.physics_engine.update()
        self.center_camera_to_player()

        # powerup interactions
        for powerup in self.scene["powerups"]:
            if powerup.type == "drill":
                for cell in powerup.collides_with_list(self.scene["cells"]):
                    cell.kill()

def main():
    """Main function"""
    window = arc.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, fullscreen=False, resizable=True)
    start_view = GameView()
    window.show_view(start_view)
    arc.run()


if __name__ == "__main__":
    main()
