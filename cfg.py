# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Configurações do Player
PLAYER_WIDTH = 200
PLAYER_HEIGHT = 200
PLAYER_SPEED = 8
SHOOT_DELAY = 100

# Configurações dos tiros
BULLET_WIDTH = 2
BULLET_HEIGHT = 32
BULLET_SPEED = 40

# Configurações do inimigo
ENEMY_WIDTH = 150
ENEMY_HEIGHT = 120
ENEMY_SPEED = -5

# Configurações das estrelas
NUM_STARS = 100
STAR_COLORS = [(135, 206, 235), (176, 224, 230), (173, 216, 230), (135, 206, 250)]
STAR_LEVELS = 5
STAR_SPEED = [1, 2, 4, 8, 16]

STAR_DARK_BLUE = (0, 0, 139) # [Backgroud Stars]
STAR_LIGHT_BLUE = (173, 216, 230) # [Backgroud Stars]

# Estado do jogo
estado = "menu00"

# Inicializações do jogo
initial_lives = 6
initial_shield = 6
player_lives = initial_lives
player_shield = initial_shield
score = 0

# Caminhos de arquivos
font_path = r"C:\Users\joaov\Desktop\Projeto OMEGA\Assets\Fonts\Neutra.ttf"

BACKGROUND_MUSIC_PATH = "C:/Users/joaov/Desktop/Projeto OMEGA/Assets/OST/background_music.mp3"
MENU_MUSIC_PATH = "C:/Users/joaov/Desktop/Projeto OMEGA/Assets/OST/menu_music.mp3"
BUTTON_SOUND_PATH = "C:/Users/joaov/Desktop/Projeto OMEGA/Assets/OST/button_sound.wav"

SHOOT_SOUND_PATH = "C:/Users/joaov/Desktop/Projeto OMEGA/Assets/OST/shoot.wav"
EXPLOSION_SOUND_PATH = "C:/Users/joaov/Desktop/Projeto OMEGA/Assets/OST/explosion.wav"

PLAYER_SPRITE_PATH_1 = "C:/Users/joaov/Desktop/Projeto OMEGA/Assets/PLAYER/Spartan00.png"
PLAYER_SPRITE_PATH_2 = "C:/Users/joaov/Desktop/Projeto OMEGA/Assets/PLAYER/Spartan01.png"

ENEMY_SPRITE_PATH = "C:/Users/joaov/Desktop/Projeto OMEGA/Assets/INIMIGOS/enemy_sprite.png"

AVATAR_IMAGE_PATH = "C:/Users/joaov/Desktop/Projeto OMEGA/Assets/AVATAR/Isis/Light Isis.png"

