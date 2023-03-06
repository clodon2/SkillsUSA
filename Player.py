import arcade as arc
from math import radians, sin, cos


class Player(arc.Sprite):
    def __init__():
        super().__init__()
        
        self.velocity = 0
        
    def update(self):
        angle_rad = radians(self.angle)
        
        self.angle += self.change_angle
        
        self.change_x = self.velocity * sin(angle_rad)
        self.change_y = self.velocity * cos(angle_rad)
