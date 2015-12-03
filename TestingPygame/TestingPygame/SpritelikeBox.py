import pygame

class SpriteBox(pygame.sprite.Sprite):
    """See on õige klass kasti jaoks"""

    Id = int()
    def __init__(self, color, width, height, id):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.Id = id
