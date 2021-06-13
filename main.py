# Steps taken
# 1. Create game window
# 2. Title, Logo, and Background
# 3. Add Images
# 4. Player Movement by increasing/decreasing pixel coordinate value in every loop
# 5. Attach pixel increase/decrease to keyboard input
# 6. Add boundaries to the board
# 7. Create an enemy
# 8. Movement mechanics of the enemy
# 9. Add a background image
# 10. Create Bullet




# Import Pygame module
import pygame
# Import random module to randomize enemy x,y axis values
import random
# Intitialize the pygame
pygame.init()     




# # Create the screen.  Pass in 1. width *n/800--> and 2. height *n/600 v
# # arguments into the parameters
screen = pygame.display.set_mode ((800, 600))
# Set the background
background = pygame.image.load('Dimensional Tear.png')
# Set the Title of your pygame display 
pygame.display.set_caption(" ⚡️ 👽 ⭐︎ 👉 Dimensional Defender 👈 ⭐︎ 👽 ⚡️ ")
# Set the Icon of your pygame display.  Use png file from Flaticon.com at 32x32px  
icon = pygame.image.load('enemy.png')
pygame.display.set_icon(icon)




# Player
# Image 64 x 64px
playerImg = pygame.image.load('player.png') 
playerX = 368  
playerY = 516
playerX_change = 0 
def player(x, y):
    # draw an image of the player on the surface of our 
    # game window.  First value is player image, the second and 
    # third are a pair of coordinates
    screen.blit(playerImg, (x, y))




# Enemy
enemyImg = pygame.image.load('enemy.png')
# randomize x,y axis values by importing random module and
# providing a range of coordinates that represent the borders on the x-axis and the 
# other side of the board on the y.
enemyX = random.randint(0, 736)
enemyY = random.randint(20, 150)
# how many pixels the enemy will move per loop on the x-axis.
enemyX_change = 3 
# enemy will not only move on the x-axis, but will come down towards the player on the
# y-axis once it hits a set border.  To enable this, the enemy will also have an 
# enemyY_change, unlike the player
enemyY_change = 40  
def enemy(x, y):
    # draw an image of the enemy on the surface of our 
    # game window.  First value is enemy image, the second and 
    # third are a pair of coordinates
    screen.blit(enemyImg, (x, y))




# Bullet
# Image 32 x 32px
bulletImg = pygame.image.load('LaserBeam.png') 
bulletX = 0  
# bulletY value the same as player's nose
bulletY = 516
# Bullet_X wont change, as the bullet will never move side to side
bulletX_change = 0 
# Bullet speed 
bulletY_change = 10 
# Ready - You can't see the bullet on the screen
# Fire - The bullet is currently in motion
bullet_state = 'ready'
def fire_bullet(x, y):
    global bullet_state
    bullet_state = 'fire' 
    # X coordinate + 16 so that the bullet is centered halfway through the player (32px/2 = 16)
    # Y coordinate + 10 so thaty the bullet appears somewhat "above" the player when executed
    # screen.blit makes the bullet appear on the screen 
    screen.blit(bulletImg, (x + 16, y + 10))
    


# Game Loop
# Infinite loop to capture game events  
running = True
while running:
    # Change the background of the window using screen.fill.  
    # This takes 3 values, R,G,B or Red, Greed, and Blue.  
    # This is positioned so it runs in the infinite while 
    # loop while the game runs.  Range is 0 - 255 for each color.
    screen.fill((150, 0, 255)) 

    # Set the background
    screen.blit(background, (0, 0))
    background = pygame.image.load('Dimensional Tear.png')
    
    # loop though all of the events happening inside
    # the game window
    for event in pygame.event.get():
        # If close button has been pressed,
        if event.type == pygame.QUIT:
            # Quit the program window
            running = False

        # Keyboard
        # If keystroke is pressed, check whether it is right or left.
        # Keystrokes are pygame events that will be captured and 
        # looped through.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                # when left arrow key is pressed, playerX_change 
                # variable moves player n pixels toward origin on the x-axis.
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                # when right arrow is pressed, playerX_change variable 
                # moves player n pixels away from the origin on the x-axis
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                # when spacebar is pressed, fire bullet function is called and 
                # bullet state is switched to fire. 
                fire_bullet(playerX, bulletY)
        
        if event.type == pygame.KEYUP:
                # when key is released, PlayerX_change variable changes 
                # to zero, stopping player_X axis movement.
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0  

    # Player Movement           
    playerX += playerX_change
    # Set boundaries for playerX, not allowing the 64-pixel icon to go beyond
    # 0 on the left or 736 on the right (800 pixel screen size - 64 pixel icon) 
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Enemy Movement
    # To make sure that our enemy is always on the screen
    # we call our enemy function in the infinite while loop
    enemyX += enemyX_change
    # Set boundaries for enemyX, not allowing the 64-pixel icon to go beyond
    # 0 on the left or 736 on the right (800 pixel screen size - 64 pixel icon)  
    if enemyX <= 0:
        # When X-value has decreased all the way to zero, we begin increasing it.
        # sending the enemy the other direction with every loop 
        enemyX_change = 3
        enemyY += enemyY_change
    elif enemyX >= 736:
        # When X-value has increased all the way to 736, we begin decreasing it by 
        # the movement speed value, sending the enemy the other direction with every loop
        enemyX_change = -3
        enemyY += enemyY_change

    # Bullet movement
    if bullet_state is 'fire':
        fire_bullet(playerX, bulletY)
        bulletY -= bulletY_change


    # To make sure that our player is always on the screen
    # we call our player function in the infinite while loop
    player(playerX, playerY) 
    enemy(enemyX, enemyY)

    # Then we update the display so our changes show 
    # on the screen in the infinite loop
    pygame.display.update()