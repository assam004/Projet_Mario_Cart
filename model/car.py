import pygame
import math

from constants import (
    CAR_ACCELERATION,
    CAR_WIDTH,
    CAR_HEIGHT,
    TILE_SIZE,
    CAR_MAX_SPEED,
    CAR_MAX_REVERSE_SPEED,
    CAR_AIR_FRICTION,
    CAR_TURN_SPEED
)


class Car:
    """Représente une voiture et gère ses déplacements."""

    def __init__(self, start_col: int, start_row: int):
        """Initialise la position et les propriétés de la voiture."""

        # Position de départ au centre de la case
        self.x = start_col * TILE_SIZE + TILE_SIZE // 2
        self.y = start_row * TILE_SIZE + TILE_SIZE // 2

        # Vitesse et orientation initiales
        self.speed: float = 0.0
        self.angle: float = 0.0

        # Création de l'image de la voiture
        self.sprite = self.build_sprite()

    def accelerate(self) -> None:
        """Augmente la vitesse de la voiture."""

        self.speed += CAR_ACCELERATION

        # Limite la vitesse maximale en marche avant
        self.speed = min(self.speed, CAR_MAX_SPEED)

    def brake(self) -> None:
        """Freine la voiture ou la fait reculer."""

        self.speed -= CAR_ACCELERATION

        # Limite la vitesse maximale en marche arrière
        self.speed = max(self.speed, -CAR_MAX_REVERSE_SPEED)

    def turn_left(self) -> None:
        """Tourne la voiture vers la gauche."""

        # Augmente l'angle de la voiture
        self.angle -= CAR_TURN_SPEED

    def turn_right(self) -> None:
        """Tourne la voiture vers la droite."""

        # Diminue l'angle de la voiture
        self.angle += CAR_TURN_SPEED

    def update_position(self) -> None:
        """Met à jour la vitesse et la position de la voiture."""

        # Applique les frottements de l'air
        self.speed *= CAR_AIR_FRICTION

        # Arrête la voiture si sa vitesse est très faible
        if abs(self.speed) < 0.01:
            self.speed = 0

        # Convertit l'angle en radians
        angle_rad = math.radians(self.angle)

        # Calcule le déplacement selon l'orientation de la voiture
        self.x -= math.sin(angle_rad) * self.speed
        self.y += math.cos(angle_rad) * self.speed

    def build_sprite(self) -> pygame.Surface:
        """Crée l'image de la voiture avec un avant et un arrière visibles."""

        surf = pygame.Surface((CAR_WIDTH, CAR_HEIGHT), pygame.SRCALPHA)

        # Carrosserie rouge
        pygame.draw.rect(
            surf, (255, 0, 0),
            (0, 0, CAR_WIDTH, CAR_HEIGHT),
            border_radius=5
        )

        # Pare-brise bleu à l'avant de la voiture
        pygame.draw.rect(
            surf, (100, 200, 255),
            (5, CAR_HEIGHT - 17, CAR_WIDTH - 10, 10),
            border_radius=2
        )

        # Phares avant jaunes
        pygame.draw.rect(surf, (255, 255, 0), (3, CAR_HEIGHT - 5, 6, 4))
        pygame.draw.rect(surf, (255, 255, 0), (CAR_WIDTH - 9, CAR_HEIGHT - 5, 6, 4))

        # Feux arrière noirs
        pygame.draw.rect(surf, (50, 50, 50), (3, 2, 6, 4))
        pygame.draw.rect(surf, (50, 50, 50), (CAR_WIDTH - 9, 2, 6, 4))

        return surf

    def get_rotated_sprite(self) -> tuple[pygame.Surface, pygame.Rect]:
        """Retourne l'image de la voiture avec son orientation."""

        rotated = pygame.transform.rotate(self.sprite, -self.angle)
        rect = rotated.get_rect(center=(int(self.x), int(self.y)))

        return rotated, rect