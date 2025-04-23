import pygame

from cfg import *
from screen import (

    scale_rect, scale, tick_rate, fade_screen, draw_horizontal_gradient,
    text_styles, resize_draw_background
    
)

pygame.mixer.init()
button_sound = pygame.mixer.Sound("c:/Users/joaov/OneDrive/Arquivos/Projeto OMEGA/Assets/interface/OST/button.wav")


# TELA GAME OVER MENU01
#_________________________________________________________________________________________
class menu01:

    def game_over(self, screen, screen_width, screen_height):
        global start_button, return_button

        pygame.mixer.music.load(MENU_MUSIC_PATH)
        pygame.mixer.music.play(-1)

        over_running = True
        clock = pygame.time.Clock()

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


            font = pygame.font.Font(font_path, int(80 * (screen_width / 1920)))
            text_styles(

                "GAME OVER!!!", font, screen,
                int(screen_width // 20), int(screen_height // 2 - 60),
                color_scheme='red', gradient=True, border=True, aura=True

            )

            font = pygame.font.Font(font_path, int(30 * (screen_width / 1920)))
            start_button = scale_rect(pygame.Rect(100, 920, 200, 44))
            return_button = scale_rect(pygame.Rect(100, 980, 200, 44))
            text_styles("Decolar", font, screen, start_button.x, start_button.y, color_scheme='red', gradient=True, border=True, aura=True)
            text_styles("Voltar", font, screen, return_button.x, return_button.y, color_scheme='red', gradient=True, border=True, aura=True)

            pygame.display.flip()
            tick_rate(clock)


# TELA INICIAL MENU00
#_________________________________________________________________________________________
class menu00:

    def main_menu(self, screen, screen_width, screen_height):
        global background_image

        pygame.mixer.music.load(MENU_MUSIC_PATH)
        pygame.mixer.music.play(-1)
        background_image = pygame.image.load("c:/Users/joaov/OneDrive/Arquivos/Projeto OMEGA/Assets/interface/background/menu_home.png").convert()

        menu_running = True
        clock = pygame.time.Clock()

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

            resize_draw_background(screen, background_image, screen_width, screen_height)

            gradient_surface = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
            draw_horizontal_gradient(gradient_surface, (0, 0, 0), (0, 0, 0, 0))
            screen.blit(gradient_surface, (0, 0))

            font = pygame.font.Font(font_path, int(80 * (screen_width / 1920)))
            text_styles(

                "SPEED NAVY ULTRA", font, screen,
                int(screen_width // 20), int(screen_height // 2 - 60),
                color_scheme='blue', gradient=True, border=True, aura=True
            )

            font = pygame.font.Font(font_path, int(30 * (screen_width / 1920)))
            start_button = scale_rect(pygame.Rect(100, 920, 200, 44))
            quit_button = scale_rect(pygame.Rect(100, 980, 200, 44))
            text_styles("Decolar", font, screen, start_button.x, start_button.y, color_scheme='blue', gradient=True, border=True, aura=True)
            text_styles("Sair", font, screen, quit_button.x, quit_button.y, color_scheme='blue', gradient=True, border=True, aura=True)

            pygame.display.flip()
            tick_rate(clock)
