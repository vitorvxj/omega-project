# Cores
#________________________________________________________
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Configurações do Player
#________________________________________________________
PLAYER_WIDTH = 200
PLAYER_HEIGHT = 200
PLAYER_SPEED = 8
SHOOT_DELAY = 100

# Configurações dos tiros
#________________________________________________________
BULLET_WIDTH = 2
BULLET_HEIGHT = 32
BULLET_SPEED = 40

# Configurações do inimigo
#________________________________________________________
ENEMY_WIDTH = 150
ENEMY_HEIGHT = 120
ENEMY_SPEED = -5

# Configurações das estrelas
#________________________________________________________
NUM_STARS = 100
STAR_COLORS = [(135, 206, 235), (176, 224, 230), (173, 216, 230), (135, 206, 250)]
STAR_LEVELS = 5
STAR_SPEED = [1, 2, 4, 8, 16]

STAR_DARK_BLUE = (0, 0, 139) # [Backgroud Stars]
STAR_LIGHT_BLUE = (173, 216, 230) # [Backgroud Stars]

# Estado do jogo
#________________________________________________________
estado = "menu00"

# Inicializações do jogo
#________________________________________________________
initial_lives = 6
initial_shield = 6
player_lives = initial_lives
player_shield = initial_shield
score = 0

# Caminhos de arquivos
#________________________________________________________
font_path = r"C:\Users\joaov\OneDrive\Arquivos\Projeto OMEGA\Assets\interface\fonts\Neutra.ttf"

BACKGROUND_MUSIC_PATH = "C:/Users/joaov/OneDrive/Arquivos/Projeto OMEGA/Assets/level/OST/level.mp3"
MENU_MUSIC_PATH = "C:/Users/joaov/OneDrive/Arquivos/Projeto OMEGA/Assets/interface/OST/menu_theme.mp3"
BUTTON_SOUND_PATH = "C:/Users/joaov/OneDrive/Arquivos/Projeto OMEGA/Assets/interface/OST/button.wav"

SHOOT_SOUND_PATH = "C:/Users/joaov/OneDrive/Arquivos/Projeto OMEGA/Assets/effects/shoot player/OST/shoot.wav"
EXPLOSION_SOUND_PATH = "C:/Users/joaov/OneDrive/Arquivos/Projeto OMEGA/Assets/effects/explosion/OST/explosion.wav"

PLAYER_SPRITE_PATH_1 = "C:/Users/joaov/OneDrive/Arquivos/Projeto OMEGA/Assets/player/player sprite/Spartan00.png"
PLAYER_SPRITE_PATH_2 = "C:/Users/joaov/OneDrive/Arquivos/Projeto OMEGA/Assets/player/player sprite/Spartan01.png"

ENEMY_SPRITE_PATH = "C:/Users/joaov/OneDrive/Arquivos/Projeto OMEGA/Assets/enemy/enemy sprite/enemy_sprite.png"

AVATAR_IMAGE_PATH = "C:/Users/joaov/OneDrive/Arquivos/Projeto OMEGA/Assets/player/player avatar/Isis/Light Isis.png"

