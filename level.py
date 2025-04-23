import pygame
import random

from screen import screen, screen_width, screen_height
from cfg import *




def generate_stars():

    stars = []
    for _ in range(NUM_STARS):
        x = random.randint(0, screen_width)
        y = random.randint(0, screen_height)
        color = random.choice(STAR_COLORS)
        level = random.randint(1, STAR_LEVELS)
        stars.append((x, y, color, level))
    return stars

def update_stars(stars):
    
    for i, (x, y, color, level) in enumerate(stars):
        x -= STAR_SPEED[level - 1]
        if x < 0:
            x = screen_width
            y = random.randint(0, screen_height)
        stars[i] = (x, y, color, level)

        pygame.draw.rect(screen, STAR_LIGHT_BLUE, (x, y, level, level))
        pygame.draw.rect(screen, STAR_DARK_BLUE, (x, y - level, level, level))
        pygame.draw.rect(screen, STAR_DARK_BLUE, (x, y + level, level, level))
        pygame.draw.rect(screen, STAR_DARK_BLUE, (x - level, y, level, level))
        pygame.draw.rect(screen, STAR_DARK_BLUE, (x + level, y, level, level))




