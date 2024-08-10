import discord
from discord.ext import commands 
import turtle
import ctypes
from tkinter import simpledialog
from colorama import Fore

scr=turtle.Screen()
scr.bgcolor("black")

#get discord bot token
TOKEN=simpledialog.askstring("Input","Enter bot token here")
print(TOKEN)




#code array. This works by constructing code based on button presses, this is the array of lines

codearr=[["import discord","from discord.ext import commands"]]

#execution array. same as code array but a single string

execarr=""

def constructcode():
    global codearr,execarr
    for i in codearr:
        for j in i:
            execarr = execarr+(j+"\n")



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
#REMEMBER TO CHECK IF currentlyInScope

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
def newcommandfunc(x,y):
    global currentlyInScope

    if currentlyInScope==True:
        print(Fore.RED, "Leave scope to create new function", Fore.RESET)
        return

    cmdname=simpledialog.askstring("Input","command name here: ")
    fname=simpledialog.askstring("Input","function name here (does not affect functionality):")
    codearr.append( [f'@bot.command(name="{cmdname}")', f'async def {fname}(ctx):'] )
    currentlyInScope=True
    print(codearr)


printtest=turtle.Turtle()
initturtle(printtest,"circle","brown",y=-170)

def printtestfunc(x,y):
    global currentlyInScope
    printparam=simpledialog.askstring("Input","what to print?")
    if currentlyInScope==True:
        codearr.append( [f'    print("{printparam}")'] )
    else:
        codearr.append([f'print("{printparam}")'])
        

play=turtle.Turtle()
initturtle(play,"triangle","green", y=-229)
    
def playfunc(x,y):
    global execarr
    constructcode()
    exec(execarr)


#little text in the bottom of the screen

littlehelpertext=turtle.Turtle()
littlehelpertext.color("white")

def wr(text,x,y,victim):
    victim.penup()
    victim.speed(0)
    victim.setx(x)
    victim.sety(y)
    victim.write(text, font=("Arial",10))
    victim.hideturtle()

wr("press l for debug mode",-24,-180,littlehelpertext)
wr("new command (auto indents)", -310, 190,littlehelpertext)
wr("print test",-310,-205,littlehelpertext)


#bind buttonpresses to code construction

newcommand.onclick(newcommandfunc)
play.onclick(playfunc)
printtest.onclick(printtestfunc)


#i should probably start this


# ///


turtle.mainloop()
