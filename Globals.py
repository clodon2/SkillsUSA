import arcade as arc

from random import randrange

arc.enable_timings()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
MID_SCREEN = SCREEN_WIDTH / 2

SCREEN_PERCENTS = (SCREEN_WIDTH / 1080, SCREEN_HEIGHT / 720)
SCREEN_PERCENT = (SCREEN_PERCENTS[0] + SCREEN_PERCENTS[1]) / 2

SCREEN_TITLE = "Cave Racer"

# Game Values
RACE_NUM = 6

# Menu Stuff
# for custom fonts
arc.load_font("Assets/Menus/ARCADECLASSIC.TTF")
DEFAULT_FONT_SIZE = 25
TEXTURE_CACHE = 100

# Physics
ENGINE = None

DAMPING = 1

P_FRICTION = .8
P_MOVE_FORCE = 4000
P_MAX_SPEED = 10000

B_FRICTION = 1
B_MOVE_FORCE = 4000
B_MAX_SPEED = 10000

PLAYER_ROTATION_SPEED = 3
BOT_ROTATION_SPEED = 3

DEADZONE = 0.1

# Bot stuff
BOT_MIN_TURN_ANGLE = 5

# Camera
LEFT_VIEWPORT_MARGIN = SCREEN_WIDTH / 6.4
RIGHT_VIEWPORT_MARGIN = SCREEN_WIDTH / 1.2
BOTTOM_VIEWPORT_MARGIN = SCREEN_HEIGHT / 2
TOP_VIEWPORT_MARGIN = SCREEN_HEIGHT / 2

CAMERA_SPEED = .3

# Powerup stuff
DRILL_SPEED = 30

# Cell Generation
GRID_WIDTH = 600
GRID_HEIGHT = 75
GRID_BL_POS = (5, 5)

CELL_WIDTH = 20
CELL_HEIGHT = 20

# Cell colors use an equation, this allows us to tweak some constants
R_CELL_COLOR_RANGE = (50, 128)
G_CELL_COLOR_RANGE = (50, 128)
B_CELL_COLOR_RANGE = (50, 128)
CELL_COLOR_GRANULARITY = 7

CELL_GRID_HEIGHT = CELL_HEIGHT * GRID_HEIGHT
CELL_GRID_WIDTH = CELL_WIDTH * GRID_WIDTH

RANDOM_DEATH_PERCENT = .6

TRACK_KILL_DEATH_PERCENT = .3
TRACK_KILL_POINT_AMOUNT = int(3 * (GRID_WIDTH/100))

# a cell can have up to 8 neighbors
MAX_NEIGHBORS_DEATH = 9
MIN_NEIGHBORS_DEATH = 5

MAX_NEIGHBORS_BIRTH = 9
MIN_NEIGHBORS_BIRTH = 6


# Helper functions

def resize_screen(width: int, height: int):
    global SCREEN_WIDTH, SCREEN_HEIGHT, MID_SCREEN, SCREEN_PERCENTS, SCREEN_PERCENT, CELL_WIDTH, CELL_HEIGHT,\
        CELL_GRID_HEIGHT, CELL_GRID_WIDTH, PLAYER_MAX_SPEED, PLAYER_BACK_MAX_SPEED, PLAYER_DRIFT_SPEED, BOT_MAX_SPEED, \
        DRILL_SPEED

    SCREEN_WIDTH = width
    SCREEN_HEIGHT = height

    MID_SCREEN = SCREEN_WIDTH / 2

    SCREEN_PERCENTS = (SCREEN_WIDTH / 1080, SCREEN_HEIGHT / 720)
    SCREEN_PERCENT = (SCREEN_PERCENTS[0] + SCREEN_PERCENTS[1]) / 2

    CELL_WIDTH = int(20 * SCREEN_PERCENTS[0])
    CELL_HEIGHT = int(20 * SCREEN_PERCENTS[1])

    CELL_GRID_HEIGHT = CELL_HEIGHT * GRID_HEIGHT
    CELL_GRID_WIDTH = CELL_WIDTH * GRID_WIDTH

    PLAYER_MAX_SPEED = 10 * SCREEN_PERCENT
    PLAYER_BACK_MAX_SPEED = PLAYER_MAX_SPEED / 1.2
    PLAYER_DRIFT_SPEED = PLAYER_MAX_SPEED / 1.3

    BOT_MAX_SPEED = 10.23 * SCREEN_PERCENT
    DRILL_SPEED = 14 * SCREEN_PERCENT


def randomize_wall_color():
    global R_CELL_COLOR_RANGE, G_CELL_COLOR_RANGE, B_CELL_COLOR_RANGE

    r_min = randrange(15, 80)
    R_CELL_COLOR_RANGE = (r_min, randrange(r_min, 120))
    g_min = randrange(15, 80)
    G_CELL_COLOR_RANGE = (g_min, randrange(g_min, 120))
    b_min = randrange(15, 80)
    B_CELL_COLOR_RANGE = (b_min, randrange(b_min, 120))
