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
        global State,Buttons
        if State==self.Callback:
            State=0
            self.Actor.image='button'
        else:
            State=self.Callback
            self.Actor.image='button_down'
            for i in Buttons:
                if i!=self:
                    i.Actor.image='button'


class LifeText: #文本的类
    def __init__(self,Msg,Pos,Size=20,LifeTime=-1): #文本参数
        self.Msg=Msg #文本
        self.Pos=Pos #位置
        self.LifeTime=LifeTime #持续时间，-1表示永久存在
        self.Size=Size #大小
        self.Death=0 #时间是否结束

    def draw(self): #绘制文本部分
            screen.draw.text(self.Msg,self.Pos,color='black',fontsize=self.Size) #依据文本、位置、大小绘制黑色文本
            
    def up(self): #文本更新部分
        self.LifeTime-=1 #持续时间-1
        if not self.LifeTime: #如果时间到了
            self.Death=1 #表示时间结束


class Panel:
    def __init__(self,No,Pos=(WIDTH//3+50,50),End=(WIDTH//3*2-100,HEIGHT-100),Color=(255,255,255)):
        self.No=No
        self.Pos=Pos
        self.Rect=Rect(Pos,End)
        self.Color=Color
        self.Base=[]
    
    def draw(self):
        global State
        if self.No!=State:
            return
        screen.draw.filled_rect(self.Rect,self.Color)
    


Buttons=[]
Labels=['下载启动器','选择模式','开始游戏']
for i in range(1,4):
    pass
    b=Button((WIDTH//6,HEIGHT//4*(i)),
    Labels[i-1],
    i)
    Buttons.append(b)

Panels=[]
for i in range(1,4):
    Panels.append(Panel(i))


State=0 #0:Nope 1:download 2:choice 3:start


def draw():
    screen.fill((220,220,220))
    screen.draw.line((WIDTH//3,0),(WIDTH//3,HEIGHT),(155,155,155))

    for i in Buttons+Panels:
        i.draw()
    

def on_mouse_down(pos):
    for i in Buttons:
        if i.Callback and i.Actor.collidepoint(pos):
            i.mousedown()
            break



pgzrun.go(Title='TeeStore:Teestore')