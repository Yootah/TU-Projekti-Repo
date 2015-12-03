import pygame
class Player(pygame.sprite.Sprite):
    """Tegelane"""
    Gravi = 10
    Stuck = False
    Surface = False
    Moved = False
    image_U = pygame.image.load("Player01U.bmp")
    image_U.set_colorkey((255, 255, 255))
    image_D = pygame.image.load("Player01D.bmp")
    image_D.set_colorkey((255, 255, 255))
    image_name = "Player01U.bmp"

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player01U.bmp")
        self.rect = self.image.get_rect()
        self.image.set_colorkey((255, 255, 255))
        self.rect.x = 100
        self.rect.y = 80    

    def FlipGravi(self):
        self.Surface = False
        self.Gravi *= -1
        if self.image_name == "Player01U.bmp":
            self.image = self.image_D
            self.image_name = "Player01D.bmp"
        else: 
            self.image = self.image_U
            self.image_name = "Player01U.bmp"




