import pygame
from BlockData import *
from Block import *
from os.path import join

class Stage(object):
    """A stage in a level. """

    def __init__(self, name, levelObject):
        """ name - "01"
            levelObject - Level() 
            """
        self.StageLength = int()
        self.Name = name
        self.IdCount = 0

        DataObject = BlockData()
        DataObject.ReadHashes(levelObject.Name[-1], name+".txt", levelObject.Width)
        for picName in DataObject.blockDict:
            for blockPlace in DataObject.blockDict[picName]:
                block = Block(picName, blockPlace, name+"-"+str(self.IdCount))
                levelObject.AllBlocksGroup.add(block)
                self.IdCount += 1
        self.StageLength = DataObject.maxLength + 40
        del DataObject
        levelObject.Width += self.StageLength