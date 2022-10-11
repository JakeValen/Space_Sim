#The goal of this project is to be able to edit and simulate a solar system. This system should be custom and creatable.
#Good luck Jake, you're going to need it..
import pygame as p
import random as r
import simclasses as s
import sys
p.init()
buttons = []

#This function creates a screen for the simulation to use.
def create_screen(width,height):
    screen_init = p.display.set_mode(size=(width,height))
    p.display.set_caption("Space Simulator")
    return screen_init

def button_pressed():
    print("Button Pressed")

#Here is where the simulation is run
running = True
while running:
    mouse = p.mouse.get_pos()
    #Initialize the screen
    game_screen = create_screen(750,750)
    game_screen.fill((0,0,0))
    button1 = s.Button(game_screen,(30,30),115,40,button_list=buttons,on_click_function=button_pressed,one_press=True,text="One Press")
    button2 = s.Button(game_screen,(100,100), 115, 40, button_list=buttons, on_click_function=button_pressed,one_press=False, text="Multi Press")
    #Searchiong through events to set certain conditions
    for event in p.event.get():
        if event.type == p.QUIT: #If the x is hit on the screen, quit the program.
            running = False
        if event.type == p.MOUSEBUTTONUP:
            s.pressed = False

    #Searching through the objects to see if they are being executed
    for obj in buttons:
        obj.process()

    p.display.flip()

