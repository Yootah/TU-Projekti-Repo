import pygame

class FunctionalScreen(object):
    """Base class for title/end screen. """

    def __init__(self, window, type, rectx=int(), recty=int(), string=str()):

        self.background = window.grid
        self.logoname = type+"logo.bmp"
        self.logo = pygame.image.load("/data/screens/"+type+"logo.bmp")
        self.logo.set_colorkey((163,73,164))

        window.Window.blit(background, (0,0))
        window.Window.blit(logo, (500-rectx//2, 40))

        font = pygame.font.SysFont("calibri", 20)
        label = myfont.render(string, 5, (0,0,0))
        window.Window.blit(label, (500-len(string)//2*15, 400))
        





