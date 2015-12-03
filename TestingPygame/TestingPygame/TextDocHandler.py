class BlockData(object):
    """description of class"""
    import re
    blockDict = {}
    regexName = re.compile('.bmp$')
    regexNumber = re.compile(r'\d \d')
    worldEnvi = {'#': 'Box01D.bmp' }
    maxLength = 0

    def ReadFile(self, filename): 
        """Gimme a file and imma make u a blockDict. """
        named = False
        file = open(filename)
        for row in file:
            if self.regexName.search(row.strip()):
                imageName = row.strip()
                self.blockDict[imageName] = []
            elif self.regexNumber.search(row.strip()):
                self.blockDict[imageName].append(tuple(int(x) for x in row.strip().split()))
        file.close()

    def ReadHashes(self, filename):
        height = -1
        length = -1
        file = open(filename)
        for row in file:
            print(row)
            print(row.strip())
            height +=1
            for piece in row:
                length +=1
                if piece in self.worldEnvi:
                    if length > self.maxLength:
                        self.maxLength = length
                    piece_name = self.worldEnvi[piece]
                    piece_x = 40*length
                    piece_y = 40*height
                    print(piece, length, height)
                    if piece_name in self.blockDict:
                        if (piece_x, piece_y) not in self.blockDict[piece_name]:
                            self.blockDict[piece_name].append((piece_x, piece_y))
                    else:
                        self.blockDict[piece_name] = [(piece_x, piece_y)]
            length = -1
        




