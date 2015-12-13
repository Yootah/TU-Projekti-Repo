import pygame
from FunctionalScreen import *

class StartScreen(FunctionalScreen):
    """description of class"""

    def __init__(self, window):
        """"""
        return super().__init__(window, "start", 562, 300, "Press SPACE to start")

