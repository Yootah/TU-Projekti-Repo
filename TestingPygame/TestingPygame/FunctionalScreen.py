import pygame

class FunctionalScreen(object):
    """Base class for title/end screen. """

    def __init__(self, window, type = "start", rectx=360, recty=600):

        background = window.grid
        logo = pygame.image.load("/data/screens/"+type+"logo.bmp")
        logo.set_colorkey((163,73,164))
        buttonImage = pygame.image.load("/data/screens/"+type+"button1.bmp")

        window.Window.blit(background, (0,0))
        window.Window.blit(logo, (500-rectx/2, 0-recty))
        window.Window.blit(buttonImage, (400, 360))



