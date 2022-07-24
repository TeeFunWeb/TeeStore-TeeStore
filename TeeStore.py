from os import system
import pgzrun
import requests

WIDTH=950
HEIGHT=550



class Button:
    FontSize=35
    FontName='font'
    def __init__(self,Pos,Text,Callback=0,Img='button'):
        self.Actor=Actor(Img,Pos)
        self.Pos=Pos
        self.Text=Text
        self.Callback=Callback
    

    def draw(self):
        self.Actor.draw()
        screen.draw.text(self.Text,self.Pos,color='black',fontsize=Button.FontSize,fontname=self.FontName,anchor=(0.5,0.5))
    

    def mousedown(self):
        global State
        if State==self.Callback:
            State=0
        else:
            State=self.Callback



Buttons=[]
Labels=['下载启动器','选择模式','开始游戏']
for i in range(1,4):
    pass
    b=Button((WIDTH//6,HEIGHT//4*(i)),
    Labels[i-1],
    i)
    Buttons.append(b)


State=0 #0:Nope 1:download 2:choice 3:start
'''
def chstate(v):
    global State
    State=v
    if v==3:
'''


def draw():
    screen.fill((220,220,220))
    screen.draw.line((WIDTH//3,0),(WIDTH//3,HEIGHT),(155,155,155))

    for i in Buttons:
        i.draw()


def on_mouse_down(pos):
    for i in Buttons:
        if i.Callback and i.Actor.collidepoint(pos):
            i.mousedown()
            break



pgzrun.go(Title='TeeStore:Teestore')