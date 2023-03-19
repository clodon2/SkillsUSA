SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720

SCREEN_TITLE = "Cellular Automata Racing"

# Player stuff
PLAYER_MOVEMENT_SPEED = 5
PLAYER_ROTATION_SPEED = 3

DEADZONE = 0.1

# Camera
LEFT_VIEWPORT_MARGIN = SCREEN_WIDTH / 6.4
RIGHT_VIEWPORT_MARGIN = SCREEN_WIDTH / 1.5
BOTTOM_VIEWPORT_MARGIN = SCREEN_HEIGHT / 2
TOP_VIEWPORT_MARGIN = SCREEN_HEIGHT / 2

CAMERA_SPEED = .3

# Powerup stuff
DRILL_SPEED = 6

# Cell Generation
GRID_WIDTH = 500
GRID_HEIGHT = 75
GRID_BL_POS = (5, 5)

CELL_WIDTH = 20
CELL_HEIGHT = 20

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