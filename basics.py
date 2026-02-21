import pygame

pygame.init()

window = pygame.display.set_mode((600,400)) # set canvas dimensions
pygame.display.set_caption("Game") # game window title

running = True

while(running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    window.fill("RED") # fill canvas with specified color
    pygame.display.flip()

pygame.quit()