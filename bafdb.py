import discord
from discord.ext import commands 
import turtle
import ctypes
from tkinter import simpledialog

scr=turtle.Screen()
scr.bgcolor("black")

#get discord bot token
TOKEN=simpledialog.askstring("Input","Enter bot token here")
print(TOKEN)




#code array. This works by constructing code based on button presses, this is the array of lines

codearr=[]


#Variable used to check if the code being inputted is in a command or not 
#(Pretty much the same as indented)

currentlyInScope=False

#basically for my convenience
debugmode=False

def debugmodeon():
    global debugmode
    if debugmode==False:
        debugmode=True
        print("tru")
        return
    if debugmode==True:
        debugmode=False
        print("fal")
        return

def getmousepos(x,y):
    global debugmode
    msg=f"{x}:{y}"
    if debugmode==True:
        print(msg)



scr.listen()
scr.onkey(debugmodeon, "l")
scr.onclick(getmousepos)

#initialise all buttons for bot construction

#STAY ON THIS X AXIS: x-287 y229

def initturtle(victim,shape,colour,y=229,size=2,x=-287,speed=0):
    victim.penup()
    victim.shape(shape)
    victim.color(colour)
    victim.shapesize(size)
    victim.speed(speed)
    victim.setx(x)
    victim.sety(y)

newcommand=turtle.Turtle()
initturtle(newcommand,"square","blue")
newcommandArr=[[f"@bot.command(name={simpledialog.askstring('Input','command name?')}"],[f"async def {simpledialog.askstring('Input','func name?')}(ctx):"]]#make sure to turn inscopevar to true after this



#little text in the bottom of the screen

littlehelpertext=turtle.Turtle()
littlehelpertext.color("white")

def wr(text,x,y,victim):
    victim.penup()
    victim.setx(x)
    victim.sety(y)
    victim.write(text, font=("Arial",16))
    victim.hideturtle()

wr("press l for debug mode",-24,-180,littlehelpertext)


#bind buttonpresses to code construction


#i should probably start this


# ///


turtle.mainloop()
