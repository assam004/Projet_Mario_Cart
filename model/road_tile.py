import pygame
from constants import TILE_SIZE
from model.terrain import Terrain, Road


class RoadTile:

    def __init__(self, col: int, row: int, terrain: Terrain | None = None):
        self.col = col
        self.row = row
        self.sprite: pygame.Surface | None = None

        if terrain is None:
            self.terrain = Road()
        else:
            self.terrain = terrain 

    def get_sprite(self, tile_size: int = TILE_SIZE) -> pygame.Surface:
        if self.sprite and self.sprite.get_width() == tile_size:
            return self.sprite
        surface = pygame.Surface((tile_size, tile_size))
        surface.fill(self.terrain.color)
        pygame.draw.rect(surface, (60, 60, 70), surface.get_rect(), 2)

        self.sprite = surface
        return self.sprite
