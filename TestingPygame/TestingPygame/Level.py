import pygame
from Environment import Stage
from Player import Player

class Level(object):
    """List of stages should be created before a correponding Level object"""
    Name = str()
    Bckgr = None       # some image
    CurrentStage = Stage()
    AwaitingStages = []
    Width = 0
    LevelShift = 0
    CurrentX = 0       # amount of shift; max: (W - 1000); former X
    EndReached = False
    StagesList = list()
    PlayerGroup = pygame.sprite.GroupSingle() 

    def __init__(self, window, imageName = "bckg.bmp", name = "Level x", stages = list()):
        self.PlayerGroup.add(Player())
        self.StagesList = stages
        self.Bckgr = pygame.image.load(imageName)
        self.Width = sum(map(lambda stg: stg.StageLength, stages))
        self.CurrentStage = self.StagesList.pop(0)
        window.blit(self.Bckgr, (self.CurrentX, 0))

    def NextStage(self):
        """Assuming that the level has an existing StagesList. """
        if self.StagesList: 
            newStage = self.StagesList.pop(0)
            newStage.SetBoxesX()
            self.AwaitingStages.append(newStage)
        else:
            pass    # End Level

    def DrawFrame(self, screen):
        screen.blit(self.Bckgr, (X,0))
        self.CurrentStage.BlockGroup.draw(screen)
        for stg in self.AwaitingStages:
            stg.BlockGroup.draw(screen)
        self.PlayerGroup.draw(screen)





        


