import pygame
import os
pygame.init()

# img = pygame.image.load(os.path.join("Media","obstacle_top.png"))
# img1 = pygame.image.load(os.path.join("Media","obstacle_bottom.png"))

# print(img.get_width())
# print(img.get_height())

# print(img1.get_width())
# print(img1.get_height())


FLAPPY_BIRD_IMG = pygame.transform.scale(pygame.image.load(os.path.join("Media","flappy2.png")), (60,50))
print(FLAPPY_BIRD_IMG.get_rect())
# print(FLAPPY_BIRD_IMG.get_rect())
# print(FLAPPY_BIRD_IMG.get_rect())