import pygame
from cfg import *


# Player [Configuração geral do Player]
#_____________________________________________________________________________________________________________________
class Player(pygame.sprite.Sprite):
    
    # Método construtor
    def __init__(self, pos, scale_width, scale_height):
        super().__init__()
        self.images = [
            pygame.transform.scale(pygame.image.load(PLAYER_SPRITE_PATH_1).convert_alpha(), (scale_width, scale_height)),
            pygame.transform.scale(pygame.image.load(PLAYER_SPRITE_PATH_2).convert_alpha(), (scale_width, scale_height))
        ]
        self.current_image = 0
        self.image = self.images[self.current_image]
        self.rect = self.image.get_rect(center=pos)
        self.last_update = pygame.time.get_ticks()
        self.animation_delay = 500  # milissegundos, aumente este valor para uma transição mais sutil
        self.last_shot_time = pygame.time.get_ticks()  # Adiciona last_shot_time como atributo da classe
    
    # Método para atualizar a animação
    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.animation_delay:
            self.last_update = now
            self.current_image = (self.current_image + 1) % len(self.images)
            self.image = self.images[self.current_image]
    
    # Método para movimentar o player
    def handle_movement(self, keys, screen_height, screen_width):
        if keys[pygame.K_w] and self.rect.top > 0:
            self.rect.y -= PLAYER_SPEED
        if keys[pygame.K_s] and self.rect.bottom < screen_height:
            self.rect.y += PLAYER_SPEED
        if keys[pygame.K_a] and self.rect.left > 0:
            self.rect.x -= PLAYER_SPEED
        if keys[pygame.K_d] and self.rect.right < screen_width:
            self.rect.x += PLAYER_SPEED
    
    # Método para gerar o tiro
    def handle_shooting(self, current_time, bullets, shoot_channel, shoot_sound):
        if pygame.mouse.get_pressed()[0] and current_time - self.last_shot_time > SHOOT_DELAY:
            bullet_rect1 = pygame.Rect(self.rect.right, self.rect.centery - 10, BULLET_HEIGHT, BULLET_WIDTH)
            bullet_rect2 = pygame.Rect(self.rect.right, self.rect.centery + 10, BULLET_HEIGHT, BULLET_WIDTH)
            bullets.append((bullet_rect1, bullet_rect2))
            shoot_channel.play(shoot_sound)
            self.last_shot_time = current_time  # Atualiza last_shot_time
    
    # Método para desenhar os tiros
    def draw_bullets(self, screen, bullets):
        for bullet_pair in bullets:
            bullet_rect1, bullet_rect2 = bullet_pair
            pygame.draw.rect(screen, RED, bullet_rect1)
            pygame.draw.rect(screen, RED, bullet_rect2)
    
    # Método para mover os tiros
    def move_bullets(self, bullets, screen_width):
        bullets_to_remove = []
        for bullet_pair in bullets:
            bullet_rect1, bullet_rect2 = bullet_pair
            bullet_rect1.x += BULLET_SPEED
            bullet_rect2.x += BULLET_SPEED
            if bullet_rect1.left > screen_width:
                bullets_to_remove.append(bullet_pair)
        for bullet_pair in bullets_to_remove:
            if bullet_pair in bullets:
                bullets.remove(bullet_pair)


# Avatar [Adapta o Avatar para ser impregado ao game]
#_____________________________________________________________________________________________________________________
def avatar(scale_width, scale_height):
    avatar_image = pygame.image.load(AVATAR_IMAGE_PATH).convert_alpha()
    avatar_image = pygame.transform.scale(avatar_image, (scale_width, scale_height))
    return avatar_image
