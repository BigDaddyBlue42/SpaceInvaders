import pygame
import random

# initialize the pygame
pygame.init()

# create screen
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("MOTHER FUCKING TITLE BITCH")
icon = pygame.image.load('ufo (1).png')
pygame.display.set_icon(icon)
background = pygame.image.load('Backgroundimg.png')

# player
playerImg = pygame.image.load('battleship.png')
playerX = 370
playerY = 480
playerX_Change = 0

# enemy
enemyImg = pygame.image.load('enemy.png')
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyX_Change = .1
enemyY_change = 0

# bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletY_change = .4
bullet_state = "ready"
constantX = 0

def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


def fireBullet(x, y):
    global constantX
    constantX = x
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


# Game Loop, makes sure the game window is always open till the user quits the game.

running = True

while running:
    # background color.
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed, check if right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_Change = -.2
            if event.key == pygame.K_RIGHT:
                playerX_Change = .2

            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    fireBullet(playerX, playerY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_Change = 0

    playerX += playerX_Change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    enemyX += enemyX_Change

    if enemyX <= 0:
        enemyX_Change = 0.1
        enemyY += 50
    elif enemyX >= 736:
        enemyX_Change = -0.1
        enemyY += 50
    if bullet_state == "fire":
        fireBullet(constantX, bulletY)
        bulletY -= bulletY_change
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
