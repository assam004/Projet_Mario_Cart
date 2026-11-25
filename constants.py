WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 768
FPS = 60

TILE_SIZE = 64
GRID_COLS = 16
GRID_ROWS = 12

# Paramètres physiques de la voiture
CAR_ACCELERATION = 0.05

# Limite de vitesse en marche avant et arrière
CAR_MAX_SPEED = 6
CAR_MAX_REVERSE_SPEED = 3

# Frottement de l'air : la vitesse diminue progressivement
CAR_AIR_FRICTION = 0.985

# Dimensions de la voiture
CAR_WIDTH = 30
CAR_HEIGHT = 50

# Vitesse de rotation de la voiture (degrés par frame)
CAR_TURN_SPEED = 2


class GameState:
    MENU = "menu"
    RACING = "racing"


# --- Couleurs UI ---
COLOR_BG = (15, 15, 25)
COLOR_TEXT = (240, 240, 240)
COLOR_ACCENT = (255, 200, 0)
COLOR_PANEL = (30, 30, 50)
COLOR_PANEL_BORDER = (60, 60, 100)
