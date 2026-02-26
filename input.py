import pygame

pygame.init()

window = pygame.display.set_mode((800,600))

running = True

while(running):

    # Event-based input (can't hold down like "sprint")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            print("Key pressed: ", event.key)
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("Mouse clicked at pos: ", event.pos)


    # continuous input (held keys)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        print("key pressed...")
    
    mouse_pos = pygame.mouse.get_pos()
    print(mouse_pos)

pygame.quit()