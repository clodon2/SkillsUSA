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
