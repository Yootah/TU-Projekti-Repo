import pygame

class CollisionCheck(object):
    """Object that checks for player's various collisions"""

    def BuildWall(collisions, player):
        """"""
        left = 1000
        wall = []
        notWalls = []
        deaded = False #I know right, retarded English
        for box in collisions: 
            clip = player.rect.clip(box.rect)
            if (clip.width > clip.height 
                or (clip.width == clip.height 
                    and clip.width <= 10 
                    and clip.height <= 10) 
                or (clip.height == 10 
                    and clip.width in range(2, 8))):

                notWalls.append(box)

            else:
                if box.rect.x < left:
                    left = box.rect.x
                    wall = [box]
                    if box.deadly:
                        deaded = True
                elif box.rect.x == left:
                    wall.append
                    if box.deadly:
                        deaded = True
        return left, wall, notWalls, deaded

    def BuildFloor(notWalls, player):
        """"""
        floors = []
        deaded = False
        g = player.Gravi
        if g > 0:
            # Moving down
            highest = 480
            for box in notWalls: 
                if box.rect.y < highest:
                    floors = [box]
                    highest = box.rect.y
                    if box.deadly:
                        deaded = True
                elif box.rect.y == highest:
                    floors.append(box)
                    if box.deadly:
                        deaded = True
            return highest, deaded
        else:
            # Moving up
            lowest = 0
            for box in notWalls:
                if box.rect.y+40 > lowest:
                    floors = [box]
                    lowest = box.rect.y+40
                    if box.deadly:
                        deaded = True
                elif box.rect.y+40 == lowest:
                    floors.append(box)
                    if box.deadly:
                        deaded = True
            return lowest, deaded

    def LostTheGame(player):
        return True if player.rect.x <= -40 or player.rect.y <= -40 or player.rect.y >= 480 else False

    def LevelCleared(player):
        return True if player.rect.x >= 1000 else False