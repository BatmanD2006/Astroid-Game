import pygame
from bullet import *
from mathq import *
class Target:
    def __init__(self, x, y, radius, speed):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = speed

    def draw(self, screen):
        pygame.draw.circle(screen, "blue", (self.x, self.y), self.radius)

    def update(self, player_x,player_y):
        dx = player_x - self.x #differnce in target and players curr pos
        dy = player_y - self.y
        distance = get_distance_between((self.x, self.y), (player_x, player_y)) #distance between points
        if distance != 0: #avoids divison by 0
            self.x += dx / distance * self.speed #moves target towards player, takes x diff and divdes by total distance  
            self.y += dy / distance * self.speed


    
    def collide_bullet(self, t_x,t_y,b_x,b_y):
        distance= get_distance_between((t_x,t_y),(b_x,b_y))
        if distance < 30:
            return True
        return False
    
    def collide_player(self, t_x,t_y,b_x,b_y):
        distance= get_distance_between((t_x,t_y),(b_x,b_y))
        if distance < 60:
            return True
        return False
    
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y


