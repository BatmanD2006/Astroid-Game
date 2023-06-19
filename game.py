import random
import pygame
from bullet import *
from target import *



pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0



#Setup 
screen_x=1280
screen_y=720
radius=40
ship_x=1280/2 
ship_y=720/2
bullets= [] #initilize bullets as empty list
targets=[] #initilize targets as empty list
last_time_shot=0
count=0
max_targets=5
target_spawn_rate= .01
score=0

while running:
    dt=clock.tick(120)/1000

    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            running = False  

    def draw():
        screen.fill("black")
        pygame.draw.circle(screen,"red",(ship_x,ship_y),radius)
        for bullet in bullets: #looping over list of Bullet objects called bullets
            Bullet.draw(bullet, screen) #draws every bullet
        for target in targets:
            Target.draw(target,screen)
        pygame.display.flip()
    
    def generate_target():
        target_x=random.randint(0,screen_x)
        target_y=random.randint(0,screen_y)
        target= Target(target_x,target_y,25,1)
        targets.append(target)

    def key_input():
        global ship_x
        global ship_y

        key=pygame.key.get_pressed()
        if (key[pygame.K_w] and ship_y!=radius):
            ship_y-=2.5
        if (key[pygame.K_s] and ship_y!=screen_y-radius):
            ship_y+=2.5
        if (key[pygame.K_d] and ship_x!=screen_x-radius):
            ship_x+=2.5
        if (key[pygame.K_a] and ship_x!=radius):
            ship_x-=2.5

    def mouse_input():
        global bullet, last_time_shot, score

        current_time= pygame.time.get_ticks()
        pos= pygame.mouse.get_pos()
        #angle= get_angle_between((ship_x, ship_y),pos)
        mouse=pygame.mouse.get_pressed()
        if (mouse[0] and current_time - last_time_shot >=250): #2 seconds passed and no bullets exist
            bullet= Bullet(ship_x, ship_y, pos) # creawo keep track of all bullets fired in game
            bullets.append(bullet)
            last_time_shot=current_time #updates last time shot
        for bullet in bullets:
            bullet.update()
            Bullet.update(bullet)#updates all the bullets, moves bullets
            temp_x=Bullet.x_get(bullet)
            temp_y=Bullet.y_get(bullet)
            if Bullet.offscreen(bullet): #checks to see if bullet is offscreen
                bullets.remove(bullet) #if so removes it from list, dont have to update old bullets, optamize performance
            for target in targets: #looping through all targets
                if Target.collide_bullet(target,temp_x,temp_y,Target.get_x(target), Target.get_y(target)): #collision 
                    targets.remove(target)
                    bullets.remove(bullet)
                    score+=100
                    print(score)

    mouse_input()
    draw()
    key_input() 

    for target in targets:
        Target.update(target,ship_x,ship_y)
        if(Target.collide_player(target,ship_x,ship_y,Target.get_x(target),Target.get_y(target))):
            pygame.quit()


    if len(targets) < max_targets:
        if(random.random() < target_spawn_rate):
            generate_target()



    

pygame.display.flip()
pygame.quit()

