import pygame

# initialize the pygame
pygame.init()

# create screen
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("MOTHER FUCKING TITLE BITCH")
icon = pygame.image.load('ufo (1).png')
pygame.display.set_icon(icon)

# player
playerImg = pygame.image.load('space-invaders.png')
playerX = 370
playerY = 480
playerX_Change = 0


def player(x, y):
    screen.blit(playerImg, (x, y))


# Game Loop, makes sure the game window is always open till the user quits the game.

running = True

while running:
    # background color.
    screen.fill((0, 102, 204))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed, check if right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_Change = -.1
            if event.key == pygame.K_RIGHT:
                playerX_Change = .1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_Change = 0
    playerX += playerX_Change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    player(playerX, playerY)
    pygame.display.update()
