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

#This function allows for easy creating of buttons
def button(screen,position,text):
    font = p.font.SysFont("Times New Roman", 50)
    text_renderer = font.render(text,True,(255,255,255))
    p.draw.rect()




#Here is where the simulation is run
running = True
while running:

    mouse = p.mouse.get_pos()
    #Initialize the screen
    game_screen = create_screen(750,750)
    game_screen.fill((0,0,0))
    p.display.flip()

    #Searchiong through events to set certain conditions
    for event in p.event.get():
        if event.type == p.QUIT: #If the x is hit on the screen, quit the program.
            running = False



