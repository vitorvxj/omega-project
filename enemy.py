import pygame
import random
from cfg import ENEMY_SPRITE_PATH, ENEMY_WIDTH, ENEMY_HEIGHT, ENEMY_SPEED

class Enemy:
    def __init__(self, exit_points, occupied_exits, exit_spawn_times, current_time):
        self.exit_points = exit_points
        self.occupied_exits = occupied_exits
        self.exit_spawn_times = exit_spawn_times
        self.current_time = current_time
        self.sprite = pygame.image.load(ENEMY_SPRITE_PATH).convert_alpha()
        self.sprite = pygame.transform.scale(self.sprite, (ENEMY_WIDTH, ENEMY_HEIGHT))
        self.rect = self.create_enemy()
        self.exit_index = None  # Adiciona o índice de saída

    def create_enemy(self):
        spawn_delay = 3000  # Delay de 3 segundos
        valid_exits = [
            i for i in range(len(self.exit_points))
            if i not in self.occupied_exits and self.current_time - self.exit_spawn_times[i] > spawn_delay
        ]
        if not valid_exits:
            return None
        self.exit_index = random.choice(valid_exits)  # Armazena o índice de saída
        exit_pos = self.exit_points[self.exit_index]
        self.exit_spawn_times[self.exit_index] = self.current_time
        return pygame.Rect(exit_pos[0], exit_pos[1] - ENEMY_HEIGHT // 2, ENEMY_WIDTH, ENEMY_HEIGHT)

    def move(self):
        self.rect.x += ENEMY_SPEED

    def draw(self, screen):
        screen.blit(self.sprite, self.rect)

    def create_new_enemy(exit_points, occupied_exits, exit_spawn_times, current_time):
        new_enemy = Enemy(exit_points, occupied_exits, exit_spawn_times, current_time)
        if new_enemy.rect:
            occupied_exits.add(new_enemy.exit_index)
            return new_enemy
        return None

    def move_enemies(enemies):
        new_enemies = []
        for enemy in enemies:
            enemy.move()
            if enemy.rect.right >= 0:
                new_enemies.append(enemy)
        return new_enemies
