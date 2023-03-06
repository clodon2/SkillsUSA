from Globals import *
import arcade as arc
from Automata import generate_start_grid, run_sim


def setup_level(game):
    game.scene = arc.Scene()
    game.scene.add_sprite_list("cells")
    game.grid = generate_start_grid(GRID_WIDTH, GRID_HEIGHT)
    
    for r in range(len(game.grid)):
        for c in range(len(game.grid[0])):
            if game.grid[r][c] == 1:
                cell = arc.SpriteSolidColor(width=CELL_WIDTH, height=CELL_HEIGHT, color=arc.color.BLUE)
                cell.center_x = c * CELL_WIDTH + GRID_BL_POS[0]
                cell.center_y = r * CELL_HEIGHT + GRID_BL_POS[1]
                game.scene.add_sprite("cells", cell)
            

def update_level(game):
    game.grid = run_sim(3, game.grid)

    game.scene.get_sprite_list("cells").clear()
    for r in range(len(game.grid)):
        for c in range(len(game.grid[0])):
            if game.grid[r][c] == 1:
                cell = arc.SpriteSolidColor(width=CELL_WIDTH, height=CELL_HEIGHT, color=arc.color.BLUE)
                cell.center_x = c * CELL_WIDTH + GRID_BL_POS[0]
                cell.center_y = r * CELL_HEIGHT + GRID_BL_POS[1]
                game.scene.add_sprite("cells", cell)
