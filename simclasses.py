#Star class
#Star class should have defining parameters passed in to be set as attributes
class Star:
    #The initialization of the star should set the mass and the color of the star.
    def __init__(self,mass,color):
        self.mass = mass
        self.color = color

    #The create function should draw the star on the screen
    def create(self):
        pass



#Planet class
class Planet:
    def __init__(self,mass,color,path):
        self.mass = mass
        self.color = color
        pass



