import pygame, math

pygame.init()

screen = pygame.display.set_mode([500, 500])
reloj = pygame.time.Clock()

running = True
x = 0
y = 170

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    color = (255, 255, 255)
    screen.fill(color)

    pygame.draw.circle(screen, (0, 0, 240), (x, y), 20)
    
    pygame.display.flip()



    x = x + 4
    y = y + round(8 * (math.sin(math.radians(x))))

    
    if x > 550:
        x = 0
        y = 170

    reloj.tick(50)

pygame.quit()