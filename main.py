import math
import random
import time
import pygame
pygame.init()

# all unknown code gotten from https://www.youtube.com/@TechWithTim

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
    def collide(self,x,y):
        # Calculate the distance between the point (x, y) and the center of the circle (self.x, self.y)
        dis = math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2)
        return dis <= self.size
        
def draw(win, targets):
    win.fill("Black")      # Background colour

    for target in targets:
        target.draw(win)
    pygame.display.update()
def main():
    run = True
    targets = []
    clock = pygame.time.Clock() #creating a framerate so it isn't based on how fast the computer processing speed is
    target_pressed= 0
    clicks = 0
    misses = 0
    start_time = time.time()
    
    pygame.time.set_timer(TARGET_EVENT,TARGET_INCREMENT)
    while run:
        clock.tick(60) #because the targets update by frames the more frames there are the harder it becomes
        click=False

        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                run = False
                break
            if event.type == TARGET_EVENT:
                x=random.randint(TARGET_PADDING,WIDTH-TARGET_PADDING) #preventing target from going of screen because of radius
                y=random.randint(TARGET_PADDING,HEIGHT-TARGET_PADDING)
                target=Target(x,y)
                targets.append(target)
            if event.type == pygame.MOUSEBUTTONDOWN:
                click=True
                clicks+= 1 
                mouse_pos = pygame.mouse.get_pos()
        for target in targets:
            target.update()
            if target.size<=0:
                targets.remove(target)
                misses+=1               # Known as SPLAT operator
            if click and target.collide(*mouse_pos):  # * breaks down tuple into its individual components. The collide function is not taking a tuple but the pygame.mouse.get_pos gives thex,y as a tuple so I need to separate them
                targets.remove(target)
                target_pressed+=1
                
        draw(WIN,targets)
    pygame.quit()

if __name__ == "__main__": #makes sure the function main runs if we are exucuting this file directly
    main()