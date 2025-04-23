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