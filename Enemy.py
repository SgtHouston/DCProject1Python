# Make a class Enemy and decide what I can pull out of main.
import random

class Enemy():
    def __init__(self, enemyImg, enemyX, enemyY, enemyX_change, enemyY_change, i):
        self.enemyImg = enemyImg
        self.enemyX = enemyX
        self.enemyY = enemyY
        self.enemyX_change = enemyX_change
        self.enemyY_change = enemyY_change
        self.i = i

#     def enemy(x, y, i):
#     # enemy x,y coordinates are passed in as well as the iteration 
#     # of the enemy on the list.
#     # draw an image of the enemy on the surface of our 
#     # game window.  First value is enemy image iteration, the second and 
#     # third are a pair of coordinates
#         screen.blit(enemyImg[i], (x, y))




# # randomize x,y axis values by importing random module and
#     # providing a range of coordinates that represent the borders on the 
#     # x-axis and the other side of the board on the y.
#     enemyX.append(random.randint(0, 736))
#     enemyY.append(random.randint(20, 150))
#     # how many pixels the enemy will move per loop on the x-axis.
#     enemyX_change.append(3)
#     # enemy will not only move on the x-axis, but will come down towards 
#     # the player on the y-axis once it hits a set border.  To enable this, 
#     # the enemy will also have an enemyY_change, unlike the player
#     enemyY_change.append(40) 



