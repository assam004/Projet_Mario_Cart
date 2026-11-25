import pygame
import math

from constants import (
    CAR_ACCELERATION,
    CAR_WIDTH,
    CAR_HEIGHT,
    TILE_SIZE,
    CAR_MAX_SPEED,
    CAR_MAX_REVERSE_SPEED,
    CAR_AIR_FRICTION
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

    def update_position(self) -> None:
        """Met à jour la vitesse et la position."""

        # Applique les frottements de l'air
        self.speed *= CAR_AIR_FRICTION

        # Arrête la voiture si sa vitesse devient très faible
        if abs(self.speed) < 0.01:
            self.speed = 0

        # Met à jour la position verticale
        self.y += self.speed

    def build_sprite(self) -> pygame.Surface:
        """Crée l'image de la voiture."""

        surf = pygame.Surface((CAR_WIDTH, CAR_HEIGHT), pygame.SRCALPHA)

        pygame.draw.rect(
            surf,
            (255, 0, 0),
            (0, 0, CAR_WIDTH, CAR_HEIGHT),
            border_radius=5
        )

        return surf

    def get_rotated_sprite(self) -> tuple[pygame.Surface, pygame.Rect]:
        """Retourne l'image de la voiture avec son orientation."""

        rotated = pygame.transform.rotate(self.sprite, -self.angle)
        rect = rotated.get_rect(center=(int(self.x), int(self.y)))

        return rotated, rect