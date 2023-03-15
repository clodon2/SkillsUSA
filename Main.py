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

        self.level_update_timer = 0
        self.grid = []

    def on_key_press(self, key, modifiers):
        if key == arc.key.N:
            lvl.update_level(self)

        if key == arc.key.R:
            lvl.new_track(self)

        if key == arc.key.C:
            self.scene["cells"].clear()

    def on_show_view(self):
        arc.set_viewport(0, self.window.width, 0, self.window.height)
        self.load_level()

    def load_level(self):
        lvl.new_track(self)

    def on_draw(self):
        arc.draw_rectangle_filled(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT, arc.color.BLACK)
        self.scene.draw()

    def on_update(self, delta_time: float):
        self.scene.update()


def main():
    """Main function"""
    window = arc.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, fullscreen=False, resizable=True)
    start_view = GameView()
    window.show_view(start_view)
    arc.run()


if __name__ == "__main__":
    main()
