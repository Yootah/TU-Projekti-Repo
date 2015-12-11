import pygame
from Level import Level

class GameWindow(object):
    """"""
    
    W = 1000
    H = 480
    BckgrImg = {"1": "bckg.bmp"}
    
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


