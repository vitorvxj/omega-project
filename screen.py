import pygame

# Configurações da tela
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.SRCALPHA)
screen_width, screen_height = screen.get_size()

resolucoes = {

    "HD": (1280, 720),
    "Full HD": (1920, 1080),
    "2K": (2560, 1440),
    "4K": (3840, 2160)

}

def mudar_resolucao(screen, resolucao):
    screen = pygame.display.set_mode(resolucao, pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.HWSURFACE)
    return screen

def escalonar_elementos(nova_resolucao, resolucao_atual, elementos):
    
    fator_largura = nova_resolucao[0] / resolucao_atual[0]
    fator_altura = nova_resolucao[1] / resolucao_atual[1]
    elementos_escalonados = []
    
    for elemento in elementos:
        elemento_escalonado = {

            "posicao": (elemento["posicao"][0] * fator_largura, elemento["posicao"][1] * fator_altura),
            "tamanho": (elemento["tamanho"][0] * fator_largura, elemento["tamanho"][1] * fator_altura)

        }
        elementos_escalonados.append(elemento_escalonado)
    
    return elementos_escalonados