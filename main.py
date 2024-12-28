import math
import random
import time
import pygame
pygame.init()

WIDTH , HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("AIM TRAINER")

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