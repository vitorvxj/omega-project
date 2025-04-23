import pygame
import random

from interfaces import menu00, menu01
from cfg import *
from screen import screen, screen_width, screen_height, tick_rate
from level import generate_stars, update_stars
from player import Player, avatar

pygame.init()
pygame.mixer.init()

# -   -   -   -   -   -   -   -   -   -   -   -   -   -   -

main_menu = menu00()
game_over = menu01()

# Motor Grafico [Estrutura principal]
#_________________________________________________________________________________________
def game():
    global player_lives, score, player_rect, screen, estado

    clock = pygame.time.Clock()
    stars = generate_stars()
    avatar_image = avatar(100, 100)

    player = Player((screen_width // 10, (screen_height - PLAYER_HEIGHT) // 2), PLAYER_WIDTH, PLAYER_HEIGHT)  # Ajuste a posição inicial do jogador
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    shoot_sound = pygame.mixer.Sound(SHOOT_SOUND_PATH)
    shoot_channel = pygame.mixer.Channel(1)

    explosion_sound = pygame.mixer.Sound(EXPLOSION_SOUND_PATH)
    explosion_channel = pygame.mixer.Channel(2)

    pygame.mixer.music.load(BACKGROUND_MUSIC_PATH)
    pygame.mixer.music.play(-1)

    bullets = []

    # Configuração da fonte para exibir o FPS
    font = pygame.font.SysFont("Arial", 18, bold=True)
    fps_color = (255, 255, 255)  # Cor branca para o texto do FPS

    reset_game_state()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # [Mecanica PRINCIPAL]
        # - - - - - - - - - - -
        keys = pygame.key.get_pressed()
        current_time = pygame.time.get_ticks()
        player.handle_movement(keys, screen_height, screen_width)
        player.handle_shooting(current_time, bullets, shoot_channel, shoot_sound)
        player.move_bullets(bullets, screen_width)
        all_sprites.update()

        # [Colisões]
        # - - - - - - - - - - -

        # [Gerador de GRAFICO]
        # - - - - - - - - - - - -

        screen.fill(BLACK)
        update_stars(stars)
        
        all_sprites.draw(screen)  # Desenha todos os sprites
        for bullet_pair in bullets:
            bullet_rect1, bullet_rect2 = bullet_pair
            pygame.draw.rect(screen, RED, bullet_rect1)
            pygame.draw.rect(screen, RED, bullet_rect2)

        draw_hud(avatar_image)

        # Exibição do FPS
        fps = clock.get_fps()
        fps_text = font.render(f"FPS: {int(fps)}", True, fps_color)
        screen.blit(fps_text, (10, 10))  # Exibe o FPS no canto superior esquerdo

        pygame.display.update()
        tick_rate(clock)

# Hud in game [Desenha o HUD durante a gameplay]
#_________________________________________________________________________________________
def draw_hud(avatar_image):
    global screen, player_lives, player_shield, score

    # Desenha a Moldura do Avatar
    # - - - - - - - - - - - - - - 
    square_size = 80  # [Tamanho da Moldura]
    border_thickness = 1  # [Espessura da Moldura]
    square_rect = pygame.Rect((screen_width // 2 - square_size // 2, screen_height - 50 - square_size // 2), (square_size, square_size))

    border_color = (255, 204, 255)  # [Cor da Moldura]
    pygame.draw.rect(screen, border_color, square_rect, border_thickness)

    avatar_size = square_size - 2 * border_thickness
    avatar_image = pygame.transform.scale(avatar_image, (avatar_size, avatar_size))
    avatar_rect = avatar_image.get_rect(center=square_rect.center)
    screen.blit(avatar_image, avatar_rect.topleft)

    # Desenha a barra de vida
    # - - - - - - - - - - - - - - 
    life_bar_width = 400  # [Comprimento]
    life_bar_height = 20  # [Altura]
    life_bar_color = (0, 255, 0)  # [Cor da vida]
    life_bar_border_color = (144, 238, 144)  # [Cor da borda da vida]

    life_bar_rect = pygame.Rect(square_rect.left - life_bar_width - 10, square_rect.centery - life_bar_height // 2, life_bar_width, life_bar_height)
    pygame.draw.rect(screen, life_bar_border_color, life_bar_rect, border_thickness)

    current_life_width = (player_lives / initial_lives) * (life_bar_width - 2 * border_thickness)
    current_life_rect = pygame.Rect(life_bar_rect.left + border_thickness, life_bar_rect.top + border_thickness, current_life_width, life_bar_height - 2 * border_thickness)
    pygame.draw.rect(screen, life_bar_color, current_life_rect)

    # Desenha a barra de escudo
    # - - - - - - - - - - - - - - 
    shield_bar_width = 400  # [Comprimento]
    shield_bar_height = 20  # [Altura]
    shield_bar_color = (0, 0, 255)  # [Cor do Shield]
    shield_bar_border_color = (173, 216, 230)  # [Cor da borda do Shield]

    shield_bar_rect = pygame.Rect(square_rect.right + 10, square_rect.centery - shield_bar_height // 2, shield_bar_width, shield_bar_height)
    pygame.draw.rect(screen, shield_bar_border_color, shield_bar_rect, border_thickness)

    if initial_shield > 0:
        current_shield_width = (player_shield / initial_shield) * (shield_bar_width - 2 * border_thickness)
    else:
        current_shield_width = 0
    current_shield_rect = pygame.Rect(shield_bar_rect.left + border_thickness, shield_bar_rect.top + border_thickness, current_shield_width, shield_bar_height - 2 * border_thickness)
    pygame.draw.rect(screen, shield_bar_color, current_shield_rect)

def reset_game_state():
    global player_lives, player_shield, score
    player_lives = initial_lives  
    player_shield = initial_shield
    score = 0

# Loop principal [Gerenciador de estados do GAME]
#_________________________________________________________________________________________
while True:
    if estado == "menu00":
        estado = main_menu.main_menu(screen, screen_width, screen_height)
    elif estado == "menu01":
        estado = game_over.game_over(screen, screen_width, screen_height)
    elif estado == "game":
        game()