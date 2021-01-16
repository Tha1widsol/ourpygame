import pygame

pygame.init()       
Windowx=1000                    # These are global variables for the window size(1000 X 1000)
Windowy=1000
pygame.display.set_caption("Ourproject")   

clock = pygame.time.Clock()
screen = pygame.display.set_mode((Windowx,Windowy))


execute = True

while execute:# This is the main loop that runs the entire program.
    for event in pygame.event.get():
        position = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
             execute=False
                    
    keys = pygame.key.get_pressed()
    click = pygame.mouse.get_pressed()
    