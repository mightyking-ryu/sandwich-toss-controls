from math import *
import pygame
from ellipse import ellipse


pygame.init()
pygame.font.init()
pygame.display.set_caption('타원')

size  = 800, 800
screen = pygame.display.set_mode(size)

my_ellipse = ellipse(f_point=(400, 400), win_size=(800, 800), r_k=0.5)
my_ellipse2 = ellipse(f_point=(400, 400), win_size=(800, 800), r_k=0.5)
my_ellipse3 = ellipse(f_point=(400, 400), win_size=(800, 800), r_k=0.5)
my_ellipse.set_v(1)
my_ellipse2.set_v(1)
my_ellipse3.set_v(t=my_ellipse.T*0.8)

p = 0
p2 = -int(len(my_ellipse2.points)*0.2)
p3 = 0

now = False
now2 = True

clock = pygame.time.Clock()

font1 = pygame.font.SysFont("한컴말랑말랑", 100)
img1 = font1.render('성공!',True, "purple")


running = True
while running:

    if p==len(my_ellipse.points):
        p = 0
        now = False
        now2 = False

    if p2==len(my_ellipse2.points) or p2==0:
        p2 = 0
        now = True
    
    if p3==len(my_ellipse3.points):
        p3 = 0

    dt = clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("gray")


    x, y = my_ellipse.points[p]

    x1, y1 = my_ellipse2.points[p2]

    x2, y2 = my_ellipse3.points[p3]

    pygame.draw.circle(screen, (0, 0, 255), my_ellipse.convert_coordinate(my_ellipse.f_point), 60)
    pygame.draw.circle(screen, (255, 0, 0), (int(x), int(y)), 20)
    pygame.draw.circle(screen, (0, 255, 0), (int(x1), int(y1)), 20)
    if now==True:
        pygame.draw.circle(screen, (0, 0, 0), (int(x2), int(y2)), 10)

    if now2==False:
        screen.blit(img1, (300, 150))
    pygame.display.update()
    if now2==True:
        p += 1
        p2 += 1
    if now==True:
        p3 += 1

pygame.quit()