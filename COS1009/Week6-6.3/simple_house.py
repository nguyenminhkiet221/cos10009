import pygame
import sys

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple House")

SKY = (135, 206, 235)
BROWN = (139, 69, 19)
LIGHT_BROWN = (205, 133, 63)
RED = (200, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

running = True
clock = pygame.time.Clock()

while running:
    clock.tick(60)  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(SKY)

    # Mặt trời
    pygame.draw.circle(screen, YELLOW, (700, 100), 50)

    # Thân nhà
    pygame.draw.rect(screen, LIGHT_BROWN, (300, 300, 200, 200))

    # Mái nhà
    pygame.draw.polygon(screen, RED, [
        (280, 300),
        (400, 0),
        (520, 300)
    ])

    # Cửa
    pygame.draw.rect(screen, BROWN, (375, 380, 50, 120))

    # Cửa sổ
    pygame.draw.rect(screen, WHITE, (320, 330, 50, 50))
    pygame.draw.rect(screen, WHITE, (430, 330, 50, 50))

    pygame.display.flip()

pygame.quit()
sys.exit()