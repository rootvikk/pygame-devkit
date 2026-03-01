import pygame

pygame.init()

window = pygame.display.set_mode((800,400))

speed = 1

player = pygame.Rect(50, 50, 100, 60)
wall = pygame.Rect(700, 50, 30, 300)

running = True

while(running):
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        player.y -= speed
    if keys[pygame.K_a]:
        player.x -= speed
    if keys[pygame.K_s]:
        player.y += speed
    if keys[pygame.K_d]:
        player.x += speed

    if player.colliderect(wall):
        color = "BLUE"
    else:
        color = "RED"

    window.fill("WHITE")
    
    pygame.draw.rect(window, color, player)
    pygame.draw.rect(window, "BLACK", wall)

    pygame.display.flip()


pygame.quit()