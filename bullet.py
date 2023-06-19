import pygame
from mathq import *


class Bullet:
    def __init__(self, start_x, start_y, target):
        self.start_x = start_x #pos of ship
        self.start_y = start_y #pos of ship
        self.target_x, self.target_y = target #mouse pos
        self.speed = 5
        self.color = "white"
        self.radius = 10
        self.distance = get_distance_between((self.start_x, self.start_y), (self.target_x, self.target_y)) #distance between me and target
        self.dx = (self.target_x - self.start_x) / self.distance * self.speed #change in x pos / by the distance between points gives ratio how much of total distance correpsonds to horiz displacement 
        self.dy = (self.target_y - self.start_y) / self.distance * self.speed
        self.x = self.start_x
        self.y = self.start_y

    def update(self):
        self.x += self.dx #causing pos to update towards new target
        self.y += self.dy

    def offscreen(self):
        if self.x < 0 or self.x > 1280 or self.y < 0 or self.y > 720: #if x-pos less than 0 off screen same for 1280
            return True
        return False
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

    def x_get(self):
        return self.x
    def y_get(self):
        return self.y




    