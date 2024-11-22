# dự trò chơi rpg 2d bàng python
# danh sách thành viên:
#1.Đức Danh code - engineer
#2.Thiên luân vfx + visual edittor
#3.Trọng Hoàng code - engineer
import pygame
import sys
pygame.init()
window_width = 800
window_height = 600
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("RPG - GAME")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
running = True
while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
pygame.quit()
sys.exit()