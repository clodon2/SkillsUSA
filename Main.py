import arcade
import arcade as arc

import Globals
import Levels as lvl
from World_Objects import Drill, DrillGui
from Misc_Functions import IsRectCollidingWithPoint, get_turn_multiplier, pos_scale
from Menus import start_menu, controls_menu, win_menu, loss_menu, play_selection, Icon
from Particles import drill_wall_emit
from math import radians, sin, cos
from copy import deepcopy


class MainMenu(arc.View):
    def __init__(self):
        super().__init__()
        self.width = Globals.SCREEN_WIDTH
        self.height = Globals.SCREEN_HEIGHT

        self.scene = None

        self.camera = None
        self.button_list = []
        self.text_list = []

    def on_show_view(self):
        start_menu(self)

    def on_resize(self, width: int, height: int):
        self.window.set_viewport(0, width, 0, height)
        Globals.resize_screen(width, height)
        self.__init__()
        self.on_show_view()

    def on_draw(self):
        arc.draw_xywh_rectangle_filled(0, 0, Globals.SCREEN_WIDTH, Globals.SCREEN_HEIGHT, color=arc.color.DARK_SLATE_GRAY)

        for button in self.button_list:
            button.update()
        for text in self.text_list:
            try:
                text.update()
            except:
                text.draw()

    def on_mouse_press(self, mouse_x: int, mouse_y: int, button: int, modifiers: int):
        for button in self.button_list:
            if IsRectCollidingWithPoint(button.get_rect(), (mouse_x, mouse_y)):
                if button.id == "start":
                    select_view = PlayerSelect()
                    self.window.show_view(select_view)
                if button.id == "controls":
                    controls_view = ControlsView()
                    self.window.show_view(controls_view)

    def on_key_press(self, key, modifiers):
        if key == arc.key.ESCAPE:
            arc.exit()


class PlayerSelect(arc.View):
    def __init__(self):
        super().__init__()
        self.width = Globals.SCREEN_WIDTH
        self.height = Globals.SCREEN_HEIGHT

        self.scene = None

        self.camera = None
        self.button_list = []
        self.text_list = []
        self.icon_list = []

        self.controllers = arc.get_joysticks()
        # 0 = None, 1 = keyboard, 2 = controller
        self.input_types = [1, 0, 0, 0]

        self.kb_texture = arc.load_texture("Assets/Menus/keyboard_icon.png")
        self.controller_texture = arc.load_texture("Assets/Menus/controller_icon.png")

    def on_show_view(self):
        play_selection(self)

    def on_resize(self, width: int, height: int):
        self.window.set_viewport(0, width, 0, height)
        Globals.resize_screen(width, height)
        self.__init__()
        self.on_show_view()

    def on_draw(self):
        arc.draw_xywh_rectangle_filled(0, 0, Globals.SCREEN_WIDTH, Globals.SCREEN_HEIGHT, color=arc.color.DARK_SLATE_GRAY)

        for button in self.button_list:
            button.update()
        for text in self.text_list:
            try:
                text.update()
            except:
                text.draw()

        # draw icons for input selection
        self.icon_list.clear()
        # loop though input selections and the button ids
        for icon, icon_num in zip(self.input_types, range(len(self.input_types))):
            # add one to icon button id because they start at 1
            icon_num = icon_num + 1
            # find correct button for input type, put at that location
            for button in self.button_list:
                if button.id == f"i{icon_num}":
                    icon_pos = button.location
                    icon_pos = (icon_pos[0], icon_pos[1])
            # draw icons
            if icon == 1:
                self.kb_texture.draw_scaled(icon_pos[0], icon_pos[1], .5)
            elif icon == 2:
                self.controller_texture.draw_scaled(icon_pos[0], icon_pos[1], .5)

    def on_mouse_press(self, mouse_x: int, mouse_y: int, button: int, modifiers: int):
        for button in self.button_list:
            if IsRectCollidingWithPoint(button.get_rect(), (mouse_x, mouse_y)):
                if button.id == "START":
                    game_view = GameView(self.input_types)
                    self.window.show_view(game_view)
                if button.id[0] == "i":
                    self.input_types[int(button.id[1]) - 1] = (self.input_types[int(button.id[1]) - 1] + 1) % 3

    def on_key_press(self, key, modifiers):
        if key == arc.key.ESCAPE:
            arc.exit()


class ControlsView(arc.View):
    def __init__(self):
        super().__init__()
        self.width = Globals.SCREEN_WIDTH
        self.height = Globals.SCREEN_HEIGHT

        self.scene = None

        self.camera = None
        self.button_list = []
        self.text_list = []

    def on_show_view(self):
        controls_menu(self)

    def on_resize(self, width: int, height: int):
        self.window.set_viewport(0, width, 0, height)
        Globals.resize_screen(width, height)
        self.__init__()
        self.on_show_view()

    def on_draw(self):
        arc.draw_xywh_rectangle_filled(0, 0, Globals.SCREEN_WIDTH, Globals.SCREEN_HEIGHT, color=arc.color.DARK_SLATE_GRAY)

        for button in self.button_list:
            button.update()
        for text in self.text_list:
            try:
                text.update()
            except:
                text.draw()

    def on_mouse_press(self, mouse_x: int, mouse_y: int, button: int, modifiers: int):
        for button in self.button_list:
            if IsRectCollidingWithPoint(button.get_rect(), (mouse_x, mouse_y)):
                if button.id == "back":
                    menu_view = MainMenu()
                    self.window.show_view(menu_view)

    def on_key_press(self, key, modifiers):
        if key == arc.key.ESCAPE:
            arc.exit()


class EndMenus(arc.View):
    def __init__(self):
        super().__init__()
        self.width = Globals.SCREEN_WIDTH
        self.height = Globals.SCREEN_HEIGHT

        self.scene = None

        self.camera = None
        self.button_list = []
        self.text_list = []

    def on_show_view(self):
        controls_menu(self)

    def on_resize(self, width: int, height: int):
        self.window.set_viewport(0, width, 0, height)
        Globals.resize_screen(width, height)
        self.__init__()
        self.on_show_view()

    def on_draw(self):
        arc.draw_xywh_rectangle_filled(0, 0, Globals.SCREEN_WIDTH, Globals.SCREEN_HEIGHT, color=arc.color.DARK_SLATE_GRAY)

        for button in self.button_list:
            button.update()
        for text in self.text_list:
            try:
                text.update()
            except:
                text.draw()

    def on_mouse_press(self, mouse_x: int, mouse_y: int, button: int, modifiers: int):
        for button in self.button_list:
            if IsRectCollidingWithPoint(button.get_rect(), (mouse_x, mouse_y)):
                if button.id == "back":
                    menu_view = MainMenu()
                    self.window.show_view(menu_view)

    def on_key_press(self, key, modifiers):
        if key == arc.key.ESCAPE:
            arc.exit()


class WinView(EndMenus):
    def __init__(self):
        super().__init__()

    def on_show_view(self):
        win_menu(self)


class LossView(EndMenus):
    def __init__(self):
        super().__init__()

    def on_show_view(self):
        loss_menu(self)


class GameView(arc.View):
    def __init__(self, inputs=None):
        super().__init__()
        self.width = Globals.SCREEN_WIDTH
        self.height = Globals.SCREEN_HEIGHT

        self.scene = None

        self.camera = None
        self.gui_camera = None
        self.view_left = 0
        self.view_bottom = 0
        self.end_of_map = Globals.CELL_GRID_WIDTH
        self.map_height = Globals.CELL_GRID_HEIGHT - .5 * Globals.CELL_HEIGHT

        self.player = None
        self.players = []

        # input stuff
        self.inputs = inputs
        self.controllers = arc.get_game_controllers()

        usable_controllers = ["keyboard"]
        usable_controllers.extend(arc.get_game_controllers())

        self.player_controls = []
        print(self.inputs, arc.get_game_controllers())
        for i in self.inputs:
            # count controllers
            controller_count = 0
            for cont in usable_controllers:
                print(type(cont), "cont type")
                if type(cont) == object:
                    controller_count += 1

            keyboard_count = usable_controllers.count("keyboard")

            # adds players in as long as there are controllers left to use
            if (len(usable_controllers)) > 0:
                print(i)
                if i == 0:
                    self.player_controls.append("None")
                # use keyboard
                if i == 1 and keyboard_count > 0:
                    self.player_controls.append("keyboard")
                    usable_controllers.pop(usable_controllers.index("keyboard"))
                    # use controller
                if i == 2 and controller_count > 0:
                    # if there is a keyboard left in the list
                    if keyboard_count > 0:
                        print("kb run")
                        u_c_copy = deepcopy(usable_controllers)
                        u_c_copy.pop(u_c_copy.index("keyboard"))
                        selected_controller = u_c_copy[0]
                        self.player_controls.append(selected_controller)
                        usable_controllers.pop(usable_controllers.index(selected_controller))
                    else:
                        print("self-run")
                        self.player_controls.append(usable_controllers[0])
                        usable_controllers.pop(0)
                else:
                    self.player_controls.append("Load Failure")

        print(self.player_controls)
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

        self.thumbstick_rotation = 0

        self.move_up = False
        self.move_down = False
        self.move_left = False
        self.move_right = False

        self.powerup_pressed = False

        # game stuff
        self.race_num = 1
        self.game_timer = 0
        self.past_time = 0
        self.seconds_timer = 0
        self.start_countdown = None
        self.start_countdown_num = 0
        self.drill_gui = None
        self.emitters = []
        self.physics_engine = None
        self.bot_physics = []

        # grid/automata stuff
        self.level_update_timer = 0
        self.grid = []

        self.track_points = []

    def process_keychange(self):
        # print(self.controller.x)

        if self.players is None:
            return

        print(self.player_controls)
        for player, control in zip(self.players, self.player_controls):
            if player.control == "keyboard":
                # Process left/right
                if player.w_pressed or player.up_pressed:
                    player.move_up = True
                else:
                    player.move_up = False

                if player.s_pressed or player.down_pressed:
                    player.move_down = True
                else:
                    player.move_down = False

                if player.a_pressed or player.left_pressed:
                    player.move_left = True
                else:
                    player.move_left = False

                if player.d_pressed or player.right_pressed:
                    player.move_right = True
                else:
                    player.move_right = False

                controller_rotation_mult = 1

            elif player.control == "controller":
                player.thumbstick_rotation = control.x

                # Process left/right
                if player.right_trigger_pressed:
                    player.move_up = True
                else:
                    player.move_up = False

                if player.left_trigger_pressed:
                    player.move_down = True
                else:
                    player.move_down = False

                if player.thumbstick_rotation < -Globals.DEADZONE:
                    player.move_left = True
                else:
                    player.move_left = False

                if player.thumbstick_rotation > Globals.DEADZONE:
                    player.move_right = True
                else:
                    player.move_right = False

                controller_rotation_mult = 1

                if player.thumbstick_rotation != 0:
                    controller_rotation_mult = abs(player.thumbstick_rotation)

            else:
                controller_rotation_mult = 1

            print("sieujhjhersgisehrgiujhesnriguhsrethg")

            if self.seconds_timer < 10:
                pass
            elif player.move_up and not player.move_down:
                player.accelerate()
            elif player.move_down and not player.move_up:
                player.backwards_accelerate()

            if player.move_right and not player.move_left:
                player.change_angle = radians(-Globals.PLAYER_ROTATION_SPEED) * controller_rotation_mult
            elif player.move_left and not player.move_right:
                player.change_angle = radians(Globals.PLAYER_ROTATION_SPEED) * controller_rotation_mult
            elif not player.move_left and not player.move_right:
                player.change_angle = 0

            if player.powerup_pressed and player.power_up == "drill":
                new_drill = Drill(launch_angle=player.angle)
                new_drill.center_x = player.center_x
                new_drill.center_y = player.center_y
                self.scene.add_sprite("powerups", sprite=new_drill)
                player.powerup_pressed = False
                player.power_up = None
                self.drill_gui.toggle()

    def on_key_press(self, key, modifiers):
        for player in self.players:
            if player.control == "keyboard":
                if key == arc.key.W:
                    player.w_pressed = True
                if key == arc.key.S:
                    player.s_pressed = True
                if key == arc.key.A:
                    player.a_pressed = True
                if key == arc.key.D:
                    player.d_pressed = True

                if key == arc.key.UP:
                    player.up_pressed = True
                if key == arc.key.DOWN:
                    player.down_pressed = True
                if key == arc.key.LEFT:
                    player.left_pressed = True
                if key == arc.key.RIGHT:
                    player.right_pressed = True

                if key == arc.key.SPACE:
                    player.powerup_pressed = True

        if key == arc.key.ESCAPE:
            arc.exit()

    def on_key_release(self, key, modifiers):
        for player in self.players:
            if player.control == "keyboard":
                if key == arc.key.W:
                    player.w_pressed = False
                if key == arc.key.S:
                    player.s_pressed = False
                if key == arc.key.A:
                    player.a_pressed = False
                if key == arc.key.D:
                    player.d_pressed = False

                if key == arc.key.UP:
                    player.up_pressed = False
                if key == arc.key.DOWN:
                    player.down_pressed = False
                if key == arc.key.LEFT:
                    player.left_pressed = False
                if key == arc.key.RIGHT:
                    player.right_pressed = False

                if key == arc.key.SPACE:
                    player.powerup_pressed = False

        self.process_keychange()

    # noinspection PyMethodMayBeStatic
    def on_joybutton_press(self, joystick, button):

        if button == 7:  # Right Trigger
            self.right_trigger_pressed = True
        elif button == 6:  # Left Trigger
            self.left_trigger_pressed = True
        elif button == 3:  # "X" Button
            self.powerup_pressed = True

    # noinspection PyMethodMayBeStatic
    def on_joybutton_release(self, joystick, button):

        if button == 7:  # Right Trigger
            self.right_trigger_pressed = False
        elif button == 6:  # Left Trigger
            self.left_trigger_pressed = False
        elif button == 3:  # "X" Button
            self.powerup_pressed = False

    def on_show_view(self):
        arc.set_viewport(0, self.window.width, 0, self.window.height)

        self.controllers = arcade.get_game_controllers()

        if self.controllers:
            if len(self.controllers) > 4:
                self.controllers = self.controllers[:3]

            self.controller = self.controllers[0]
            for controller in self.controllers:
                controller.open()
                controller.push_handlers(self)

        self.load_level()

    def load_level(self):
        lvl.new_track(self)

        # reset timers
        self.game_timer -= self.game_timer

        # start countdown info
        self.start_countdown = arc.Text(f"5", 0, 0, arc.color.WHITE, font_size=60,
                                        font_name="ARCADECLASSIC")
        self.start_countdown.x = (Globals.SCREEN_WIDTH / 2) - (self.start_countdown.content_width / 2)
        self.start_countdown.y = (Globals.SCREEN_HEIGHT / 2) - (self.start_countdown.content_height / 2)

        # drill gui thingy
        drill_gui_x = 50 * Globals.SCREEN_PERCENTS[0]
        drill_gui_y = Globals.SCREEN_HEIGHT / 1.1
        self.drill_gui = DrillGui(drill_gui_x, drill_gui_y)

    def on_resize(self, width: int, height: int):
        Globals.resize_screen(width, height)
        self.__init__()
        self.on_show_view()

    def on_draw(self):
        if self.camera is None:
            return

        self.camera.use()

        arc.draw_rectangle_filled(self.camera.position.x + self.camera.viewport_width / 2,
                                  self.camera.position.y + self.camera.viewport_height / 2,
                                  self.camera.viewport_width, self.camera.viewport_height, arc.color.BLACK)
        self.scene["powerups"].update_animation()
        self.scene.draw()

        for emitter in self.emitters:
            emitter.draw()

        '''
        for bot in self.scene["bots"]:
            arc.draw_line(bot.center_x, bot.center_y, bot.center_x + 100 * cos(bot.desired_angle), bot.center_y + 100 * sin(bot.desired_angle), (0, 0, 255), 10)
        
        i = 0
        for point in self.track_points:
            i += 1
            arc.draw_circle_filled(point[1] * Globals.CELL_WIDTH + Globals.GRID_BL_POS[1], point[0] * Globals.CELL_HEIGHT + Globals.GRID_BL_POS[0], 10, (0, 255, 0))
            arc.draw_text(str(i), point[1] * Globals.CELL_WIDTH, point[0] * Globals.CELL_HEIGHT)
        '''

        # gui cam stuff
        self.gui_camera.use()
        if self.start_countdown:
            self.start_countdown.draw()

        self.drill_gui.draw()
        self.drill_gui.activation_text.draw()

    def center_camera_to_player(self):
        # Scroll left
        left_boundary = self.view_left + Globals.LEFT_VIEWPORT_MARGIN
        if self.player.left < left_boundary:
            self.view_left -= left_boundary - self.player.left

        # Scroll right
        right_boundary = self.view_left + self.width - Globals.RIGHT_VIEWPORT_MARGIN
        if self.player.right > right_boundary:
            self.view_left += self.player.right - right_boundary

        # Scroll up
        top_boundary = self.view_bottom + self.height - Globals.TOP_VIEWPORT_MARGIN
        if self.player.top > top_boundary:
            self.view_bottom += self.player.top - top_boundary

        # Scroll down
        bottom_boundary = self.view_bottom + Globals.BOTTOM_VIEWPORT_MARGIN
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
        if self.view_bottom + self.height > self.map_height:
            self.view_bottom = self.map_height - self.height

        # Scroll to the proper location
        position = self.view_left, self.view_bottom
        self.camera.move_to(position, Globals.CAMERA_SPEED)

        # OLD
        '''''
        screen_center_x = self.player.center_x - (self.camera.viewport_width / 2)
        screen_center_y = self.player.center_y - (
            self.camera.viewport_height / 2
        )

        self.camera.move_to((screen_center_x, screen_center_y))
        '''''

    def on_update(self, delta_time: float):
        self.game_timer += delta_time
        self.seconds_timer = int(self.game_timer)

        self.process_keychange()
        # pre-race info
        if self.seconds_timer < 4:
            self.start_countdown.text = f"Race {self.race_num} of {Globals.RACE_NUM}"
            self.start_countdown.x = Globals.MID_SCREEN - (self.start_countdown.content_width / 2)
            self.start_countdown.y = (Globals.SCREEN_HEIGHT / 2) - (self.start_countdown.content_height / 2)
        # race countdown start
        elif 4 <= self.seconds_timer <= 8.5:
            self.start_countdown_num = -((self.seconds_timer - 4) - 5)
            self.start_countdown.text = f"{self.start_countdown_num}"
            self.start_countdown.x = Globals.MID_SCREEN - (self.start_countdown.content_width / 2)
            self.start_countdown.y = (Globals.SCREEN_HEIGHT / 2) - (self.start_countdown.content_height / 2)
        # GO
        elif 8.5 < self.seconds_timer == 9:
            self.start_countdown_num = -(self.seconds_timer - 5)
            self.start_countdown.text = f"GO"
        # Race started
        else:
            if self.start_countdown:
                self.start_countdown = None
            self.scene.update()
            self.physics_engine.step()
        for emitter in self.emitters:
            emitter.update()
        self.center_camera_to_player()

        # player-power up box interaction
        collisions = arc.check_for_collision_with_list(self.player, self.scene["power_boxes"])
        for box in collisions:
            if not self.player.power_up == "drill":
                self.drill_gui.toggle()
                self.player.power_up = "drill"
            box.kill()

        # bot-exit interaction
        for bot in self.scene["bots"]:
            bot_exit_collisions = arc.check_for_collision_with_list(bot, self.scene["exit"])
            if bot_exit_collisions:
                l_view = LossView()
                self.window.show_view(l_view)

        # player-exit interaction
        exit_collisions = arc.check_for_collision_with_list(self.player, self.scene["exit"])
        if exit_collisions:
            self.race_num += 1
            if self.race_num > Globals.RACE_NUM:
                win_view = WinView()
                self.window.show_view(win_view)
            else:
                Globals.randomize_wall_color()
                self.load_level()

        # powerup interactions
        for powerup in self.scene["powerups"]:
            if powerup.type == "drill":
                for cell in powerup.collides_with_list(self.scene["cells"]):
                    emitter_label, new_emitter = drill_wall_emit((cell.center_x, cell.center_y),
                                                                 cell.texture.image.getcolors()[0][1])
                    self.emitters.append(new_emitter)
                    cell.kill()


def main():
    """Main function"""
    window = arc.Window(Globals.SCREEN_WIDTH, Globals.SCREEN_HEIGHT, Globals.SCREEN_TITLE,
                        fullscreen=False, resizable=True, vsync=False)
    start_view = MainMenu()
    window.show_view(start_view)
    arc.run()


if __name__ == "__main__":
    main()
