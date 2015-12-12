import pygame
from Player import *
from Block import *
from CollisionCheck import *
from Stage import *
from BlockData import BlockData as dt
from os.path import join
from os import getcwd

class Level(object):
    """..."""
   
    def __init__(self, window, imageName = "bckg.bmp", name = "Level 1"):
        """
        nop. 
        """
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
                
        for n in range(1,5):
            s = Stage(str(n).rjust(2, "0"), self)
            del s


    def DrawFrame(self, screen):
        screen.Window.blit(self.Bckgr, (self.CurrentX,0))
        self.AllBlocksGroup.draw(screen.Window)
        self.PlayerGroup.draw(screen.Window)

        

    def ShiftFrame(self): 

        # Shifting all blocks on screen
        self.PlayerGroup.sprite.Animate()

        if not self.EndReached:

            for block in self.AllBlocksGroup:             
                block.rect.x -= 10                   
                if block.rect.x + 40 <= 0:
                    block.kill()

            self.LevelShift -= 10

            if self.PlayerGroup.sprite.rect.x < 120 and not self.PlayerGroup.sprite.Stuck:
                self.PlayerGroup.sprite.rect.x += 2

        elif self.EndReached:
            self.PlayerGroup.sprite.rect.x += 10

        if not self.PlayerGroup.sprite.Surface:
            self.PlayerGroup.sprite.rect.y += self.PlayerGroup.sprite.Gravi        # If we have nothing under our feet, move the Player 10 px up/down
        
        collisions = pygame.sprite.spritecollide(self.PlayerGroup.sprite, self.AllBlocksGroup, False)      # A list of Blocks that collide with the Player
        Leftmost, Walls, NotWalls, Deaded = CollisionCheck.BuildWall(collisions, self.PlayerGroup.sprite)
        
        if Walls:
            RECTS = list((b.rect.x, b.rect.y) for b in Walls)
            #print("walls:",RECTS)
            self.PlayerGroup.sprite.rect.x = Leftmost - 40
            self.PlayerGroup.sprite.Surface = False
            self.PlayerGroup.sprite.Stuck = True
        else: 
            self.PlayerGroup.sprite.Stuck = False

        NotWalls = list(filter(   (lambda a: a.rect.y+40 >= self.PlayerGroup.sprite.rect.y+40 
                                       if (     self.PlayerGroup.sprite.Gravi > 0    )
                                       else a.rect.y <= self.PlayerGroup.sprite.rect.y
                                       ), 
                                    NotWalls
                                    )
                            )
        if (NotWalls 
            and not self.PlayerGroup.sprite.Surface 
            and NotWalls[0].rect.x != Leftmost): 

            IDS = list((b.rect.x, b.rect.y) for b in NotWalls)
            #print("notwalls:",IDS)
            Limit, Deaded = CollisionCheck.BuildFloor(NotWalls, self.PlayerGroup.sprite)
            self.PlayerGroup.sprite.rect.y = Limit-40 if self.PlayerGroup.sprite.Gravi > 0 else Limit
            self.PlayerGroup.sprite.Surface = True

        elif (not NotWalls
              and self.PlayerGroup.sprite.Surface):
            self.PlayerGroup.sprite.rect.y += 1 if self.PlayerGroup.sprite.Gravi > 0 else -1
            collisions2 = pygame.sprite.spritecollide(self.PlayerGroup.sprite, self.AllBlocksGroup, False)
            if not collisions2: 
                self.PlayerGroup.sprite.Surface = False
            self.PlayerGroup.sprite.rect.y -= 1 if self.PlayerGroup.sprite.Gravi > 0 else -1
        
        if Deaded: self.Lost = True

        if not self.Lost:
            self.Lost = CollisionCheck.LostTheGame(self.PlayerGroup.sprite)
        if not self.Cleared:
            self.Cleared = CollisionCheck.LevelCleared(self.PlayerGroup.sprite)

        

    






        


