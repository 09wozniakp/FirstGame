'''This file contains the code for spriets and entities for 
    the game '''
import pygame
from config import *
import math
import random

class Player(pygame.sprite.Sprite):
    '''This is the main character class'''
    def __init__(self, game, x, y):
        '''Initialize the player character
            and draw it on the screen'''
        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        # Set some parameters
        self.x = x * TILESIZE
        self.y = y* TILESIZE
        self.width = PLAYER_SIZE
        self.height = PLAYER_SIZE

        # Temporary variables to store player movement
        self.x_change = 0
        self.y_change = 0

        # Default player sprite directions - important for animations
        self.facing = 'down'

        # Initialize player character
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((0, 255, 0))

        # Draw player character
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.movement() # Call the movemnt function

        # Update the actual co-ordinates of the player character
        self.rect.x += self.x_change # Horizontal direction
        self.collide_blocks('x') # Call for collision check with blocks
        self.rect.y += self.y_change # Vertical direction
        self.collide_blocks('y') # Call for collision check with blocks

        # Reset the temporary variable
        self.x_change = 0
        self.y_change = 0

    def movement(self):
        '''Handle player movement'''
        keys = pygame.key.get_pressed() # Look for keyboard presses
        # Handle moving in all directions and character rotation
        # Also keep the player within screen bounds
        if keys[pygame.K_LEFT] and self.rect.x - PLAYER_VEL >= 0:
            self.x_change -= PLAYER_VEL
            self.facing = 'left'
        if keys[pygame.K_RIGHT] and self.rect.x + PLAYER_VEL + self.width <= WIN_WIDTH:
            self.x_change += PLAYER_VEL
            self.facing = 'right'
        if keys[pygame.K_UP] and self.rect.y - PLAYER_VEL >= 0:
            self.y_change -= PLAYER_VEL
            self.facing = 'up'
        if keys[pygame.K_DOWN] and self.rect.y + PLAYER_VEL + self.height <= WIN_HEIGHT:
            self.y_change += PLAYER_VEL
            self.facing = 'down'
    
    def collide_blocks(self, direction):
        '''Function for collission handling with blocks'''
        # For horizontal movement
        if direction == "x":
            # Check for collission
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                # When going left
                if self.x_change > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width
                # When going right
                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right
       # For vertical movement
        if direction == "y":
            # Check for collission
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                # For up movement
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height
                # For down movement
                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom

class Enemy(pygame.sprite.Sprite):
    '''This is an enemy character class'''
    def __init__(self, game, x, y):
        '''Initialise and draw the enemy character
            on the screen'''
        self.game = game
        self._layer = ENEMY_LAYER
        self.groups = self.game.all_sprites, self.game.enemies
        pygame.sprite.Sprite.__init__(self, self.groups)

        # Set some parameters
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        # Temporary variables to store movement in
        self.x_change = 0
        self.y_change = 0

        # Set the facing for the enemy sprite
        self.facing = random.choice(['left','right', 'up', 'down'])

        # Set some movement parameters
        self.movement_loop = 0
        self.max_travel = random.randint(50, 100)

        # Initialise the enemy character
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((255, 0, 0))

        # Draw enemy character
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        '''This function updates the enemy sprite as the game progresses'''
        
        self.movement() #Call the movement function

        # Update the actual co-ordinates of the enemy character
        self.rect.x += self.x_change # Horizontal direction
        self.collide_blocks('x') # Call for collision check with blocks
        self.rect.y += self.y_change # Vertical direction
        self.collide_blocks('y') # Call for collision check with blocks

        # Reset the temporary variable
        self.x_change = 0
        self.y_change = 0

    def movement(self):
        '''This function handles the enemy character movement'''
        if self.facing == 'left':
            self.x_change -= ENEMY_SPEED
            self.movement_loop -= 1
            if self.movement_loop <= -self.max_travel:
                self.facing = random.choice(['right', 'up', 'down'])


        if self.facing == 'right':
            self.x_change += ENEMY_SPEED
            self.movement_loop += 1
            if self.movement_loop >= self.max_travel:
                self.facing = random.choice(['left', 'up', 'down'])

        if self.facing == 'up':
            self.y_change -= ENEMY_SPEED
            self.movement_loop -= 1
            if self.movement_loop <= -self.max_travel:
                self.facing = random.choice(['left','right', 'down'])

        if self.facing == 'down':
            self.y_change += ENEMY_SPEED
            self.movement_loop += 1
            if self.movement_loop >= self.max_travel:
                self.facing = random.choice(['left','right', 'up'])

    def collide_blocks(self, direction):
        '''Function for collission handling with blocks'''
        # For horizontal movement
        if direction == "x":
            # Check for collission
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                # When going left
                if self.x_change > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width
                # When going right
                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right
       # For vertical movement
        if direction == "y":
            # Check for collission
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                # For up movement
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height
                # For down movement
                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom

class Block(pygame.sprite.Sprite):
    '''Class for the block obstacles'''
    def __init__(self, game, x, y):
        '''Initialize the block object'''
        self.game = game
        self._layer =  BLOCK_LAYER
        self.groups = self.game.all_sprites, self.game.blocks
        pygame.sprite.Sprite.__init__(self, self.groups)

        # Set some parameters
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        # Initialise the block sprite
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((0, 0, 255))
        
        # Draw the block
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

