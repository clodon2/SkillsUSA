import arcade as arc
from Globals import *
from Misc_Functions import get_closest_wall
from math import sin, cos, radians, degrees, sqrt, atan2, pi


class Car(arc.Sprite):
    def __init__(self):
        super().__init__()

    def update(self):
        self.center_x = -self.change_y * sin(radians(self.angle))

        self.center_y = self.change_y * cos(radians(self.angle))


class BasicBot(arc.Sprite):
    def __init__(self, walls, track_points):
        super().__init__("./Assets/Player/Audi.png")

        self.scale = .3
        self.angle = -90

        self.desired_angle = 0

        self.walls = walls
        self.track_points = track_points
        self.last_track_point = -1

        self.wall_closeness = CELL_HEIGHT * 1.5

        self.speed = 0

        self.max_speed = BOT_MAX_SPEED

    def accelerate(self):
        '''
        if self.change_y < self.max_speed:
            self.change_y += 2
        '''
        self.change_y = self.max_speed

    def update(self):
        closest_wall = get_closest_wall(self, self.walls)
        next_track_point = self.track_points[self.last_track_point + 1]
        next_track_point_pos = (next_track_point[1] * CELL_HEIGHT + GRID_BL_POS[1], next_track_point[0] * CELL_WIDTH + GRID_BL_POS[0])

        if sqrt(abs(next_track_point_pos[0] - self.center_x)**2 + abs(next_track_point_pos[1] - self.center_y)**2) < 5 * CELL_HEIGHT:
            self.last_track_point += 1

        self.angle %= 360

        desired_angle = atan2(next_track_point_pos[1] - self.center_y, next_track_point_pos[0] - self.center_x) - (pi/2)
        print(degrees(desired_angle), next_track_point_pos, (self.center_x, self.center_y))

        '''
        angle_diff = degrees(desired_angle)

        cw_y_dist = self.center_y - closest_wall.center_y
        cw_x_dist = self.center_x - closest_wall.center_x

        direction = 0
        if angle_diff > 0:
            direction = -1
        elif angle_diff < 0:
            direction = 1

        self.angle -= direction
        '''

        self.desired_angle = desired_angle + (pi/2)  # for debugging
        self.angle = degrees(desired_angle)

        self.accelerate()

        self.center_x += -self.change_y * sin(radians(self.angle))
        self.center_y += self.change_y * cos(radians(self.angle))

        self.change_x = 0
        self.change_y = 0
