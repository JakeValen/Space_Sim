#Star class
import pygame as p
import sys
pressed = False
mouse_loc = (0,0)

class Star:
    #The initialization of the star should set the mass and the color of the star.
    def __init__(self,screen,mass=0,color="#000000",center=(750/2,750/2),radius=0):
        self.screen = screen
        self.mass = mass
        self.color = color
        self.center = center
        self.radius = radius

    #This function will prompt the user to input star attributes
    def get_star_attributes(self):
        self.mass = int(input("Enter the mass in kg: "))
        self.color = input("Enter the color in hex: ")
        self.center = (750/2,750/2)
        self.radius = int(input("Enter the radius in Km: "))

    #The create function should draw the star on the screen
    def create(self):
        """
        This will create a star at the center of the window.
        :return:
        """
        p.draw.circle(self.screen, self.color, self.center, self.radius)
        p.display.update()

#Planet class
class Planet:
    def __init__(self,screen,mass=0,color="#000000",radius=0):
        global mouse_loc
        self.screen = screen
        self.mass = mass
        self.color = color
        self.radius = radius
        self.center = mouse_loc
        pass

    def get_planet_attribute(self):
        global mouse_loc
        self.mass = int(input("Enter the mass in kg: "))
        self.color = input("Enter the color in hex: ")
        self.radius = int(input("Enter the radius in Km: "))
        print("Click the location of the planet..")
        while mouse_loc == (0,0): #Trying to add a planet at cursor location when clicked, this is not working yet.
            if p.mouse.get_pressed(3)[0] == 1:
                mouse_loc = p.mouse.get_pos()

    def create(self):
        p.draw.circle(self.screen, self.color, self.center, self.radius)

#Button class
class Button:
    def __init__(self,screen,position,width,height,button_list,on_click_function=None,one_press=False,text=''):
        #Here all the basic attributes are set
        self.x, self.y = position
        self.font = p.font.SysFont("OCR A Extended", 30)
        self.width = width
        self.height = height
        self.text = text
        self.on_click_function = on_click_function
        self.one_press = one_press
        self.screen = screen
        self.already_pressed = False
        #These colors are what will fill the button on its certain states
        self.fillColors = {
            'normal':'#fff7fd',
            'hover':'#d9cbe1',
            'pressed':'#4c3d53'
        }
        #This initializes the surface of the buttons
        self.buttonSurface = p.Surface((self.width, self.height))
        self.buttonRect = p.Rect(self.x, self.y, self.width, self.height)
        self.buttonSurf = self.font.render(text, True, (20,20,20))
        button_list.append(self)

        #This process checks to see what state the button is in
    def process(self):
        global pressed
        mouse_pos = p.mouse.get_pos()
        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mouse_pos):
            self.buttonSurface.fill(self.fillColors['hover'])
            if p.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColors['pressed'])
                #Need to come up with a solution to make it so the button only scans for a single cycle
                if self.one_press:
                    while not pressed:
                        self.on_click_function()
                        pressed = True
                else:
                    self.on_click_function()



        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width/2 - self.buttonSurface.get_rect().width/2,
            self.buttonRect.height/2 - self.buttonSurface.get_rect().height/2
        ])

        self.screen.blit(self.buttonSurface, self.buttonRect)