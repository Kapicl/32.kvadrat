import pygame
import random
pygame.init()
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Анимация прямоугольников")
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255), (255, 165, 0), (128, 0, 128)]

FPS = 60
clock = pygame.time.Clock()
running = True
while running:
    screen.fill((0, 0, 0))
    rect_size = 190
    center_x, center_y = WIDTH // 2, HEIGHT // 2

    for i in range(19):
        color = random.choice(colors)
        rect_x = center_x - rect_size // 2
        rect_y = center_y - rect_size // 2
        pygame.draw.rect(screen, color, (rect_x, rect_y, rect_size, rect_size), 3)
        rect_size -= 10
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()
