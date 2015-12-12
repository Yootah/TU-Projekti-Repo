import pygame
from Level import Level

class GameWindow(object):
    """"""
    
    W = 1000
    H = 480
    BckgrImg = {"1": "bckg1.bmp", "2": "bckg2.bmp", "3": "bckg3.bmp", "4": "bckg4.bmp"}
    grid = pygame.image.load("data/screens/whitegrid.bmp")
    grid.set_colorkey((163,73,164))
    
    def __init__(self):
        """Creating a GameWindow with width, height and caption. 
        Also adding the first level. """
        
        self.Window = pygame.display.set_mode( (self.W, self.H) )
        pygame.display.set_caption("Yoo Asura")
        
        self.Level = Level(self.Window, "bckg1.bmp", "Level 1")


    def NextLevel(self, previous):
        """A new level object after the previous one is through. """
        n = previous+1
        newLevel = Level(self, imageName = self.BckgrImg[str(n)], name = "Level %d" % n)
        del self.Level
        self.Level = newLevel

    def DisplayPause(self):
        self.Window.blit(self.grid, (0,0))
