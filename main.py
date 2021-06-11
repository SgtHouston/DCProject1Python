# Import Pygame module
import pygame

# Intitialize the pygame
pygame.init()           

# # Create the screen.  Pass in 1. width 800--> and 2. height ^
# # arguments into the parameters
screen = pygame.display.set_mode ((800, 600))

# Set the Title of your pygame display 
pygame.display.set_caption(" 👽 Space Invaders 👽 ")

# Set the Icon of your pygame display.  Use png file from Flaticon.com.  
icon = pygame.image.load('spacefighter.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 530

def player(x, y):
    # draw an image of the player on the surface of our 
    # game window.  First value is player image, the second and 
    # third are a pair of coordinates
    screen.blit(playerImg, (x, y))

# Game Loop
running = True
while running:
    # Change the background of the window using screen.fill.  
    # This takes 3 values, R,G,B or Red, Greed, and Blue.  
    # This is positioned so it runs in the infinite while 
    # loop while the game runs.  Range is 0 - 255 for each color.
    screen.fill((150, 0, 255))
    
    


    # loop though all of the events happening inside
    # the game window
    for event in pygame.event.get():
        # If close button has been pressed,
        if event.type == pygame.QUIT:
            # Quit the program window
            running = False

# If keystroke is pressed, check whether it is right or left.
# Keystrokes are pygame events that will be captured and 
# looped through

    # To make sure that our player is always on the screen
    # we call our player function in the infinite while loop
    player(playerX, playerY) 

    # Then we update the display so our changes show
    pygame.display.update()