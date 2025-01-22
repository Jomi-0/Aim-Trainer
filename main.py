import math
import random
import time
import pygame
pygame.init()

# all unknown code gotten from https://www.youtube.com/@TechWithTim

WIDTH , HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("AIM TRAINER")


TOP_BAR_HEIGHT = 50
LABEL_FONT = pygame.font.SysFont("comicsans",24)

TARGET_INCREMENT = 400
TARGET_EVENT = pygame.USEREVENT
TARGET_PADDING = 30  # how many pizels off the center of the screen
LIVES = 5
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
    

def format_time(secs):
    milli = math.floor(int(secs*1000 %1000)/100)
    seconds = int(round(secs % 60,1))
    minutes = int(secs//60)

    return f"{minutes:02d}:{seconds:02d}.{milli}"


def draw_top_bar(win,elapsed_time,targets_pressed,misses): 
    pygame.draw.rect(win,"grey",(0,0,WIDTH,TOP_BAR_HEIGHT)) 
    time_label = LABEL_FONT.render(
        f"Time:{format_time(elapsed_time)}",1,"black")
    speed = round(targets_pressed/elapsed_time,1)
    speed_label = LABEL_FONT.render(f"Speed:{speed}t/s",1,"black")
    hits_label = LABEL_FONT.render(f"Hits:{targets_pressed}",1,"black")
    lives_label = LABEL_FONT.render(f"Lives:{LIVES - misses}",1,"black")
    win.blit(time_label,(5,5))
    win.blit(speed_label,(200,5)) 
    win.blit(hits_label,(450,5))
    win.blit(lives_label,(650,5)) 

def end_screen(win,elapsed_time,targets_pressed,clicks):
    win.fill("Black")
    pygame.draw.rect(win,"grey",(0,0,WIDTH,TOP_BAR_HEIGHT)) 
    time_label = LABEL_FONT.render(f"Time:{format_time(elapsed_time)}",1,"black")
    speed = round(targets_pressed/elapsed_time,1)
    speed_label = LABEL_FONT.render(f"Speed:{speed}t/s",1,"black")
    hits_label = LABEL_FONT.render(f"Hits:{targets_pressed}",1,"black")
    accuracy = round(targets_pressed/clicks*100,1) if clicks > 0 else 0
    accuracy_label = LABEL_FONT.render(f"Accuracy:{accuracy}%",1,"black")
    win.blit(time_label,(get_middle(time_label),100))
    win.blit(speed_label,(get_middle(speed_label),200)) 
    win.blit(hits_label,(get_middle(hits_label),300))
    win.blit(accuracy_label,(get_middle(accuracy_label),400)) 

    pygame.display.update()

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT() or event.type == pygame.KEYDOWN:
                quit()



def get_middle(surface):
    return WIDTH/2 - surface.get_width()/2
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
        elapsed_time=time.time()-start_time

        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                quit()
                break
            if event.type == TARGET_EVENT:
                x=random.randint(TARGET_PADDING,WIDTH-TARGET_PADDING) #preventing target from going of screen because of radius
                y=random.randint(TARGET_PADDING+TOP_BAR_HEIGHT,HEIGHT-TARGET_PADDING)
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
        if misses>= LIVES:
            end_screen(WIN,elapsed_time,target_pressed)

                
        draw(WIN,targets)
        draw_top_bar(WIN,elapsed_time,target_pressed,misses)
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__": #makes sure the function main runs if we are exucuting this file directly
    main()  

