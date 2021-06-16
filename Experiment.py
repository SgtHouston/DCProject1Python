# Steps taken
# 1. Create game window
# 2. Title, Logo, and Background
# 3. Add Images
# 4. Track image/player movement in infinite loop.  
# 4. Player Movement by increasing/decreasing pixel value in every loop
# 5. Attach pixel increase/decrease to keyboard input
# 6. Add boundaries to the board
# 7. Create an enemy
# 8. Movement mechanics of the enemy
# 9. Add a background image
# 10. Create Bullet
# 11. Bullet_Y boundary reset fire to ready
# 12. Separating Bullet movement from player x movement.
# 13. Collision Detection For Bullet/Enemy
# D = SqRt((x2 - x1)**2 + (y2 - y1)**2)
# 14. Creating multiple enemies in a list to iterate through - [i]
# 15. Add text and display score 
# 16. Add sound - background, bullet, collision
# 17. Collision Detection for Enemy/Player-space
# 18. 'Game Over' message
# 19. High Score Board json added
# TODO Difficulty Menu using speeds
# TODO enemy Classes
# D = SqRt((x2 - x1)**2 + (y2 - y1)**2)




# Import Pygame module
import pygame
# To add background music
from pygame import mixer
# Intitialize the pygame
pygame.init()
# Import random module to randomize enemy x,y axis values
import random
# Import math for collision calc
import math
# Import json for high score save
import json
with open('high_score.json','r') as high_score_json:
    high_score = json.load(high_score_json)



# Initial Setup
# # Create the screen.  Pass in 1. width *n/800--> and 2. height *n/600 v
# # arguments into the parameters
screen = pygame.display.set_mode ((800, 600))
# Set the background
background = pygame.image.load('Galaxies.png')
# Background sound
mixer.music.load('game_theme.wav')
mixer.music.play(-1)
# Set the Title of your pygame display 
pygame.display.set_caption(" ⚡️ 👽 ⭐︎  Dimensional Defender  ⭐︎ 👽 ⚡️ ")
# Set the Icon of your pygame display.  Use png file from Flaticon.com 
# at 32x32px  
icon = pygame.image.load('enemy.png')
pygame.display.set_icon(icon)





# Player
# Image 64 x 64px
playerImg = pygame.image.load('player.png') 
playerX = 368  
playerY = 530
playerX_change = 0 
def player(x, y):
    # draw an image of the player on the surface of our 
    # game window.  First value is player image, the second and 
    # third are a pair of coordinates
    screen.blit(playerImg, (x, y))




# Enemies
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6 
# Give it a face
for i in range(num_of_enemies):
    for n in range(6):
        if n <= 1:
            enemyImg.append(pygame.image.load('enemy.png'))
        if n > 1 and n < 4:
            enemyImg.append(pygame.image.load('enemy2.png'))
        if n > 4 and n < 6:
            enemyImg.append(pygame.image.load('enemy3.png'))
    # Give it a location
    # # randomize x,y axis values by importing random module and
    # providing a range of coordinates that represent the borders on the 
    # x-axis and the other side of the board on the y.
    enemyX.append(random.randint(0, 736))      
    enemyY.append(random.randint(20, 150))
    # how many pixels the enemy will move per loop on the x-axis.
    
    enemyX_change.append(8)
    # enemy will not only move on the x-axis, but will come down towards 
    # the player on the y-axis once it hits a set border.  To enable this, 
    # the enemy will also have an enemyY_change, unlike the player
    enemyY_change.append(50)  
def enemy(x, y, i):
    # enemy x,y coordinates are passed in as well as the iteration 
    # of the enemy on the list.
    # draw an image of the enemy on the surface of our 
    # game window.  First value is enemy image iteration, the second and 
    # third are a pair of coordinates
    screen.blit(enemyImg[i], (x, y))




# Bullet
# Image 32 x 32px
bulletImg = pygame.image.load('LaserBeam.png') 
# bulletY value the same as player's nose
bulletY = 500
# bulletX wont change, as the bullet will never move side to side
bulletX = 0
bulletX_change = 0 
# Bullet speed 
bulletY_change = 10 
# Ready - You can't see the bullet on the screen
# Fire - The bullet is currently in motion
bullet_state = 'ready'
def fire_bullet(x, y):
    global bullet_state
    bullet_state = 'fire' 
    # X coordinate + 16 so that the bullet is centered halfway through 
    # the player (32px/2 = 16)Y coordinate + 10 so thaty the bullet 
    # appears somewhat "above" the player when executed.
    # screen.blit(image variable, (x, y coordinates))makes the bullet 
    # appear on the screen 
    screen.blit(bulletImg, (x + 16, y + 10))

def enemyCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(((enemyX - bulletX)** 2) + ((enemyY - bulletY)** 2))
    if distance < 27:
        return True 
    else: 
        return False

# Display score
score_value = 0 
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10 
textY = 10 
def show_score(x,y):
    # first render the score using the pygame function font render.
    # Pass in string to display, TRUE,  and the color font. 
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    # then blit it on the screen
    screen.blit(score, (x, y))

# Display Game Over text   
game_over_font = pygame.font.Font('freesansbold.ttf', 64)
high_score_font = pygame.font.Font('freesansbold.ttf', 32)
def game_over_text():
    # first render the score using the pygame function font render.
    # Pass in string to display, TRUE,  and the color font. 
    game_over = game_over_font.render("G A M E  O V E R", True, (255, 255, 255))
    if high_score > score_value:
        high_score_display = high_score_font.render(f"H I G H  S C O R E: {high_score}", True, (255, 255, 255))
        screen.blit(high_score_display, (235, 450))
    elif score_value > high_score:
        high_score_display = high_score_font.render(f"N E W  H I G H  S C O R E :  {score_value}", True, (255, 255, 255))
        screen.blit(high_score_display, (190, 450))
    # then blit it on the screen 
    screen.blit(game_over, (150, 250))
    

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
    background = pygame.image.load('Galaxies.png')
    
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
                # variable moves player n pixels toward origin on the 
                # x-axis.
                playerX_change = -10
            if event.key == pygame.K_RIGHT:
                # when right arrow is pressed, playerX_change variable 
                # moves player n pixels away from the origin on the 
                # x-axis
                playerX_change = 10 
            if event.key == pygame.K_SPACE:
                # when spacebar is pressed, fire bullet function is 
                # called and bullet state is switched to fire. 
                
                # bulletX - when the spacebar is pressed, players x value is saved
                # into the bulletX variable.  This keeps it fixed and it is then 
                # passed into the function.  The alternative, using playerX itself, 
                # yields the bullet following the the players x value as it changes.
                # I might have a second Class of bullet that does just this in the future.  
                # Passing playerX into its x-coordinate would allow you to "guide" 
                # the missles post-fire.
                if bullet_state == 'ready':
                    bullet_sound = mixer.Sound('LaserBlast.wav')
                    bullet_sound.play()
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
        
        if event.type == pygame.KEYUP:
                # when key is released, PlayerX_change variable changes 
                # to zero, stopping player_X axis movement.
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0  




    # Player Movement           
    playerX += playerX_change
    # Set boundaries for playerX, not allowing the 64-pixel icon to 
    # go beyond 0 on the left or 736 on the right (800 pixel screen 
    # size - 64 pixel icon) 
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736




    # Enemy Movement
    # To make sure that our enemies are always on the screen
    # we call our enemy function in the infinite while loop
    # Set boundaries for enemyX, not allowing the 64-pixel icon to go 
    # beyond 0 on the left or 736 on the right (800 pixel screen 
    # size - 64 pixel icon)  
    for i in range(num_of_enemies):
        enemyX[i] += enemyX_change[i]
        
        # If enemy hits left wall
        if enemyX[i] <= 0:
        # When X-value has decreased all the way to zero, begin 
        # increasing it, sending the enemy the other direction 
        # with every loop 
            enemyX_change[i] = 8
            enemyY[i] += enemyY_change[i]
        
        # if enemy hits right wall 
        if enemyX[i] >= 736:
        # When X-value has increased to 736, begin 
        # decreasing it by the movement speed value, sending the 
        # enemy the other direction with every loop
            enemyX_change[i] = -8
            enemyY[i] += enemyY_change[i]

        # Check for Collision with every enemy
        collision = enemyCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision == True:
            collision_sound = mixer.Sound('collision.wav')
            collision_sound.play()
            # reset bullet
            bulletY = 500
            bullet_state = 'ready'
            # increase and display score
            score_value  += 1
            # respawn enemy on other side
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(20, 150)
        
        # Game Over
        if enemyY[i] >= 480:  
            for n in range(num_of_enemies):
                
                enemyY[n] = 2000
                playerY = 2000
            # json dump
            if score_value > high_score:
                with open('high_score.json', 'w') as high_score_json:
                    json.dump(score_value, high_score_json)
            
            # game over message 
            game_over_text()
            break

        # To plot enemy images on screen
        enemy(enemyX[i], enemyY[i], i)




    # Bullet movement
    # When bulletImg passes the 0 Y value, it is off the screen.  
    # This resets the Y value back to the tip of players nose.
    if bulletY <= 0:
        bulletY = 500 
        bullet_state = 'ready'
    # When spacebar is pressed, the function fire_bullet is called 
    # and bullet state is changed to 'fire'. When this happens, 
    if bullet_state == 'fire': 
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change




    # To make sure that our player is always on the screen
    # we call our player function in the infinite while loop
    player(playerX, playerY) 

    # To display our score, we call the show_score function in the while loop
    show_score(textX,textY)
    
    # Then we update the display so our changes show 
    # on the screen in the infinite loop
    pygame.display.update()