import math
import random
import time
import pygame
pygame.init()

WIDTH , HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("AIM TRAINER")

TARGET_INCREMENT = 400
TARGET_EVENT = pygame.USEREVENT
TARGET_PADDING = 30  # how many pizels off the center of the screen

class Target:
    MAX_SIZE = 30
    GROWTH_RATE = 0.2
    COLOUR = "red"
    SECOND_COLOUR = "white"
    #constructor
    #set up the initial state of an object by initializing the attributes or properties of the class.
    def __init__(self,x,y): #self allows you to access the attributes and methods of the object. When you create an object from a class, the __init__ method is automatically called.
        self.x=x
        self.y=y
        self.size =0
        self.grow =True
    def update(self):
        if self.size + self.GROWTH_RATE >= self.MAX_SIZE:
            self.grow = False
        if self.grow:
            self.size += self.GROWTH_RATE
        else:
            self.size -= self.GROWTH_RATE
    def draw(self,win):
        pygame.draw.circle(win,self.COLOUR,(self.x,self.y),self.size)
        pygame.draw.circle(win,self.SECOND_COLOUR,(self.x,self.y),self.size*0.8)
        pygame.draw.circle(win,self.COLOUR,(self.x,self.y),self.size*0.6)
        pygame.draw.circle(win,self.SECOND_COLOUR,(self.x,self.y),self.size*0.4)

def draw(win, targets):
    win.fill("Black")      # Background colour

    for target in targets:
        target.draw(win)
    pygame.display.update()
def main():
    run = True
    targets = []
    clock = pygame.time.Clock() #creating a framerate so it isn't based on how fast the computer processing speed is
    pygame.time.set_timer(TARGET_EVENT,TARGET_INCREMENT)
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                run = False
                break
            if event.type == TARGET_EVENT:
                x=random.randint(TARGET_PADDING,WIDTH-TARGET_PADDING) #preventing target from going of screen because of radius
                y=random.randint(TARGET_PADDING,HEIGHT-TARGET_PADDING)
                target=Target(x,y)
                targets.append(target)
        for target in targets:
            target.update()
        draw(WIN,targets)
    pygame.quit()

if __name__ == "__main__": #makes sure the function main runs if we are exucuting this file directly
    main()