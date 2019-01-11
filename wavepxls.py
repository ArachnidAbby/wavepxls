import pygame # Imports Pygame
import generation
import colorSelector
pygame.init() # Initialize Pygame
generation.init()
gameDisplay = pygame.display.set_mode((350,350)) # Window size
pygame.display.set_caption("Lights Out") # Window title
m = pygame.image.load(r"Images\\menu.png") # Load menu screen image
icon = pygame.image.load(r"Images\\icon.png") # Load icon image
pygame.display.set_icon(icon) # Window icon

rectA = [0,0,10,10] # Rectangle parameters
running = True # Boolean for game loop running
menu = False # Boolean for menu
while running: # Game loop
    gameDisplay.fill([33,22,15]) # Background color update
    for event in pygame.event.get(): # Event stuff
        if event.type == pygame.QUIT: # If they press the X on the window
            running = False # Game loop condition turns false
        if event.type == pygame.KEYUP: # If they let go of a key
            if event.key != pygame.K_ESCAPE: # If that key is not the escape key
                if menu:
                    menu = False
            if event.key == pygame.K_ESCAPE: # If that key is the escape key
                if menu == False:
                    menu = True
                elif menu:
                    running = False
    generation.generate.mouse(0)
    if menu: # If the program is supposed to open the menu
        gameDisplay.blit(m,(175 - (m.get_size()[0]/2),175 - (m.get_size()[1]/2)))
    generation.generate.draw(gameDisplay)# The menu is opened
    colorSelector.create(gameDisplay)
    pygame.display.update() # Update at end of game loop

pygame.quit() # Quits pygame
