import pygame
import random

from screen import screen, screen_width, screen_height

# Configurações das estrelas
NUM_STARS = 100
STAR_COLORS = [(135, 206, 235), (176, 224, 230), (173, 216, 230), (135, 206, 250)]
STAR_LEVELS = 5
STAR_SPEED = [1, 2, 4, 8, 16]

STAR_DARK_BLUE = (0, 0, 139) # [Backgroud Stars]
STAR_LIGHT_BLUE = (173, 216, 230) # [Backgroud Stars]


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




