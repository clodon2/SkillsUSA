import arcade

from Globals import *
import arcade as arc
from Automata import generate_random_grid, run_sim, generate_track
from Bots import BasicBot
from Player import BasicPlayer
from math import sin, cos


def new_track(game):
    game.scene = arc.Scene()

    # load in track
    game.scene.add_sprite_list("cells", use_spatial_hash=True)
    game.grid = generate_track(GRID_WIDTH, GRID_HEIGHT)

    load_track(game)

    # player
    game.scene.add_sprite_list_after("player", "cells")

    game.camera = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)

    game.player = BasicPlayer()
    game.player.center_x = 2 * CELL_WIDTH
    game.player.center_y = (GRID_HEIGHT / 2) * CELL_HEIGHT
    game.scene.add_sprite("player", game.player)
    game.physics_engine = arc.PhysicsEngineSimple(game.player, game.scene.get_sprite_list("cells"))

    game.scene.add_sprite_list_after("bots", "player")

    bot = BasicBot(walls=game.scene["cells"])
    bot.center_x = 2 * CELL_WIDTH
    bot.center_y = (GRID_HEIGHT / 2) * CELL_HEIGHT
    game.scene.add_sprite("bots", bot)
    bot_physics = arc.PhysicsEngineSimple(bot, game.scene.get_sprite_list("cells"))
    game.bot_physics.append(bot_physics)

    game.scene.add_sprite_list_after("powerups", "bots")


def load_track(game):
    for r in range(len(game.grid)):
        for c in range(len(game.grid[0])):
            if game.grid[r][c] == 1:
                cell_shade = int((sin(r / CELL_COLOR_GRANULARITY) + sin(c / CELL_COLOR_GRANULARITY) + 2) / 4 * (CELL_COLOR_MAX - CELL_COLOR_MIN)) + CELL_COLOR_MIN
                cell = arc.SpriteSolidColor(width=CELL_WIDTH, height=CELL_HEIGHT, color=(cell_shade, cell_shade, cell_shade))
                cell.center_x = c * CELL_WIDTH + GRID_BL_POS[0]
                cell.center_y = r * CELL_HEIGHT + GRID_BL_POS[1]
                game.scene.add_sprite("cells", cell)


def setup_level(game):
    game.scene = arc.Scene()
    game.scene.add_sprite_list("cells", use_spatial_hash=True)
    game.grid = generate_random_grid(GRID_WIDTH, GRID_HEIGHT)

    for r in range(len(game.grid)):
        for c in range(len(game.grid[0])):
            if game.grid[r][c] == 1:
                cell = arc.SpriteSolidColor(width=CELL_WIDTH, height=CELL_HEIGHT, color=arc.color.BLUE)
                cell.center_x = c * CELL_WIDTH + GRID_BL_POS[0]
                cell.center_y = r * CELL_HEIGHT + GRID_BL_POS[1]
                game.scene.add_sprite("cells", cell)


def update_level(game):
    game.grid = run_sim(1, game.grid)

    game.scene.get_sprite_list("cells").clear()
    for r in range(len(game.grid)):
        for c in range(len(game.grid[0])):
            if game.grid[r][c] == 1:
                cell = arc.SpriteSolidColor(width=CELL_WIDTH, height=CELL_HEIGHT, color=arc.color.BLUE)
                cell.center_x = c * CELL_WIDTH + GRID_BL_POS[0]
                cell.center_y = r * CELL_HEIGHT + GRID_BL_POS[1]
                game.scene.add_sprite("cells", cell)
