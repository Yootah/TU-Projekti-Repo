from os import getcwd
from os.path import join

class BlockData(object):
    """description of class"""

    worldEnvi = {'G': 'Grass1U.bmp', 
                 'g': 'Grass1D.bmp', 
                 "I": "Ice1U.bmp", 
                 "i": "Ice2U.bmp", 
                 "t": "tree.bmp", 
                 "S": "spikes.bmp",
                 "s": "spikesD.bmp"}

    def __init__(self):
        self.maxLength = 0
        self.blockDict = {}

    def ReadHashes(self, lev, filename, n):
        if filename == "01.txt":
            print("OK")
        height = -1
        length = -1
        file = open(join("data/levels", lev, filename))
        for row in file:
            height +=1
            for piece in row:
                length +=1
                if piece in self.worldEnvi:
                    piece_name = self.worldEnvi[piece]
                    piece_x = 40*length + n
                    piece_y = 40*height
                    if 40*length > self.maxLength:
                        self.maxLength = 40*length
                    if piece_name in self.blockDict:
                        if (piece_x, piece_y) not in self.blockDict[piece_name]:
                            self.blockDict[piece_name].append((piece_x, piece_y))
                    else:
                        self.blockDict[piece_name] = [(piece_x, piece_y)]
            length = -1
        




