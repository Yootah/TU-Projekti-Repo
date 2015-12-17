import pygame
from FunctionalScreen import *

class WinScreen(FunctionalScreen):
    """description of class"""

    def __init__(self, window):
        """"""
        return super().__init__(window, "win", 529, 300, "      You won! Press SPACE to play again")
