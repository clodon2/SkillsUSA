import arcade as arc
from Globals import *
import Levels as lvl


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

        self.player = None

        # input stuff
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
        print(self.w_pressed)
        # Process left/right
        if self.w_pressed or self.up_pressed:
            self.move_up = True
        else:
            self.move_up = False

        if self.s_pressed or self.down_pressed:
            self.move_down = True
        else:
            self.move_down = False

        if self.a_pressed or self.left_pressed:
            self.move_left = True
        else:
            self.move_left = False

        if self.d_pressed or self.right_pressed:
            self.move_right = True
        else:
            self.move_right = False

        if self.move_right and not self.move_left:
            self.player.change_x = PLAYER_MOVEMENT_SPEED
        elif self.move_left and not self.move_right:
            self.player.change_x = -PLAYER_MOVEMENT_SPEED
        elif not self.move_left and not self.move_right:
            self.player.change_x = 0

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

    def on_show_view(self):
        arc.set_viewport(0, self.window.width, 0, self.window.height)
        self.load_level()

    def load_level(self):
        lvl.new_track(self)

    def on_draw(self):
        arc.draw_rectangle_filled(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT, arc.color.BLACK)
        self.scene.draw()

    def on_update(self, delta_time: float):
        self.process_keychange()
        self.scene.update()
        self.physics_engine.update()


def main():
    """Main function"""
    window = arc.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, fullscreen=False, resizable=True)
    start_view = GameView()
    window.show_view(start_view)
    arc.run()


if __name__ == "__main__":
    main()
