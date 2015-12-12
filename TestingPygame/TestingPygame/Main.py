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

grid = pygame.image.load("data/screens/whitegrid.bmp")
grid.set_colorkey((163,73,164))

pygame.init()
gameWindow = GameWindow()

level = gameWindow.Level
level.DrawFrame(gameWindow)

done = False
LoopCount = 0
t0 = time.time()

while done==False:

    if not (level.EndReached or level.Lost or level.Paused):  # <-----otherwise the level is through, no more stages.
        LoopCount += 1              #\
        if LoopCount % 3 == 0:      #  For the slow movement of the background image; might be completely unnecessary
            level.CurrentX -= 1     #/

    elif level.EndReached and not (level.Lost or level.Paused):
        if level.Cleared:
            print("CLEARED!")
            #done = True
            gameWindow.NextLevel(int(gameWindow.Level.Name[-1]))
            level = gameWindow.Level
            level.DrawFrame(gameWindow)
            # here goes the level transition or winning screen
    elif level.Lost and not level.Paused:
        print("LOST")
        #Losing screen here
        done = True

    if not (level.Lost or level.Cleared):
        if not level.Paused:
            level.ShiftFrame()
            if level.LevelShift + level.Width <= 1000 and not level.EndReached:
                level.EndReached = True
            level.DrawFrame(gameWindow)
        else:
            level.DrawFrame(gameWindow)
            gameWindow.DisplayPause()     



    for event in pygame.event.get():                                                                                         #\
            if event.type == pygame.QUIT:                                                                                    # \
                done = True                                                                                                  #  \
            if event.type == pygame.KEYDOWN:                                                                                 #    Looking out for key spamming, ragequitting etc (aka events).
               if event.key == pygame.K_SPACE and level.PlayerGroup.sprite.Surface and not level.Paused:                     # /
                    level.PlayerGroup.sprite.FlipGravi()                                                                     #/
               elif event.key == pygame.K_p:
                   if level.Paused:
                       level.Paused = False
                   else:
                       level.Paused = True


    t = time.time()                                                #\
    timechange = t - t0                                            # \
    if timechange < 0.035:                                         #    Making the game run smoothly both on slower & faster machines (aka frame timer)
        pygame.time.delay(35 - round((timechange)*1000))           #  /
    pygame.display.flip()                                          # /   
    t0 = time.time()                                               #/

pygame.quit()