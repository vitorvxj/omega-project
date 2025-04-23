import pygame
from cfg import *
pygame.mixer.init()

# OST
button_sound = pygame.mixer.Sound("c:/Users/joaov/OneDrive/Arquivos/Projeto OMEGA/Assets/interface/OST/button.wav")



def fade_screen(screen, color, fade_time):
    fade_surface = pygame.Surface((screen.get_width(), screen.get_height()))
    fade_surface.fill(color)
    alpha = 0
    increment = 255 / (fade_time * 60)  # Calcula o incremento baseado no tempo de fade

    for _ in range(int(fade_time * 60)):
        alpha += increment
        fade_surface.set_alpha(alpha)
        screen.blit(fade_surface, (0, 0))
        pygame.display.update()
        pygame.time.delay(int(500 / 60))  # Delay para ajustar a taxa de quadros


def draw_horizontal_gradient(surface, start_color, end_color):
    width = surface.get_width()
    height = surface.get_height()
    gradient_width = width // 2 + 30  # Define a largura do gradiente para metade da tela
    for x in range(gradient_width):
        ratio = x / gradient_width
        color = [
            int(start_color[i] * (1 - ratio) + end_color[i] * ratio)
        for i in range(3)
        ]
        color.append(int(255 * (1 - ratio)))  # Adiciona a transparência
        pygame.draw.line(surface, color, (x, 0), (x, height))



# Função para aplicar estilos de texto
#_________________________________________________________________________________________
def text_styles(text, font, surface, x, y, color_scheme, gradient=True, border=True, aura=True):
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect(topleft=(x, y))

    aura_colors = {
        'blue': (173, 216, 230),  # Aura azul suave
        'red': (230, 173, 173),    # Aura vermelha suave
    }
    if aura:
        aura_surface = font.render(text, True, aura_colors[color_scheme])
        surface.blit(aura_surface, (text_rect.x - 1, text_rect.y - 1))
        surface.blit(aura_surface, (text_rect.x + 1, text_rect.y - 1))
        surface.blit(aura_surface, (text_rect.x - 1, text_rect.y + 1))
        surface.blit(aura_surface, (text_rect.x + 1, text_rect.y + 1))

    border_colors = {
        'blue': (135, 206, 250),  # Azul claro
        'red': (250, 135, 135),    # Vermelho claro
        'purple': (255, 204, 255) # Roxo claro (mais claro em 30%)
    }
    if border:
        border_color = border_colors[color_scheme]
        for dx in [-2, 0, 2]:
            for dy in [-2, 0, 2]:
                if dx != 0 or dy != 0:
                    border_surface = font.render(text, True, border_color)
                    surface.blit(border_surface, (text_rect.x + dx, text_rect.y + dy))

    if gradient:
        gradient_surface = pygame.Surface(text_surface.get_size(), pygame.SRCALPHA)
        gradient_colors = {
            'blue': [(100, 100, 255), (0, 0, 100), (0, 0, 255)],  # Gradiente azul
            'red': [(255, 100, 100), (100, 0, 0), (255, 0, 0)],    # Gradiente vermelho
        }
        color_top, color_middle, color_bottom = gradient_colors[color_scheme]
        for i in range(text_rect.height):
            if i < text_rect.height // 2:
                color = [
                    (color_middle[j] - color_top[j]) * i // (text_rect.height // 2) + color_top[j]
                    for j in range(3)
                ]
            else:
                color = [
                    (color_bottom[j] - color_middle[j]) * (i - text_rect.height // 2) // (text_rect.height // 2) + color_middle[j]
                    for j in range(3)
                ]
            pygame.draw.line(gradient_surface, color, (0, i), (text_rect.width, i))
        text_surface.blit(gradient_surface, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

    surface.blit(text_surface, text_rect.topleft)


# Função para escalar e posicionar um retângulo proporcionalmente à resolução da tela
#_________________________________________________________________________________________
def scale_rect(rect, screen_width, screen_height, base_width=1920, base_height=1080):
    scale_x = screen_width / base_width
    scale_y = screen_height / base_height
    return pygame.Rect(
        int(rect.x * scale_x),
        int(rect.y * scale_y),
        int(rect.width * scale_x),
        int(rect.height * scale_y)
    )


# TELA GAME OVER MENU01
#_________________________________________________________________________________________
class menu01:

    def game_over(self, screen, screen_width, screen_height):
        global start_button, return_button

        pygame.mixer.music.load(MENU_MUSIC_PATH)
        pygame.mixer.music.play(-1)

        base_width, base_height = 1920, 1080  # Resolução base para escalonamento
        over_running = True
        while over_running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    over_running = False
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    if start_button.collidepoint((mouse_x, mouse_y)):
                        button_sound.play()
                        fade_screen(screen, BLACK, 1)
                        return "game"
                    elif return_button.collidepoint((mouse_x, mouse_y)):
                        button_sound.play()
                        fade_screen(screen, BLACK, 1)
                        return "menu00"

            screen.fill(BLACK)
            font = pygame.font.Font(font_path, int(80 * (screen_width / base_width)))
            text_styles(
                "GAME OVER!!!", font, screen,
                int(screen_width // 20), int(screen_height // 2 - 60),
                color_scheme='red', gradient=True, border=True, aura=True
            )

            font = pygame.font.Font(font_path, int(30 * (screen_width / base_width)))
            start_button = scale_rect(
                pygame.Rect(100, 920, 200, 44), screen_width, screen_height, base_width, base_height
            )
            return_button = scale_rect(
                pygame.Rect(100, 980, 200, 44), screen_width, screen_height, base_width, base_height
            )

            text_styles("Decolar", font, screen, start_button.x, start_button.y, color_scheme='red', gradient=True, border=True, aura=True)
            text_styles("Voltar", font, screen, return_button.x, return_button.y, color_scheme='red', gradient=True, border=True, aura=True)

            pygame.display.flip()


# TELA INICIAL MENU00
#_________________________________________________________________________________________
class menu00:

    def main_menu(self, screen, screen_width, screen_height):
        global background_image

        pygame.mixer.music.load(MENU_MUSIC_PATH)
        pygame.mixer.music.play(-1)
        background_image = pygame.image.load("c:/Users/joaov/OneDrive/Arquivos/Projeto OMEGA/Assets/interface/background/menu_home.png").convert()

        base_width, base_height = 1920, 1080  # Resolução base para escalonamento

        def resize_background():
            global background_image
            bg_aspect_ratio = background_image.get_width() / background_image.get_height()
            screen_aspect_ratio = screen_width / screen_height
            if bg_aspect_ratio > screen_aspect_ratio:
                new_height = screen_height
                new_width = int(new_height * bg_aspect_ratio)
            else:
                new_width = screen_width
                new_height = int(new_width / bg_aspect_ratio)
            background_image = pygame.transform.scale(background_image, (new_width, new_height))

        def draw_background():
            bg_x = (screen_width - background_image.get_width()) // 2
            bg_y = (screen_height - background_image.get_height()) // 2
            screen.blit(background_image, (bg_x, bg_y))

        resize_background()

        menu_running = True
        while menu_running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    menu_running = False
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    if start_button.collidepoint((mouse_x, mouse_y)):
                        button_sound.play()
                        fade_screen(screen, BLACK, 1)
                        return "game"
                    elif quit_button.collidepoint((mouse_x, mouse_y)):
                        button_sound.play()
                        fade_screen(screen, BLACK, 1)
                        pygame.quit()

            draw_background()

            gradient_surface = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
            draw_horizontal_gradient(gradient_surface, (0, 0, 0), (0, 0, 0, 0))
            screen.blit(gradient_surface, (0, 0))

            font = pygame.font.Font(font_path, int(80 * (screen_width / base_width)))
            text_styles(
                "SPEED NAVY ULTRA", font, screen,
                int(screen_width // 20), int(screen_height // 2 - 60),
                color_scheme='blue', gradient=True, border=True, aura=True
            )

            font = pygame.font.Font(font_path, int(30 * (screen_width / base_width)))
            start_button = scale_rect(
                pygame.Rect(100, 920, 200, 44), screen_width, screen_height, base_width, base_height
            )
            quit_button = scale_rect(
                pygame.Rect(100, 980, 200, 44), screen_width, screen_height, base_width, base_height
            )

            text_styles("Decolar", font, screen, start_button.x, start_button.y, color_scheme='blue', gradient=True, border=True, aura=True)
            text_styles("Sair", font, screen, quit_button.x, quit_button.y, color_scheme='blue', gradient=True, border=True, aura=True)

            pygame.display.flip()
