from random import randrange


# basically just the randrange function, but automatically puts the lower value first
def easy_randrange(value1, value2, step=1):
    if value1 > value2:
        return randrange(value2, value1, step)
    elif value1 < value2:
        return randrange(value1, value2, step)
    else:
        return value1
