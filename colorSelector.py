import pygame
pygame.init()
global colors,color
colors = [(255,255,255),(0,0,0),(200,30,2),(10,150,200)]
color  = [50,0,0]
def create(window):
    g = 20
    for x in colors:
        pygame.draw.rect(window,x,(g-1,439,12,12))
        pygame.draw.rect(window,x,(g,400,10,10))
        g+=30
