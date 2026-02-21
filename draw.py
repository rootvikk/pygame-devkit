import pygame

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Game Window")

running = True

while(running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # background color
    screen.fill("WHITE")

    # -- Basic Shapes -- 
    pygame.draw.rect(screen, "RED", (100, 100, 200, 100))
    # rect - (surface, color, (x, y, width, height))

    pygame.draw.circle(screen, "BLUE", (400, 100), 50)
    # circle - (surface, color, (x,y), radius)

    pygame.draw.line(screen, "BLACK", (100, 300), (500, 300), 5)
    # line - (surface, color, (starting - x,y) (ending - x,y), width)
    
    pygame.display.flip()

pygame.quit()