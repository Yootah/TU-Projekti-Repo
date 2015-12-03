"""Note to self:
    NEVER use frames as a timer. """

import pygame
import time
from Environment import Stage
from SpritelikeBox import SpriteBox
from Player import Player
from TextDocHandler import BlockData
from Level import Level


pygame.init()

H = 480
W = 1000
IdCount = 0
pygameWindow = pygame.display.set_mode( (W, H) )
#pygame.display.set_caption("TestingPygame")
#background = pygame.image.load("bckg.bmp")
#pygameWindow.fill( (0,255,0) )
#X = 0
#pygameWindow.blit(background, (X,0))

listOfStages = []
environment = Stage("01",IdCount)
IdCount = environment.IDcount
listOfStages.append(environment)
environment = Stage("02",IdCount)
IdCount = environment.IDcount
listOfStages.append(environment)



level = Level(pygameWindow, "bckg.bmp", "Level 1", listOfStages) 


#for tsm in range(200): #tsm = tsüklimuutuja
#    IdCount += 1
#    boxSprite = SpriteBox((255,0,0),40,40, IdCount)
#    boxSprite.image = pygame.image.load("Box01U.bmp")
#    boxSprite.rect.x = tsm * 40
#    boxSprite.rect.y = 0
#    environment.BlockGroup.add(boxSprite)

#    IdCount += 1
#    boxSprite = SpriteBox((255,0,0),40,40, IdCount)
#    boxSprite.image = pygame.image.load("Box01D.bmp")
#    boxSprite.rect.x = tsm * 40
#    boxSprite.rect.y = 440
#    environment.BlockGroup.add(boxSprite)

blockData = BlockData()
#blockData.ReadFile("TestingBlockPlacement.txt")
blockData.ReadHashes("TestingHashPlacement.txt")


for picName in blockData.blockDict.keys():
    for blockPlace in blockData.blockDict[picName]:
        IdCount += 1
        boxSprite = SpriteBox((255,0,0),40,40, IdCount)
        boxSprite.image = pygame.image.load(picName)
        if picName == "tree.bmp":
            boxSprite.image.set_colorkey((163,73,164))
        boxSprite.rect.x = blockPlace[0]
        boxSprite.rect.y = blockPlace[1]
        environment.BlockGroup.add(boxSprite)


done = False
Freeze = False
LoopCount = 0
t0 = time.time()

while done==False:

    if not Freeze:  # <-----means the level is through, no more stages.
        level.PlayerGroup.sprite.Moved = False      # <---the player has not been moved yet...

        LoopCount += 1              #\
        if LoopCount % 3 == 0:      #  For the slow movement of the background image; might be completely unnecessary
            level.CurrentX -= 1     #/


        level.CurrentStage.ShiftFrame(level.PlayerGroup.sprite)     #\
        if level.AwaitingStages:                                    # \
            for stg in level.AwaitingStages:                        #  \
                stg.ShiftFrame(level.PlayerGroup.sprite)            #   All the shifting of coordinates (boxes & player); also drawing the entire frame (from inside the level obj)
        level.DrawFrame(pygameWindow)                               # /
        level.LevelShift -= 10                                      #/


        if level.LevelShift + level.Width <= 0:                     #\
            Freeze = True                                           # \
        else:                                                       #  \
            if level.CurrentStage.EndReached:                       #    Checking if any edge is reached - either that of a stage or of the entire level
                level.NextStage                                     #  /
            if level.CurrentStage.OutOfBorder:                      # /
                level.CurrentStage = level.AwaitingStages.pop(0)    #/


    for event in pygame.event.get():                                                                    #\
            if event.type == pygame.QUIT:                                                               # \
                done = True                                                                             #  \
            if event.type == pygame.KEYDOWN and level.CurrentStage.PlayerGroup.sprite.Surface:          #    Looking out for key spamming, ragequitting etc events.
               if event.key == pygame.K_SPACE:                                                          #  /
                    print("\n  *SPACE*")                                                                # /
                    level.CurrentStage.PlayerGroup.sprite.FlipGravi()                                   #/

    t = time.time()                                                #\
    timechange = t - t0                                            # \
    if timechange < 0.04:                                          #    Making the game run smoothly both on slower & faster machines (aka frame timer)
        pygame.time.delay(40 - round((timechange)*1000))           #  /
    pygame.display.flip()                                          # /   
    t0 = time.time()                                               #/

pygame.quit()