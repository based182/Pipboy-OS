#this is the bootscreen for the pipboy OS, eventually will have to change the exit function to lead into the main pipboy OS(ro UI)

##add bootsound function

import pygame

#initiates pygame module

pygame.init()


#setting the screen dimensions

screen = pygame.display.set_mode((480, 320))


#defines booting sound file

bootsound = pygame.mixer.Sound("/home/based182/Pipboy OS/sounds/bootsounda.mp3")


#defines the bootscreen image

bootscreen = pygame.image.load("/home/based182/Pipboy OS/images/pipboy bootscreen 480.320.png").convert()


###launch code



#plays boot sound

pygame.mixer.Sound.play(bootsound)



#changes the name of the window


pygame.display.set_caption("Pipboy")



#setups boot image

screen.blit(bootscreen, (0, 0))

#update function allows screen to be refresh and the bootscreen image to appear

pygame.display.update()



#this part of the program enables the code to run, but I don't understand why

status = True
while (status):
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            status = False

