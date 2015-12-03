import pygame
from Collisions import CollisionCheck
from Player import Player

class Stage(object):
    """See tahab olla üks 'stage', selle pikkus on mul vaikimisi 1000 pikslit."""
    
    StageName = str()
    StageLength = int()
    StageFrameShift = int()
    BlockGroup = pygame.sprite.Group()
    PlayerGroup = pygame.sprite.GroupSingle()
    #Checker = CollisionCheck()                                                 # An instance of an object that deals with collisions

    def __init__(self, name="nameless", length=1000):
        self.StageName = name
        self.StageLength = length
        self.PlayerGroup.add(Player())

    def DrawFrame(self, screen, background, X):
        screen.blit(background, (X,0))
        self.BlockGroup.draw(screen)
        self.PlayerGroup.draw(screen)

    def ShiftFrame(self):
        for box in self.BlockGroup:             
            box.rect.x -= 10                    # Do the shifting (left)
            if box.rect.x+40 < 0:
                box.kill()
        if self.PlayerGroup.sprite.rect.x < 100 and not self.PlayerGroup.sprite.Stuck:
            self.PlayerGroup.sprite.rect.x += 2

        if not self.PlayerGroup.sprite.Surface:
            self.PlayerGroup.sprite.rect.y += self.PlayerGroup.sprite.Gravi        # If we have nothing under our feet, move the Player 10 px up/down
        
        Collisions = pygame.sprite.spritecollide(self.PlayerGroup.sprite, self.BlockGroup, False)      # A list of Blocks that collide with the Player
        Leftmost, Walls, NotWalls = CollisionCheck.BuildWall(Collisions, self.PlayerGroup.sprite)
        if Walls:
            RECTS = list(b.rect for b in Walls)
            print("walls:",RECTS)
            self.PlayerGroup.sprite.rect.x = Leftmost - 40
            self.PlayerGroup.sprite.Surface = False
            self.PlayerGroup.Stuck = True
        else: 
            self.PlayerGroup.Stuck = False
        NotWalls = list(filter(   (lambda a: a.rect.y+40 >= self.PlayerGroup.sprite.rect.y+40 
                                       if (     self.PlayerGroup.sprite.Gravi > 0    )
                                       else a.rect.y <= self.PlayerGroup.sprite.rect.y
                                       ), 
                                    NotWalls
                                    )
                            )
        if NotWalls and not self.PlayerGroup.sprite.Surface and NotWalls[0].rect.x != Leftmost: 
            IDS = list(b.rect for b in NotWalls)
            print("notwalls:",IDS)
            Limit = CollisionCheck.BuildFloor(NotWalls, self.PlayerGroup.sprite)
            self.PlayerGroup.sprite.rect.y = Limit-40 if self.PlayerGroup.sprite.Gravi > 0 else Limit
            self.PlayerGroup.sprite.Surface = True
        elif (not NotWalls
              and self.PlayerGroup.sprite.Surface):

            self.PlayerGroup.sprite.rect.y += 1 if self.PlayerGroup.sprite.Gravi > 0 else -1
            collisions2 = pygame.sprite.spritecollide(self.PlayerGroup.sprite, self.BlockGroup, False)
            if not collisions2: 
                self.PlayerGroup.sprite.Surface = False
            self.PlayerGroup.sprite.rect.y -= 1 if self.PlayerGroup.sprite.Gravi > 0 else -1

