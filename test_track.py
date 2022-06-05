import pygame

width, height = (1000, 600)
screen = pygame.display.set_mode((width, height))

back_image = pygame.image.load("track.png").convert()
back_rect = back_image.get_rect().move(0, 0)


print(back_rect)
