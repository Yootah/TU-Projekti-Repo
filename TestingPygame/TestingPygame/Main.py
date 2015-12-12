"""Note to self:
    NEVER use frames as a timer. """

import pygame
import time
from Stage import *
from Block import *
from Player import *
from BlockData import BlockData
from Level import *
from GameWindow import *


pygame.init()
gameWindow = GameWindow()

level = gameWindow.Level
level.DrawFrame(gameWindow)

done = False
LoopCount = 0
t0 = time.time()

while done==False:

    if not (level.EndReached or level.Lost):  # <-----otherwise the level is through, no more stages.
        LoopCount += 1              #\
        if LoopCount % 3 == 0:      #  For the slow movement of the background image; might be completely unnecessary
            level.CurrentX -= 1     #/
    elif level.EndReached:
        if level.Cleared:
            print("CLEARED!")
            done = True
            # here goes the level transition or winning screen
    elif level.Lost:
        print("LOST")
        #Losing screen here
        done = True

    if not (level.Lost or level.Cleared):
        level.ShiftFrame()
        level.DrawFrame(gameWindow)
        
        if level.LevelShift + level.Width <= 1000 and not level.EndReached:
            level.EndReached = True

        for event in pygame.event.get():                                                                    #\
                if event.type == pygame.QUIT:                                                               # \
                    done = True                                                                             #  \
                if event.type == pygame.KEYDOWN and level.PlayerGroup.sprite.Surface:                       #    Looking out for key spamming, ragequitting etc (aka events).
                   if event.key == pygame.K_SPACE:                                                          #  /
                        #print("\n  *SPACE*")                                                               # /
                        level.PlayerGroup.sprite.FlipGravi()                                                #/


    t = time.time()                                                #\
    timechange = t - t0                                            # \
    if timechange < 0.035:                                          #    Making the game run smoothly both on slower & faster machines (aka frame timer)
        pygame.time.delay(35 - round((timechange)*1000))           #  /
    pygame.display.flip()                                          # /   
    t0 = time.time()                                               #/

pygame.quit()