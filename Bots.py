import arcade as arc


class Car(arc.Sprite):
    def __init__(self):
        super().__init__()

    def update(self):
        self.center_x = -self.change_y * sin(radians(self.angle))
        self.center_y = self.change_y * cos(radians(self.angle))