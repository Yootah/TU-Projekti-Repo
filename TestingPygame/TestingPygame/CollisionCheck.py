import pygame

class CollisionCheck(object):
    "Object that checks for player's various collisions" 
    
    def LostTheGame(player):
        "Returns True if the player is out of left/upper/lower border. "
        return True if player.rect.x <= -40 or player.rect.y <= -40 or player.rect.y >= 480 else False


    def LevelCleared(player):
        "Returns True is the player is out of right border (only possible when level is cleared). "
        return True if player.rect.x >= 1000 else False


    def BuildWall(collisions, player):
        """Returns a list of blocks that collide with player and line up vertically (leftmost x) as the closest wall to him. 
        Also returns the rest of the colliding blocks that are not walls but could be potential floors. 
        And if player collides with any deadly blocks, the Deaded status becomes True"""

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
        "Depending on current gravity constant returns either the lowest edge "
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


    def CheckWalls(levelObject, walls, leftmost):
        "See if player got stuck behind something. "
        if walls:
            levelObject.PlayerGroup.sprite.rect.x = leftmost - 40
            levelObject.PlayerGroup.sprite.Surface = False
            levelObject.PlayerGroup.sprite.Stuck = True
        else: 
            levelObject.PlayerGroup.sprite.Stuck = False


    def CheckFloors(levelObject, NotWalls, Leftmost):
        "See if the player hit a surface that stops it from falling. "

        player_y = levelObject.PlayerGroup.sprite.rect.y
        moving_down = levelObject.PlayerGroup.sprite.Gravi > 0
        block_is_floor = lambda block: (block.rect.y+40 >= player_y + 40 if moving_down else block.rect.y <= player_y) and block.rect.x != Leftmost
        NotWalls = list(filter(block_is_floor, NotWalls))

        if NotWalls and not levelObject.PlayerGroup.sprite.Surface: 
            Limit, levelObject.Deaded = self.BuildFloor(NotWalls, levelObject.PlayerGroup.sprite)
            levelObject.PlayerGroup.sprite.rect.y = Limit - 40 if moving_down else Limit
            levelObject.PlayerGroup.sprite.Surface = True

        elif not NotWalls and levelObject.PlayerGroup.sprite.Surface:
            levelObject.PlayerGroup.sprite.rect.y += 1 if moving_down else -1
            blocksTouchingFeet = pygame.sprite.spritecollide(levelObject.PlayerGroup.sprite, levelObject.AllBlocksGroup, False)
            if not blocksTouchingFeet: 
                levelObject.PlayerGroup.sprite.Surface = False
            else:
                for block in blocksTouchingFeet:
                    if block.deadly:
                        levelObject.Deaded = True
            levelObject.PlayerGroup.sprite.rect.y -= 1 if moving_down else -1