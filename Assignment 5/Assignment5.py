# Brian Bowles, Assignment 5, February 9, 2015.

# File path for the background image.
background_image = 'football_background.jpg'
# File path for the sprite.
sprite_image = 'falcon.png'

# Modules to be imported.
import pygame
from pygame.locals import *
from sys import exit
import time

pygame.init()

screen = pygame.display.set_mode((200, 200), 0, 32)
pygame.display.set_caption("Diagonal Sprite Movement")

# Convert image to displays format.
background_image = pygame.image.load(background_image).convert()
sprite_image = pygame.image.load(sprite_image).convert_alpha()

sprite_x = 0
delta_x = 5
delta_y = 5
sprite_y = 0
delta_t = 0.1

# Move sprite delta-x spaces every delta t time seconds.
my_event = pygame.event.Event(KEYDOWN, key = K_SPACE, mod = 0, unicode = u' ')

# Game loop.
while True:
    pygame.event.post(my_event)
    for event in pygame.event.get():
        if event.type == QUIT:
            del background_image
            del sprite_image
            pygame.display.quit()
            exit(0)

        screen.blit(background_image, (0, 0))
        screen.blit(sprite_image, (sprite_x, sprite_y))
        
        sprite_x += delta_x
        sprite_y += delta_y

        if sprite_x > 200.0:
            sprite_x = 0

        if sprite_y > 200.0:
            sprite_y = 0

        pygame.display.update()

        time.sleep(delta_t)
