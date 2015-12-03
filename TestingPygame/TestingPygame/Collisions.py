import pygame

class CollisionCheck(object):
    """Object that checks for player's various collisions"""

    def BuildWall(collisions, player):
        """"""
        left = 1000
        wall = []
        notWalls = []
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
                elif box.rect.x == left:
                    wall.append
        return left, wall, notWalls

    def BuildFloor(notWalls, player):
        """"""
        floors = []
        g = player.Gravi
        if g > 0:
            # Moving down
            highest = 480
            for box in notWalls:
                if box.rect.y < highest:
                    floors = [box]
                    highest = box.rect.y
                elif box.rect.y == highest:
                    floors.append(box)
            return highest
        else:
            # Moving up
            lowest = 0
            for box in notWalls:
                if box.rect.y+40 > lowest:
                    floors = [box]
                    lowest = box.rect.y+40
                elif box.rect.y+40 == lowest:
                    floors.append(box)
            return lowest
           
                    