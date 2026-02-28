import pygame

pygame.init()

window = pygame.display.set_mode((800,600))

# initial coords (gameObject spawns at - x,y)
x = 300
y = 200

# movement speed
speed = 1


running = True

while(running):
    for z in pygame.event.get():
        if z.type == pygame.QUIT:
            running = False

    # controls
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        y -= speed
    if keys[pygame.K_a]:
        x -= speed
    if keys[pygame.K_s]:
        y += speed
    if keys[pygame.K_d]:
        x += speed

    window.fill("WHITE")

    # gameObject
    pygame.draw.rect(window, "RED", (x, y, 100, 60))
    
    pygame.display.flip()
pygame.quit()