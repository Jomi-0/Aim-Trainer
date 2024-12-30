import math
import random
import time
import pygame
pygame.init()

WIDTH , HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("AIM TRAINER")


class Target:
    MAX_SIZE = 30
    GROWTH_RATE = 0.2
    COLOUR = "red"
    #constructor
    #set up the initial state of an object by initializing the attributes or properties of the class.
    def __init__(Self,x,y): #self allows you to access the attributes and methods of the object. When you create an object from a class, the __init__ method is automatically called.
        self.x=x
        self.y=y
        self.size=0
        self.grow=True
def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                run = False
                break
    pygame.quit()

if __name__ == "__main__": #makes sure the function main runs if we are exucuting this file directly
    main()