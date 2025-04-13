"""
Image Creation Script
Created by ELYES
Generates simple bitmap images for the Alien Invasion game.
"""

import pygame
import os

# Initialize pygame
pygame.init()

# Create images directory if it doesn't exist
if not os.path.exists('images'):
    os.makedirs('images')

# Create a surface for the ship
ship_surface = pygame.Surface((50, 30))
ship_surface.fill((0, 0, 0))  # Black background
pygame.draw.polygon(ship_surface, (255, 255, 255), [(25, 0), (0, 30), (50, 30)])  # White triangle
pygame.image.save(ship_surface, 'images/ship.bmp')

# Create a surface for the alien
alien_surface = pygame.Surface((40, 40))
alien_surface.fill((0, 0, 0))  # Black background
# Draw alien body
pygame.draw.rect(alien_surface, (0, 255, 0), (5, 5, 30, 30))  # Green rectangle
# Draw alien eyes
pygame.draw.circle(alien_surface, (255, 0, 0), (15, 15), 5)  # Red left eye
pygame.draw.circle(alien_surface, (255, 0, 0), (25, 15), 5)  # Red right eye
pygame.image.save(alien_surface, 'images/alien.bmp')

print("Images created successfully!") 