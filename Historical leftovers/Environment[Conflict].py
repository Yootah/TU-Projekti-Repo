import Box, pygame
class EnvironmentBlock(object):
    """See tahab olla üks 'stage', selle pikkus on mul 1000 pikslit."""
    BlockName = "nameless"
    BlockLength = 1000
    BlockComponents = {}
    BlockGroup = True
    BlockFrameShift = 0
    PlayerGroup = True
    lowest_y = 99999999
    highest_y = 0

    def __init__(self, name="nameless", length=1000, components={}):
        self.BlockName = name
        self.BlockLength = length
        self.BlockComponents = components
        self.BlockGroup = pygame.sprite.Group()
        self.PlayerGroup = pygame.sprite.GroupSingle()

    def AddABox(self, singleBox):
        self.BlockComponents[box.Type + box.Id] = box.Parameters

    def UpdateDisplay(self):
        self.BlockGroup.update()

    def DrawFrame(self, screen, background, X):
        screen.blit(background, (X,0))
        self.BlockGroup.draw(screen)
        self.PlayerGroup.draw(screen)

    def ShiftFrame(self):
        #self.BlockFrameShift += 10
        
        plr = self.PlayerGroup.sprite
        for box in self.BlockGroup:
            box.rect.x -= 10
            if plr.Gravi > 0 and box.rect.y + 40  < (plr.rect.y) and (box.rect.y + 40) > self.highest_y:
                self.highest_y = box.rect.y + 40
                if pygame.sprite.spritecollide(plr, self.BlockGroup, False):
                    plr.rect.y = self.highest_y
            elif plr.Gravi < 0 and box.rect.y > (plr.rect.y + 40) and box.rect.y < self.lowest_y:
                self.lowest_y = box.rect.y
                if pygame.sprite.spritecollide(plr, self.BlockGroup, False):
                    plr.rect.y = self.lowest_y - 40
        plr.rect.y += plr.Gravi
        

        #I love my MJAU <3 :3
    #def PlayerJump(self):
    #    for plr in self.PlayerGroup:
    #        plr.FlipGravi()
    #        plr.rect.x += plr.Fwd
    #        plr.rect.y += plr.Gravi
        
