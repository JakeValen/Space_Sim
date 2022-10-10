#The goal of this project is to be able to edit and simulate a solar system. This system should be custom and creatable.
#Good luck Jake, you're going to need it..
import pygame as p
import random as r
import simclasses as s
import sys
p.init()

#This function creates a screen for the simulation to use.
def create_screen(width,height):
    screen_init = p.display.set_mode(size=(width,height))
    p.display.set_caption("Space Simulator")
    return screen_init

def button(position,text):
    pass




#Here is where the simulation is run
running = True
while running:

    mouse = p.mouse.get_pos()
    #Initialize the screen
    screen = create_screen(750,750)
    screen.fill((0,0,0))
    p.display.flip()

    #Searchiong through events to set certain conditions
    for event in p.event.get():
        if event.type == p.QUIT: #If the x is hit on the screen, quit the program.
            running = False



