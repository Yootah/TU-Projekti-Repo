import pygame
from Player import *
from Block import *
from CollisionCheck import *
from Stage import *
from BlockData import BlockData as dt
from os.path import join
from os import getcwd

class Level(object):
    "A level. Contains a player and lots blocks. Gets deleted/re-created when we want to restart or move on to the next level. "
   
    def __init__(self, window, imageName = "bckg1.bmp", name = "Level 1"):
        "Level constructor. "

        # Player belongs to the entire level
        self.PlayerGroup = pygame.sprite.GroupSingle()

        # Collision check has level-wide scope
        self.AllBlocksGroup = pygame.sprite.Group()

        self.Bckgr = pygame.image.load(join("data/levels", name[-1], imageName))
        self.Name = name
        self.PlayerGroup.add(Player())

        self.Width = int()
        self.LevelShift = int()
        self.CurrentX = int()

        self.EndReached = False
        self.Cleared = False
        self.Lost = False
        self.Paused = False
        self.Deaded = False
                
        for n in range(1,7):
            s = Stage(str(n).rjust(2, "0"), self)
            del s


    def DrawFrame(self, screen):
        "Draws things after moving. "
        screen.Window.blit(self.Bckgr, (self.CurrentX,0))
        self.AllBlocksGroup.draw(screen.Window)
        self.PlayerGroup.draw(screen.Window)
        

    def ShiftFrame(self): 
        "What the method name says. "

        self.MoveThings()
        
        collisions = pygame.sprite.spritecollide(self.PlayerGroup.sprite, self.AllBlocksGroup, False)
        Leftmost, Walls, NotWalls, self.Deaded = CollisionCheck.BuildWall(collisions, self.PlayerGroup.sprite)
        CollisionCheck.CheckWalls(self, Walls, Leftmost)
        CollisionCheck.CheckFloors(self, NotWalls, Leftmost)
        
        if self.Deaded:                         self.Lost = True
        if not self.Lost:                       self.Lost = CollisionCheck.LostTheGame(self.PlayerGroup.sprite)
        if not (self.Cleared or self.Lost):     self.Cleared = CollisionCheck.LevelCleared(self.PlayerGroup.sprite)


    def MoveThings(self):
        "Change the positions of player and blocks. "

        self.PlayerGroup.sprite.Animate()              # play the running animation

        gravi = self.PlayerGroup.sprite.Gravi
        player_x = self.PlayerGroup.sprite.rect.x
        player_stuck = self.PlayerGroup.sprite.Stuck
        player_onSurface = self.PlayerGroup.sprite.Surface
        
        if not player_onSurface:
            self.PlayerGroup.sprite.rect.y += gravi     # player falls if nothing supports him

        if not self.EndReached:
            for block in self.AllBlocksGroup:            # move every block backward 
                block.rect.x -= 10                   
                if block.rect.x + 40 <= 0:               # delete blocks that run out of borders
                    block.kill()
            self.LevelShift -= 10                        # memorize the amount of movement

            if player_x < 120 and not player_stuck:         # if player got stuck but got out, start slowly moving him forward until start position is restored
                self.PlayerGroup.sprite.rect.x += 2
        else:
            self.PlayerGroup.sprite.rect.x += 10            # if the level has nowhere else to move, freeze it and move the player forward instead

    






        


