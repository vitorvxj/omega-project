import pygame

resolucoes = {
    "HD": (1280, 720),
    "FHD": (1920, 1080),
    "2K": (2560, 1440),
    "4K": (3840, 2160)
}
resolution = resolucoes["FHD"]

screen = pygame.display.set_mode(resolution, pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.SRCALPHA)
screen_width, screen_height = screen.get_size()

TICK_RATE = 60
FPS_RATE = 60

def tick_rate(clock):
    clock.tick(TICK_RATE)



base_width, base_height = 1920, 1080  # Resolução base
aspect_ratio = base_width / base_height

if screen_width / screen_height > aspect_ratio:
    scaled_width = int(screen_height * aspect_ratio)
    scaled_height = screen_height
else:
    scaled_width = screen_width
    scaled_height = int(screen_width / aspect_ratio)



def scale(base_width, base_height, scaled_width, scaled_height):

    scale_x = scaled_width / base_width
    scale_y = scaled_height / base_height
    return scale_x, scale_y

scale_x, scale_y = scale(base_width, base_height, scaled_width, scaled_height)



def scale_rect(rect, base_width=1920, base_height=1080):

    return pygame.Rect(
        int(rect.x * scale_x),
        int(rect.y * scale_y),
        int(rect.width * scale_x),
        int(rect.height * scale_y)
    )


def mudar_resolucao(screen, resolucao="FHD"):
    global scale_x, scale_y, scaled_width, scaled_height

    if resolucao not in resolucoes:
        resolucao = "FHD" #Resolução padrão

    nova_resolucao = resolucoes[resolucao]
    pygame.display.set_mode(nova_resolucao, pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.HWSURFACE)
    
    scaled_width, scaled_height = nova_resolucao
    scale_x, scale_y = scale(base_width, base_height, scaled_width, scaled_height)

    return screen



def scale_elements(nova_resolucao, resolucao_atual, elementos):

    fator_largura, fator_altura = scale(resolucao_atual[0], resolucao_atual[1], nova_resolucao[0], nova_resolucao[1])
    escalonados = []
    
    for elemento in elementos:

        elemento_escalonado = {

            "posicao": (elemento["posicao"][0] * fator_largura, elemento["posicao"][1] * fator_altura),
            "tamanho": (elemento["tamanho"][0] * fator_largura, elemento["tamanho"][1] * fator_altura)
        }
        escalonados.append(elemento_escalonado)
    
    return escalonados




# EFEISTOS DE TELA
#_________________________________________________________________________________________
def fade_screen(screen, color, fade_time):

    fade_surface = pygame.Surface((screen.get_width(), screen.get_height()))
    fade_surface.fill(color)
    alpha = 0
    increment = 255 / (fade_time * 60)

    for _ in range(int(fade_time * 60)):
        alpha += increment
        fade_surface.set_alpha(alpha)
        screen.blit(fade_surface, (0, 0))
        pygame.display.update()
        pygame.time.delay(int(500 / 60))


def draw_horizontal_gradient(surface, start_color, end_color):

    width = surface.get_width()
    height = surface.get_height()
    gradient_width = width // 2 + 30

    for x in range(gradient_width):
        ratio = x / gradient_width
        color = [
            int(start_color[i] * (1 - ratio) + end_color[i] * ratio)
            for i in range(3)
        ]
        color.append(int(255 * (1 - ratio)))
        pygame.draw.line(surface, color, (x, 0), (x, height))


def text_styles(text, font, surface, x, y, color_scheme, gradient=True, border=True, aura=True):
 
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect(topleft=(x, y))

    aura_colors = {
        'blue': (173, 216, 230),
        'red': (230, 173, 173),
    }
    if aura:
        aura_surface = font.render(text, True, aura_colors[color_scheme])
        surface.blit(aura_surface, (text_rect.x - 1, text_rect.y - 1))
        surface.blit(aura_surface, (text_rect.x + 1, text_rect.y - 1))
        surface.blit(aura_surface, (text_rect.x - 1, text_rect.y + 1))
        surface.blit(aura_surface, (text_rect.x + 1, text_rect.y + 1))

    border_colors = {
        'blue': (135, 206, 250),
        'red': (250, 135, 135),
        'purple': (255, 204, 255)
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
            'blue': [(100, 100, 255), (0, 0, 100), (0, 0, 255)],
            'red': [(255, 100, 100), (100, 0, 0), (255, 0, 0)],
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


def resize_draw_background(screen, background_image, screen_width, screen_height):
    """
    Redimensiona uma imagem de fundo para se ajustar à resolução da tela
    e a desenha centralizada na tela.
    """
    base_width, base_height = background_image.get_width(), background_image.get_height()
    scale_x, scale_y = scale(base_width, base_height, screen_width, screen_height)
    new_width = int(base_width * scale_x)
    new_height = int(base_height * scale_y)
    resized_image = pygame.transform.scale(background_image, (new_width, new_height))
    bg_x = (screen_width - resized_image.get_width()) // 2
    bg_y = (screen_height - resized_image.get_height()) // 2
    screen.blit(resized_image, (bg_x, bg_y))