import pygame


class sprite_sheet():
    def __init__(self,sprite):
        self.sprite=sprite


    def image(self,frame,width,height,scale,colour):
        image=pygame.Surface((width,height)).convert_alpha()
        image.blit(self.sprite,(0,0),((frame*width),0,width,height))
        image.set_colorkey(colour)

        return image

