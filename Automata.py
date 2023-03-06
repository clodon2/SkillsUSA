# functions and stuff for generation
from Globals import *
from random import choice, randrange


def generate_start_grid(width, height):
    # creates starting grid, 0 = dead cell 1 = alive cell
    grid = create_grid(width, height)
    grid = random_kill(grid)
    return grid


def create_grid(width, height):
    grid = []

    # generate rows
    for w in range(width):
        grid.append([])
        # generate columns
        for h in range(height):
            grid[w].append(1)

    return grid


def random_kill(grid):
    rows = len(grid)
    columns = len(grid[0])
    # amount of cells to kill
    deaths = round(START_DEATH_PERCENT * (rows * columns))
    # choose random cells yo kill
    for i in range(deaths):
        grid[randrange(0, rows, 1)][randrange(0, columns, 1)] = 0

    return grid


def track_kill(grid):
    rows = len(grid)
    columns = len(grid[0])

    deaths = round(START_DEATH_PERCENT * (rows * columns))

    for i in range(deaths):
        pass


# needs to check in a square around the cell for "alive" aka "1" neighbors
def count_alive_neighbors(cell, grid):
    neighbors = 0
    c_row = cell[0]
    c_column = cell[1]
    
    for r in range(-1, 2):
        for c in range(-1, 2):
            if r == 0 and c == 0:
                pass
            else:
                # this error happens with the outside cells of the grid, 
                # it should give them an extra neighbor probably
                try:
                    if grid[c_row + r][c_column + c] == 1:
                        neighbors += 1
                except:
                    pass

    return neighbors


def run_sim_step(grid):
    new_grid = grid
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            neighbors = count_alive_neighbors((r, c), grid)
            if grid[r][c] == 1:
                if neighbors > MAX_NEIGHBORS_DEATH or neighbors < MIN_NEIGHBORS_DEATH:
                    new_grid[r][c] = 0
            if grid[r][c] == 0:
                if neighbors > MIN_NEIGHBORS_BIRTH:
                    new_grid[r][c] = 1

    return new_grid


def run_sim(step_num, grid):
    for i in range(step_num):
        grid = run_sim_step(grid)

    return grid
