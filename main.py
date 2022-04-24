from cProfile import run
from pickle import FALSE
from turtle import width
import pygame
from pygame.locals import *
from player import Player
import time
from enemy import Enemy
import sys
from buttons import Button

pygame.init()  # Initializes pygame

screen_res = (1920,1088)
# Sets the size of the game window
screen = pygame.display.set_mode(screen_res, pygame.RESIZABLE)

# Runs Game for as long as the user wants
clock = pygame.time.Clock()
previousTime = time.time()
#loads the 
setting_image = pygame.image.load('setting-2.png').convert_alpha()


# Creates the settings button
#setting_button = Button(setting_image, 2)

# Player and Enemy Initialization
player = Player(screen, screen_res)
enemy = Enemy(40, 40, 32, 32, 500, screen)

# Loads the game music
music = pygame.mixer.music.load('gamemusic.mp3')
pygame.mixer.music.play(-1)


def draw_text(text, color, surface, x, y):
    font = pygame.font.Font('freesansbold.ttf', 32)
    textobj = font.render(text, True, color)
    textRect = textobj.get_rect()
    textRect.topleft = (x, y)
    surface.blit(textobj, textRect)



#loads the menu back ground image
background_img = pygame.image.load('gamebackground.png').convert()
back_ground= pygame.transform.scale(background_img,(screen_res))

#loads the main menu buttons
mainmenu_button_img = pygame.image.load('Menu Button.png').convert_alpha()
mainmenu_button1 = Button(210,45,mainmenu_button_img, 0.4)
mainmenu_button2 = Button(210,245, mainmenu_button_img, 0.4)
mainmenu_button3 = Button(210,445, mainmenu_button_img, 0.4)

# Creates the main menu
def main_menu():
    clock.tick()
    WHITE = (255,255,255)
    i = 0
    run = True
    text_button1 = 'PLAY'
    text_button2 = 'SETTINGS'
    text_button3 = 'HOW TO PLAY'
    width = 1920
    while run:

        for event in pygame.event.get():
        # Quits the game when the user presses the quit button
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        
        screen.blit(back_ground,(i,0))
        screen.blit(back_ground,(width+i,0))
        if i == -width:
            screen.blit(back_ground,(width+i,0))
            i = 0

        i -=1

        mainmenu_button1.drawbutton(screen)
        if mainmenu_button1.action1 == True:
            break
        mainmenu_button2.drawbutton2(screen)
        if mainmenu_button2.action2 == True:
            settings_screen()
        mainmenu_button3.drawbutton3(screen)
        #if mainmenu_button3.action3 == True:
           # break
        draw_text(text_button1, WHITE, screen, 359, 225)
        draw_text(text_button2, WHITE, screen, 319, 425)
        draw_text(text_button3, WHITE, screen, 294,625)

        pygame.display.update()
        clock.tick()


# Responsible for Drawing items onto the Screen (Use the Function for Drawings)
def redrawGameWindow(bullets=None):
    screen.fill((255, 0, 0))  # Constantly refreshes the screen with the color black
    #setting_button.drawbutton(100,0,screen)
    player.shoot(dt)
    enemy.draw(screen, dt)
    player.draw(dt)  # Detects button inputs of the user as well as its position on screen
    pygame.display.flip()  # Updates the entirety of all the contents on the screen
    
def settings_screen():
    clock.tick()
    screen.fill((255, 0, 0))
    
    run = True
    while run:
        for event in pygame.event.get():
        # Quits the game when the user presses the quit button
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
    pygame.display.flip()
    pygame.display.update()
    clock.tick()



# Controls the main events of the game (i.e. Movement, shooting, etc.)
while True:
    clock.tick()
    currentTime = time.time()
    dt = currentTime - previousTime
    previousTime = currentTime

    playerX = player.getPlayerPositionX()
    playerY = player.getPlayerPositionY()
    playerW = player.getPlayerWidth()
    playerH = player.getPlayerHeight()

    for event in pygame.event.get():
        # Quits the game when the user presses the quit button
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # Detects whenever the user presses down on a key
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.left_pressed = True
            if event.key == pygame.K_RIGHT:
                player.right_pressed = True
            if event.key == pygame.K_UP:
                player.up_pressed = True
            if event.key == pygame.K_DOWN:
                player.down_pressed = True
        # Detects whenever the user pressed up on a key
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.left_pressed = False
            if event.key == pygame.K_RIGHT:
                player.right_pressed = False
            if event.key == pygame.K_UP:
                player.up_pressed = False
            if event.key == pygame.K_DOWN:
                player.down_pressed = False
    main_menu()
    redrawGameWindow()
    pygame.display.update()
    
    clock.tick()  # Tracks time (FPS) of the game
