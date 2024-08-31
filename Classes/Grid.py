from typing import NamedTuple

class Tile(NamedTuple):
    """
    Representación de un tile usando coordenadas axiales: q + r + s = 0 -> s = -q - r

    Tres formas de definir adyacencia dado diff = a - b:
    # (abs(diff.q) + abs(diff.r) + abs(diff.q + diff.r)) == 2
    # diff in [Tile(1, 0), Tile(0, 1), Tile(-1, 1), Tile(-1, 0), Tile(0, -1), Tile(1, -1)]
    # diff.q in (-1, 0, 1) and diff.r in (-1, 0, 1) and diff.q != diff.r
    """
    q: int
    r: int

    def __sub__(self, other):
        return Tile(self.q - other.q, self.r - other.r)

    def __add__(self, other):
        return Tile(self.q + other.q, self.r + other.r)

    def adjacent_tiles(self):
        return [self + d for d in [Tile(1, 0), Tile(0, 1), Tile(-1, 1), Tile(-1, 0), Tile(0, -1), Tile(1, -1)]]

    def is_adjacent(self, other):
        diff = self - other
        return (abs(diff.q) + abs(diff.r) + abs(diff.q + diff.r)) == 2

    def move(self, direction):
        if isinstance(direction, str):
            direction = {
                "r": Tile(0, 1),
                "br": Tile(1, 0),
                "bl": Tile(1, -1),
                "l": Tile(0, -1),
                "tl": Tile(-1, 0),
                "tl": Tile(-1, 1)
            }[direction]
        return self + direction


class Grid:
    """
    Clase que representa un grid hexagonal y contiene la funcionalidad necesaria para trabajar con este.
    """
    def __init__(self, radius):
        self.radius = radius
        self.marks = [] # utilizado para debuggear principalmente
        self.tiles = []
        for q in range(-self.radius, self.radius + 1):
            for r in range(max(-self.radius, -q - self.radius), min(self.radius, -q + self.radius) + 1):
                self.tiles.append(Tile(q, r))

    def is_inside(self, tile: Tile) -> bool:
        return tile in self.tiles

    def __str__(self):
        """
        Devuelve una representación grafica en ascii del grid
        """
        # TODO: esto es muy mejorable. Lo de tener 3 fors es un poco feo
        res = ""
        for q in range(-self.radius, self.radius + 1):
            line_start = "\n" + " " * 3 * (self.radius + abs(q))
            hrange = range(max(-self.radius, -q - self.radius), min(self.radius, -q + self.radius) + 1)
            
            res += line_start
            for r in hrange:
                res += f"╔     ╗" if Tile(q, r) in self.marks else f"┌     ┐"

            res += line_start
            for r in hrange:
                # este lio es para que todos los números de una unidad siempre tengan la misma longitud
                q_string = f" {q}" if q >= 0 else f"{q}"
                r_string = f" {r}" if r >= 0 else f"{r}"
                # res += f"│{q_string},{r_string}│" 
                res += f"║{q_string},{r_string}║" if Tile(q, r) in self.marks else f"│{q_string},{r_string}│"

            res += line_start
            for r in hrange:
                res += f"╚     ╝" if Tile(q, r) in self.marks else f"└     ┘"

        return res