"""
Image Creation Script using PIL
Created by ELYES
Generates simple bitmap images for the Alien Invasion game.
"""

from PIL import Image, ImageDraw
import os

# Create images directory if it doesn't exist
if not os.path.exists('images'):
    os.makedirs('images')

# Create ship image
ship_img = Image.new('RGB', (50, 30), 'black')
draw = ImageDraw.Draw(ship_img)
# Draw a white triangle for the ship
draw.polygon([(25, 0), (0, 30), (50, 30)], fill='white')
ship_img.save('images/ship.bmp')

# Create alien image
alien_img = Image.new('RGB', (40, 40), 'black')
draw = ImageDraw.Draw(alien_img)
# Draw a green rectangle for the alien body
draw.rectangle([(5, 5), (35, 35)], fill='green')
# Draw red eyes
draw.ellipse([(10, 10), (20, 20)], fill='red')  # Left eye
draw.ellipse([(20, 10), (30, 20)], fill='red')  # Right eye
alien_img.save('images/alien.bmp')

print("Images created successfully!") 