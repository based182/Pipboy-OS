#test file to test code, can interact with the other test files

import pygame


pygame.init()

#setting the screen dimensions

screen = pygame.display.set_mode((480, 320))

#defining the bootscreen image

bootscreen = pygame.image.load("/home/based182/Pipboy OS/images/pipboy bootscreen 480.320.png").convert()

#changes the name of the window

pygame.display.set_caption("Pipboy")

screen.blit(bootscreen, (0, 0))

#update function allows screen to be refresh and the bootscreen image to appear

pygame.display.update()

status = True
while (status):
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            status = False

