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
pygameWindow = pygame.display.set_mode( (W, H) )
pygame.display.set_caption("TestingPygame")

level = Level(pygameWindow, "bckg.bmp", "Level 1") 
level.DrawFrame(pygameWindow)

done = False
Freeze = False
LoopCount = 0
t0 = time.time()

while done==False:

    if not level.EndReached:  # <-----otherwise the level is through, no more stages.
        LoopCount += 1              #\
        if LoopCount % 3 == 0:      #  For the slow movement of the background image; might be completely unnecessary
            level.CurrentX -= 1     #/


    level.ShiftFrame()
    level.DrawFrame(pygameWindow)

    #print(level.LevelShift, level.Width, level.LevelShift + level.Width)
    
    if level.LevelShift + level.Width <= 1000 and not level.EndReached:
        #print("STOP!")
        level.EndReached = True

    for event in pygame.event.get():                                                                    #\
            if event.type == pygame.QUIT:                                                               # \
                done = True                                                                             #  \
            if event.type == pygame.KEYDOWN and level.PlayerGroup.sprite.Surface:                       #    Looking out for key spamming, ragequitting etc (aka events).
               if event.key == pygame.K_SPACE:                                                          #  /
                    #print("\n  *SPACE*")                                                                # /
                    level.PlayerGroup.sprite.FlipGravi()                                   #/

    t = time.time()                                                #\
    timechange = t - t0                                            # \
    if timechange < 0.04:                                          #    Making the game run smoothly both on slower & faster machines (aka frame timer)
        pygame.time.delay(40 - round((timechange)*1000))           #  /
    pygame.display.flip()                                          # /   
    t0 = time.time()                                               #/

pygame.quit()