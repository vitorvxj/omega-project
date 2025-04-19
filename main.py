import pygame
import random

from interfaces import menu00, menu01
from cfg import *
from screen import screen, screen_width, screen_height
from level import generate_stars, update_stars
from player import Player, avatar
from enemy import Enemy  # Importe a nova classe Enemy

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
    exit_points = [

        (screen_width, screen_height * 1 // 10),
        (screen_width, screen_height * 2 // 10),
        (screen_width, screen_height * 3 // 10),
        (screen_width, screen_height * 4 // 10),
        (screen_width, screen_height * 5 // 10),
        (screen_width, screen_height * 6 // 10),
        (screen_width, screen_height * 7 // 10),
        (screen_width, screen_height * 8 // 10),
        (screen_width, screen_height * 9 // 10),

    ]
    occupied_exits = set()
    exit_spawn_times = {i: 0 for i in range(len(exit_points))}
    enemies = []
    last_enemy_spawn_time = pygame.time.get_ticks()
    enemy_spawn_delay = 1000
    
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
        
        # Atualização de variáveis
        keys = pygame.key.get_pressed()

        # Atualização do tempo
        current_time = pygame.time.get_ticks()

        # Atualização da posição do player
        player.handle_movement(keys, screen_height, screen_width)

        # Atualização da animação do player
        player.handle_shooting(current_time, bullets, shoot_channel, shoot_sound)

        # Atualização dos tiros
        player.move_bullets(bullets, screen_width)

        # Atualização dos inimigos
        enemies = Enemy.move_enemies(enemies)

        # Atualização dos sprites
        all_sprites.update()

        # Criação de inimigos
        if current_time - last_enemy_spawn_time > enemy_spawn_delay and len(enemies) < 9:
            new_enemy = Enemy.create_new_enemy(exit_points, occupied_exits, exit_spawn_times, current_time)
            if new_enemy:
                enemies.append(new_enemy)
                last_enemy_spawn_time = current_time


        # [Colisões]
        # - - - - - - - - - - -

        # Verificação de colisões dos disparos
        for enemy in enemies[:]:  # Use uma cópia da lista para evitar problemas de remoção
            for bullet_pair in bullets[:]:
                bullet_rect1, bullet_rect2 = bullet_pair
                if enemy.rect.colliderect(bullet_rect1) or enemy.rect.colliderect(bullet_rect2):
                    explosion_channel.play(explosion_sound)
                    enemies.remove(enemy)
                    bullets.remove(bullet_pair)  # Remova diretamente
                    score += 1
                    break

        # Colisão do player com os inimigos
        for enemy in enemies: 
            if player.rect.colliderect(enemy.rect):
                player_lives -= 1
                explosion_channel.play(explosion_sound)
                enemies.remove(enemy)
                if player_lives == 0:
                    running = False
                    pygame.mixer.music.stop()
                    estado = "menu01"


        # [Gerador de GRAFICO]
        # - - - - - - - - - - - -

        screen.fill(BLACK)

        update_stars(stars)
        
        all_sprites.draw(screen)  # Desenha todos os sprites
        for enemy in enemies:
            enemy.draw(screen)
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

        clock.tick(60)




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