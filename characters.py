import pygame 
from settings import * 
from pygame.math import Vector2 as vec 

class NPC(pygame.sprite.Sprite):
    def __init__(self,game,scene,group,pos,name):
        super().__init__(group)
        self.game = game 
        self.scene = scene 
        self.name = name 
        self.image = pygame.Surface((TILESIZE,TILESIZE*1.5))
        self.rect = self.image.get_rect(topleft = pos)
        self.speed = 60 
        self.force = 2000
        self.acc = vec()
        self.vel = vec() 
        self.fric = -15
        self.pos = pos 
    
    def physics(self,dt):
        
        self.acc.x += self.vel.x*self.fric 
        self.vel.x += self.acc.x*dt
        self.rect.centerx += self.vel.x*dt*10

        self.acc.y += self.vel.y*self.fric 
        self.vel.y += self.acc.y*dt
        self.rect.centery += self.vel.y*dt*10 

        if self.vel.magnitude() >= self.speed:
            self.vel = self.vel.normalize() * self.speed




























class Player(NPC):
    def __init__(self,game,scene,group,pos,name):
        super().__init__(game,scene,group,pos,name)
    
    def movement(self):
        if INPUTS['left']:
            self.acc.x = -self.force
        elif INPUTS['right']:
            self.acc.x = self.force 
        else:
            self.acc.x = 0
        

        if INPUTS['up']:
            self.acc.y = -self.force
        elif INPUTS['down']:
            self.acc.y = self.force 
        else:
            self.acc.y = 0
        
    def update(self,dt):
        self.physics(dt)
        self.movement()