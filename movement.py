import pygame

pygame.init()

window = pygame.display.set_mode((800,600))

clock = pygame.time.Clock()

# initial coords (gameObject spawns at - x,y)
x = 300
y = 200

# movement speed (pixels/second)
speed = 400

running = True

while(running):
    dt = clock.tick (60) / 1000
    for z in pygame.event.get():
        if z.type == pygame.QUIT:
            running = False

    # controls
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        y -= speed * dt
    if keys[pygame.K_a]:
        x -= speed * dt
    if keys[pygame.K_s]:
        y += speed * dt
    if keys[pygame.K_d]:
        x += speed * dt

    window.fill("WHITE")

    # gameObject
    pygame.draw.rect(window, "RED", (x, y, 100, 60))
    
    pygame.display.flip()
pygame.quit()