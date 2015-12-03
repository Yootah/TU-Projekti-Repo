import pygame
from Collisions import CollisionCheck
from Player import Player
from TextDocHandler import BlockData
from SpritelikeBox import SpriteBox

class Stage(object):
    """A stage in a level. """
    
    StageID = str()
    StageLength = int()
    StageShift = 0
    BlockGroup = pygame.sprite.Group()
    #PlayerGroup = pygame.sprite.GroupSingle()                                            # An instance of an object that deals with collisions
    EndReached = False
    OutOfBorder = False
    IDcount = int()

    def __init__(self, name, idCount):
        self.StageID = name                   # max_StageLength == furthest_box.rect.x+40
        #self.PlayerGroup.add(Player())
        DataObject = BlockData()
        DataObject.ReadHashes(name+".txt")
        for picName in DataObject.blockDict.keys():
            for blockPlace in DataObject.blockDict[picName]:
                idCount += 1
                print("Current IDcount:", idCount)
                block = SpriteBox((255,0,0),40,40, idCount)
                block.image = pygame.image.load(picName)
                if picName == "tree.bmp":
                    block.image.set_colorkey((163,73,164))
                block.rect.x = blockPlace[0]
                block.rect.y = blockPlace[1]
                self.BlockGroup.add(block)
        self.StageLength = DataObject.maxLength + 40
        del DataObject
        self.IDcount = idCount

    def ShiftFrame(self, player):
        if self.StageLength + self.StageShift > 0:
            for box in self.BlockGroup:             
                box.rect.x -= 10                    # Do the shifting (left)
                if box.rect.x+40 < 0:
                    box.kill()
            self.StageShift -= 10
        else:
            self.OutOfBorder = True

        if player.rect.x < 100 and not player.Stuck:
            player.rect.x += 2

        if not player.Surface and not player.Moved:
            player.rect.y += player.Gravi        # If we have nothing under our feet, move the Player 10 px up/down
            player.Moved = True
        
        Collisions = pygame.sprite.spritecollide(player, self.BlockGroup, False)      # A list of Blocks that collide with the Player
        Leftmost, Walls, NotWalls = CollisionCheck.BuildWall(Collisions, player)
        
        if Walls:
            RECTS = list((b.rect.x, b.rect.y) for b in Walls)
            print("walls:",RECTS)
            player.rect.x = Leftmost - 40
            player.Surface = False
            player.Stuck = True
        else: 
            player.Stuck = False

        NotWalls = list(filter(   (lambda a: a.rect.y+40 >= player.rect.y+40 
                                       if (     player.Gravi > 0    )
                                       else a.rect.y <= player.rect.y
                                       ), 
                                    NotWalls
                                    )
                            )
        if (NotWalls 
            and not player.Surface 
            and NotWalls[0].rect.x != Leftmost): 

            IDS = list((b.rect.x, b.rect.y) for b in NotWalls)
            print("notwalls:",IDS)
            Limit = CollisionCheck.BuildFloor(NotWalls, player)
            player.rect.y = Limit-40 if player.Gravi > 0 else Limit
            player.Surface = True
        elif (not NotWalls
              and player.Surface):
            player.rect.y += 1 if player.Gravi > 0 else -1
            collisions2 = pygame.sprite.spritecollide(player, self.BlockGroup, False)
            if not collisions2: 
                player.Surface = False
            player.rect.y -= 1 if player.Gravi > 0 else -1
    
    def SetBoxesX(self):
        """Use when with stages indexed greater than 0 (the first stage in level is handled differently). 
        X is related to current frameshift. """
        for box in self.BlockGroup: 
            box.rect.x += 1000


