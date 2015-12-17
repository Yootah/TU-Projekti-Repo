import pygame
from FunctionalScreen import *

class DeathScreen(FunctionalScreen):
    """description of class"""

    def __init__(self, window):
        """"""
        return super().__init__(window, "end", 500, 300, """LOL! You died. Press SPACE to restart the level""")
