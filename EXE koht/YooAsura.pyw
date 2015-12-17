import pygame
import time
from Stage import *
from Block import *
from Player import *
from BlockData import BlockData
from Level import *
from GameWindow import *
from DeathScreen import *
from StartScreen import *
from WinScreen import *

pygame.init()
gameWindow = GameWindow()
level = gameWindow.Level

done = False
LoopCount = 0
t0 = time.time()

gameWindow.Window.blit(level.Bckgr,(0,0))
strtscrn = StartScreen(gameWindow)


while done==False:

    if gameWindow.StartScreen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True 
            if event.type == pygame.KEYDOWN:                                                                                 
                if event.key == pygame.K_SPACE:
                    gameWindow.StartScreen = False
                    del strtscrn
                    level.DrawFrame(gameWindow)
                elif event.key == pygame.K_ESCAPE:
                    done = True

    if not (level.EndReached or level.Lost or level.Paused or gameWindow.StartScreen):
        LoopCount += 1              #\
        if LoopCount % 3 == 0:      #  For the slow movement of the background image; purely cosmetical, might prove completely unnecessary
            level.CurrentX -= 1     #/

    elif level.EndReached and not (level.Lost or level.Paused or gameWindow.StartScreen or gameWindow.WinScreen):
        # When the level can't move backward anymore, the player starts to move forward

        if level.Cleared:
            if level.Name[-1] != "4":
                # Here we clear a level that is not the last one
                gameWindow.NextLevel(int(gameWindow.Level.Name[-1]))
                level = gameWindow.Level
                level.DrawFrame(gameWindow)
            else:
                # Here we win the game
                wnscrn = WinScreen(gameWindow)
                gameWindow.WinScreen = True

    elif level.Lost and not (level.Paused or gameWindow.StartScreen):
        # Here we lost (fell off or hit something deadly) 
        gameWindow.DeathScreen = True
        dthscrn = DeathScreen(gameWindow)

    if not (level.Lost or level.Cleared or gameWindow.StartScreen or level.Paused):
        # Here we are in the middle of the game without anything fatal happening
        level.ShiftFrame()
        if level.LevelShift + level.Width <= 1000 and not level.EndReached:
            # Here the level has reached its endpoint and freezes. 
            level.EndReached = True
        level.DrawFrame(gameWindow)

    for event in pygame.event.get():                                                                                                    #
            if event.type == pygame.QUIT:                                                                                               #
                # Closing the window                                                                                                    # 
                done = True                                                                                                             #  
            elif event.type == pygame.KEYDOWN:                                                                                          #
                                                                                                                                        #    Looking out for key spamming, ragequitting etc (aka events).
               if event.key == pygame.K_SPACE and level.PlayerGroup.sprite.Surface and not (level.Paused or gameWindow.WinScreen):      #  
                    # Space pressed during game (for jump)                                                                              # 
                   level.PlayerGroup.sprite.FlipGravi()                                                                                 #
                                                                                                    
               elif event.key == pygame.K_p and not (level.Lost or gameWindow.StartScreen):
                   # Pause key pressed
                   if level.Paused:
                       level.Paused = False
                   else:
                       level.DrawFrame(gameWindow)
                       gameWindow.DisplayPause() 
                       level.Paused = True

               elif gameWindow.DeathScreen and event.key == pygame.K_SPACE  and not level.Paused:
                   # Here we chose to restart the level after losing
                   gameWindow.DeathScreen = False
                   del dthscrn
                   gameWindow.RestartLevel(int(gameWindow.Level.Name[-1]))
                   level = gameWindow.Level
                   level.DrawFrame(gameWindow)

               elif gameWindow.WinScreen and event.key == pygame.K_SPACE and not level.Paused: 
                   # Here we won the game and decided to play again
                   del wnscrn
                   gameWindow.WinScreen = False
                   gameWindow.NextLevel(0)
                   level = gameWindow.Level
                   level.DrawFrame(gameWindow)

               elif event.key == pygame.K_ESCAPE:
                   # Here we chose to exit the game via Esc key
                   done = True


    t = time.time()                                                #\
    timechange = t - t0                                            # \
    if timechange < 0.035:                                         #    Making the game run smoothly both on slower & faster machines (aka frame timer)
        pygame.time.delay(35 - round((timechange)*1000))           #  /
    pygame.display.flip()                                          # /   
    t0 = time.time()                                               #/

pygame.quit()
