import pygame
from Player import Player
from TextDocHandler import BlockData
from SpritelikeBox import SpriteBox

class Stage(object):
    """A stage in a level. """
   

    def __init__(self, name, levelObject):

        self.StageLength = int()
        #self.BlockGroup = pygame.sprite.Group()
        self.Name = name
        self.IdCount = 0

        DataObject = BlockData()
        DataObject.ReadHashes(name+".txt", levelObject.Width)
        for picName in DataObject.blockDict:
            for blockPlace in DataObject.blockDict[picName]:
                block = SpriteBox(picName, blockPlace, name+"-"+str(self.IdCount))
                levelObject.AllBlocksGroup.add(block)
                self.IdCount += 1
        self.StageLength = DataObject.maxLength + 40
        del DataObject
        levelObject.Width += self.StageLength
        #print(list(b.Id for b in self.BlockGroup))
