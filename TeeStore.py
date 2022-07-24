import pgzrun
import requests

WIDTH=950
HEIGHT=550

class Button:
    FontSize=35
    FontName='font'
    def __init__(self,Pos,Text,Callback=None,Img='button'):
        self.Actor=Actor(Img,Pos)
        self.Pos=Pos
        self.Text=Text
        self.Callback=Callback

        self.Rect=Rect(self.Actor.topleft,self.Actor.bottomright)
    
    def draw(self):
        self.Actor.draw()
        screen.draw.text(self.Text,self.Pos,color='black',fontsize=Button.FontSize,fontname=self.FontName,anchor=(0.5,0.5))
        
        screen.draw.text(self.Text,self.Pos,color='black',fontsize=Button.FontSize)
    
    def mousedown(self):
        if self.Callback:
            self.Callback()

Test=Button((0,0),'HW')

def draw():
    screen.fill((255,255,255))
    Test.draw()

pgzrun.go(Title='TeeStore:Teestore')