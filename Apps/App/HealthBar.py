import pygame

class healthbar:
    def __init__(self,bx,by,bw,bh,hpmax):
        self.bx=bx
        self.by=by
        self.bw=bw
        self.bh=bh
        self.hpmax=hpmax
    def bdraw(self,hp,bsurface):
        bratio=hp/self.hpmax
        pygame.draw.rect(bsurface,"red",(self.bx,self.by,self.bw,self.bh))
        pygame.draw.rect(bsurface,"green",(self.bx,self.by,self.bw*bratio,self.bh))