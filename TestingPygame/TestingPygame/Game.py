import pygame

class Game(object):
    """List of levels should be created before a corresponding Game object (for test, at least)"""
    Window = None
    Levels = list()
    CurrentLevel = None
    
    def __init__(self, levels):
        """Creating a game instance with width, height and caption. 
        Also adding a list of levels. """
        
        self.Window = pygame.display.set_mode( (1000, 480) )
        pygame.display.set_caption("Sidescroller Runner Game")
        
        self.Levels = levels
        self.CurrentLevel = self.Levels.pop[0]

    def NextLevel(self):
        """Only needed if we ever make more than 1 level. """
        if self.Levels:
            self.CurrentLevel = self.Levels.pop(0)
        else:
            pass    # end game if all levels cleared



