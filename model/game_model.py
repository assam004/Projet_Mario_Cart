from constants import GameState, GRID_ROWS, GRID_COLS
from model.car import Car
from model.circuit import Circuit
from model.road_tile import RoadTile
from model.terrain import Road, Grass, Dirt, Ice, Void


class GameModel:

    def __init__(self):
        self.state: str = GameState.MENU
        self.circuit: Circuit | None = None
        self.car: Car | None = None


    def load_circuit(self) -> None:
        """Crée un circuit composé de différents terrains."""

        grid = []

        for row_idx in range(GRID_ROWS):
            row = []

            for col_idx in range(GRID_COLS):

                if row_idx == 0 or row_idx == GRID_ROWS - 1:
                    terrain = Void()

                elif col_idx == 0 or col_idx == GRID_COLS - 1:
                    terrain = Void()

                elif 1 <= row_idx <= 3:
                    terrain = Road()

                elif 4 <= row_idx <= 5:
                    terrain = Grass()

                elif 6 <= row_idx <= 8:
                    terrain = Dirt()

                else:
                    terrain = Ice()

                tile = RoadTile(col_idx, row_idx, terrain)
                row.append(tile)

            grid.append(row)

        self.circuit = Circuit(grid=grid)
        self.spawn_car()

    def spawn_car(self) -> None:
        self.car = Car(7, 1)

    def update(self) -> None:
        if self.state != GameState.RACING or self.circuit is None:
            return
        self.car.update_position()
