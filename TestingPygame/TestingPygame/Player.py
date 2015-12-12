import pygame
from BlockData import BlockData as dt
from os.path import join

class Player(pygame.sprite.Sprite):
    """Tegelane"""
    Gravi = 10
    Stuck = False
    Surface = False
    playerPics = {}
    PicNames = ["PlayerUa1.bmp","PlayerUa2.bmp","PlayerUa3.bmp", "PlayerDa1.bmp","PlayerDa2.bmp","PlayerDa3.bmp"]
    image_name = "PlayerUa1.bmp"

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(join("data/player","PlayerUa1.bmp"))

        for name in self.PicNames:
            img = pygame.image.load(join("data/player", name))
            img.set_colorkey((255,255,255))
            self.playerPics[name] = img

        self.rect = self.image.get_rect()
        self.image.set_colorkey((255, 255, 255))
        self.rect.x = 120
        self.rect.y = 80
        self.animCounter = 0   

    def FlipGravi(self):
        self.Surface = False
        self.Gravi *= -1
        name = self.image_name
        if name[-7] == "U":
            self.image_name = name.replace("U","D")
            self.image = self.playerPics[self.image_name]
        else: 
            self.image_name = name.replace("D","U")
            self.image = self.playerPics[self.image_name]

    def Animate(self): 
        self.animCounter += 1
        name = self.image_name
        if self.animCounter == 1:
            self.image_name = name.replace("1","2")
        elif self.animCounter == 3:
            self.image_name = name.replace("2","3")
        elif self.animCounter == 5:
            self.image_name = name.replace("3","2")
        elif self.animCounter == 7:
            self.image_name = name.replace("2","1")
            self.animCounter = 0
        self.image = self.playerPics[self.image_name]

            
            






