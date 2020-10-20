import pygame
pygame.init()
size = (1024, 768)
fps = 20 # Frames per second
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

x = 50
y = 50
width = 200
height = 100

run = True
while run:
    pygame.time.delay(100)
    pygame.draw.rect(screen, (0,0,255), (x, y, width, height))
    pygame.display.update()

pygame.quit()