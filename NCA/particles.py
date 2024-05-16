import pygame, random

class Sauce():
    def __init__(self, xy):
        self.width=random.randint(1, 2)
        self.height=random.randint(1, 2)
        
        self.color= (random.randint(136, 255),
                     random.randint(0, 80),
                     random.randint(0, 80))
        
        self.vector= (random.random()*2-1,random.random()*2-1)
        
        self.life=80+random.randint(0, 80)
        
        self.x=xy[0]
        self.y=xy[1]
        self.floor=self.y+20+random.randint(0, 8)
        self.speed=random.random()*4
        self.gravity=1
        
    def logic(self):
        self.x+=self.vector[0]*self.speed
        self.y+=self.vector[1]*self.speed+self.gravity
        self.gravity*=1.01
        if self.y>self.floor:
            self.y=self.floor
            
            self.vector=(0,0)
        
        
        self.life-=1
        
    def draw(self, DISPLAY):
        pygame.draw.rect(DISPLAY, self.color, (self.x,self.y,self.width,self.height))
        

        
        
class Exp_Gain():
    def __init__(self, xy):
        self.size=1
        
        self.color= (0,
                     random.randint(180, 255),
                     random.randint(0, 120))
        
        self.vector= (random.random()*2-1,random.random()*2-1)
        
        self.life=random.randint(0, 120)
        
        self.x=xy[0]
        self.y=xy[1]
        self.speed=random.random()*5
        
    def logic(self):
        self.x+=self.vector[0]*self.speed
        self.y+=self.vector[1]*self.speed
        
        
        self.life-=1
        
    def draw(self, DISPLAY):
        pygame.draw.circle(DISPLAY, self.color, (self.x,self.y), self.size)
        
        