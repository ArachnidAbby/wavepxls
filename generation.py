import pygame,colorSelector
f = open("sizes.txt","r")
g = f.read().split("\n")
f.close()
h = int(g[1]) # Defines the height of the grid
w = int(g[0]) # Defines the width of the grid
if h > w:
    div = h
else:
    div = w
global distance
distance = 4 # 250 divided by the width or height, whichever is larger
class init:
    def __init__(self):
        global cubes,timer,counter
        counter = 0
        timer = 0
        cubes = self
        cubes.distance = 500/div
        cubes.list = []
        generate.create(w,h)
class generate:
    def create(width,height):
        for h in range(height):
            for w in range(width):
                cubes.list.append([w,h,(255,255,255)])
    def draw(window):
        global cubes
        for x in cubes.list:
            pygame.draw.rect(window,x[2],[(x[0]*distance),x[1]*distance,distance,distance])
    def mouse(event):
        global timer, counter,distance
        pos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        timer = 1
        try:
            for x in cubes.list:
                if pos[0] >= x[0] *distance and pos[0] <= x[0] *distance+distance:
                    if pos[1] >= x[1] *distance and pos[1] <= x[1] *distance+distance:
                        if click[0] == 1:
                            x[2] = colorSelector.color
        except:
            print("error")
        if click[2] == 1:
            distance+=1
        if click[1] == 1:
            distance-=1

print("magically loaded")
