# Task is to click the number buttons in ascending order.
import os
import pygame
import webbrowser
import random


os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (100, 50)
pygame.init()
pygame.display.set_caption("Unlock Manifolds Among US task")
bg = pygame.image.load('images/start.png')
ma = pygame.image.load('images/main.png')


screen_width = 1150
screen_height = 650
print(screen_height,screen_width)
win = pygame.display.set_mode((screen_width,screen_height))
win.blit(bg, (0,0))

red = (178, 34, 34)
orange = (255, 110, 0)
lightblue = (30, 144, 255)
blue = (25, 25, 112)
pink = (255, 105, 180)
black = (0, 0, 0)
aqua = (32, 178, 170)
white = (220, 220, 220)
yellow = (239, 255, 8)
green = (50, 205, 50)


class button(object):
    def __init__(self, x, y, width, height, color1 = red, color2 = red, visible = 1, outline = 0, text='', fontsize = 30):
        self.color = white
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.outline = outline
        self.color1 = color1
        self.color2 = color2
        self.fontsize = fontsize
        self.visible = visible


    def draw(self,size = 0):
        if self.visible:
            pygame.draw.rect(win, self.color, (self.x - size, self.y - size, self.width + 2*size, self.height + 2*size), self.outline)

        if self.text != '':
            font = pygame.font.SysFont('comicsans', self.fontsize)
            text = font.render(self.text, 1, red)
            win.blit(text, (self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def isOver(self, pos2):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if self.x < pos2[0] < self.x + self.width:
            if self.y < pos2[1] < self.y + self.height:
                self.color = self.color2
                self.draw()
                return True

        self.color = self.color1
        self.draw()
        return False


def mydelay(miliSec):          # this function we created gives appprox delay in milisec
    i = 0
    while i < miliSec:
        pygame.time.delay(1)
        i += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                i = miliSec + 1
                pygame.quit()

def displayMessage(message,fontSize, height,color = red):
    font = pygame.font.SysFont('comicsans', fontSize)
    text = font.render(message, 1, color)
    win.blit(text,(screen_width//2 - int(text.get_width()/2),height))
    pygame.display.update()


def unlockmenifolds():
    win.blit(ma, (0, 0))
    mydelay(100)
    loop = True
    print("inside")
    back = button(247, 190, 55, 55,black,blue,0)
    youtube.draw()
    back.draw()
    buttonsize = 83
    xypos = {
        1 : [350, 237],
        2 : [441, 237],
        3 : [534, 237],
        4 : [626, 237],
        5 : [718, 237],
        6 : [350, 330],
        7 : [441, 330],
        8 : [534, 330],
        9 : [626, 330],
        10: [718, 330]
    }
    numbers = [str(x+1) for x in range(10)]
    randnumbers =  random.sample(numbers, len(numbers))
    buttons = []
    print(randnumbers)
    counter = 1
    reflist = []
    for i in randnumbers:
        x,y= xypos[counter]
        counter += 1
        buttons.append(button(x, y, buttonsize, buttonsize, blue, lightblue, 1, 0, str(i),80))

    for i in buttons:
        i.draw()

    while loop:
        pos_in = pygame.mouse.get_pos()
        if youtube.isOver(pos_in) and pygame.mouse.get_pressed(3)[0]:
            webbrowser.open('https://www.youtube.com/channel/UCB0S_0lk99N_MAOHJZMdkUw')
        if back.isOver(pos_in) and pygame.mouse.get_pressed(3)[0]:
            back.draw(3)
            pygame.display.update()
            loop = False
        for n in buttons:
            if n.isOver(pos_in) and pygame.mouse.get_pressed(3)[0]:
                if n.text not in reflist:
                    reflist.append(n.text)
                    if reflist == numbers[:len(reflist)]:
                        print("same")
                        n.color1 = green
                        n.color2 = green
                        n.draw()
                        if len(reflist) == 10:
                            n.isOver(pos_in)
                            displayMessage("Task Complete!", 84, 100, yellow)
                            pygame.display.update()
                            mydelay(3000)
                            loop = False

                    else:
                        displayMessage("Task incomplete!", 84, 100)
                        pygame.display.update()
                        mydelay(3000)
                        loop = False

        back.draw()
        youtube.draw()
        pygame.display.update()
        mydelay(50)



taskbutton = button(453,120,50,30,yellow,yellow,1,1)
youtube = button(20,455,180,180,red,red,0)
run = True
while run:
    pos = pygame.mouse.get_pos()
    if youtube.isOver(pos) and pygame.mouse.get_pressed(3)[0]:
        webbrowser.open('https://www.youtube.com/channel/UCB0S_0lk99N_MAOHJZMdkUw')
    if taskbutton.isOver(pos) and pygame.mouse.get_pressed(3)[0]:
        taskbutton.draw(1)
        pygame.display.update()
        unlockmenifolds()

    mydelay(100)
    win.blit(bg, (0, 0))
    taskbutton.draw()
    youtube.draw()
    pygame.display.update()
