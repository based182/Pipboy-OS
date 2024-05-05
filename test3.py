#test file to test code, can interact with the other test files

import pygame

pygame.init()

bootsound = pygame.mixer.Sound("/home/based182/Pipboy OS/sounds/bootsounda.mp3")

pygame.mixer.Sound.play(bootsound)

status = True
while (status):
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            status = False
