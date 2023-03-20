import arcade as arc
from random import randrange
from os import walk


# basically just the randrange function, but automatically puts the lower value first
def easy_randrange(value1, value2, step=1):
    if value1 > value2:
        return randrange(value2, value1, step)
    elif value1 < value2:
        return randrange(value1, value2, step)
    else:
        return value1


# use for sets of animations that DO NOT need to be flipped horizontally
def load_animation_one(path):
    frames = []
    for _, __, image_files in walk(path):
        for image in image_files:
            full_path = path + "/" + image
            image_texture = arc.load_texture(full_path)
            frames.append(image_texture)
    return frames


# Check if point is within bounds of rectangle.
def IsRectCollidingWithPoint(rect, point):
    if rect[3][0] >= point[0] >= rect[0][0] and rect[1][1] >= point[1] >= rect[0][1]:
        return True
    else:
        return False


def get_closest_wall(object, walls):
    closest_wall = walls[0]
    closest_wall_y = abs(object.center_y - walls[0].center_y)
    for wall in walls:
        wall_y_dist = abs(object.center_y - wall.center_y)
        if wall_y_dist < closest_wall_y:
            closest_wall = wall
            closest_wall_y = wall_y_dist

    return closest_wall
