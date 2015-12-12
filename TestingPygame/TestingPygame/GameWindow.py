import pygame
from Level import Level

class GameWindow(object):
    """"""
    
    W = 1000
    H = 480
    BckgrImg = {"1": "bckg.bmp"}
    grid = pygame.image.load("data/screens/whitegrid.bmp")
    grid.set_colorkey((163,73,164))
    
    def __init__(self):
        """Creating a GameWindow with width, height and caption. 
        Also adding the first level. """
        
        self.Window = pygame.display.set_mode( (self.W, self.H) )
        pygame.display.set_caption("Sidescroller Runner Game")
        
        self.Level = Level(self.Window, "bckg.bmp", "Level 1")


    def NextLevel(self, previous):
        """A new level object after the previous one is through. """
        n = "%d" % previous+1
        newLevel = Level(self, imageName = self.BckgrImg[n], name = "Level %d" % n)
        del self.Level
        self.Level = newLevel

    def DisplayPause(self):
        self.Window.blit(self.grid, (0,0))
