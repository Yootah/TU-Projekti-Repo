import pygame

class SpriteBox(pygame.sprite.Sprite):
    """See on õige klass kasti jaoks"""

    def __init__(self, name, coords, id):
        super().__init__()
        self.Id = id
        self.image = pygame.image.load(name)
        self.rect = self.image.get_rect()
        self.rect.x = coords[0]
        self.rect.y = coords[1]
        self.image.set_colorkey((163,73,164))