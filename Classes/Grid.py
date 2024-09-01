import itertools as it
import functools as ft
import operator as op

class Tile:
    """
    Representación de un tile usando coordenadas axiales: q + r + s = 0 -> s = -q - r

    Tres formas de definir adyacencia dado diff = a - b:
    # (abs(diff.q) + abs(diff.r) + abs(diff.q + diff.r)) == 2
    # diff in [Tile(1, 0), Tile(0, 1), Tile(-1, 1), Tile(-1, 0), Tile(0, -1), Tile(1, -1)]
    # diff.q in (-1, 0, 1) and diff.r in (-1, 0, 1) and diff.q != diff.r
    """
    def __init__(self, q:  int, r: int):
        self.q: int = q
        self.r: int = r
        self.s: int = -q - r

    @classmethod
    def get_all_adjacent(cls, tiles: set['Tile']) -> set['Tile']:
        """
        Devuelve la intersección de los tiles adyacentes a todos los tiles en el set.
        """
        adjacent_list: list[set[Tile]] = [t.adjacent_tiles() for t in tiles]
        adjacent_intersect: set[Tile] = ft.reduce(op.and_, adjacent_list)
        return adjacent_intersect
        
    @classmethod
    def are_all_adjacent(cls, tiles: set['Tile']) -> bool:
        """
        Comprueba si todos los tiles en el set son adyacentes entre sí.
        """
        if len(tiles) == 1:
            raise ValueError("More than one tile is needed to check adjacency")

        if len(tiles) > 3:
            return False

        return all(t1.is_adjacent(t2) or t1 == t2 for t1 in tiles for t2 in tiles)

    def __str__(self):
        return f"({self.q}, {self.r})"

    def __eq__(self, other):
        return self.q == other.q and self.r == other.r

    def __sub__(self, other):
        return Tile(self.q - other.q, self.r - other.r)

    def __add__(self, other):
        return Tile(self.q + other.q, self.r + other.r)

    def __hash__(self):
        return hash((self.q, self.r))

    def adjacent_tiles(self):
        return set(self + d for d in {Tile(1, 0), Tile(0, 1), Tile(-1, 1), Tile(-1, 0), Tile(0, -1), Tile(1, -1)})

    def adjacent_edges(self):
        return set(Edge({self, t}) for t in self.adjacent_tiles())

    def adjacent_vertexes(self): # TODO: mejorable
        res = set()
        adjacent = self.adjacent_tiles()
        for t1 in adjacent:
            for t2 in adjacent:
                if t1.is_adjacent(t2):
                    res.add(Vertex({self, t1, t2}))
        return res


    def is_adjacent(self, other): # TODO: test
        if isinstance(other, Tile):
            return self in other.adjacent_tiles()

        if isinstance(other, Edge):
            return self in other

        if isinstance(other, Vertex):
            return self in other

    def move(self, direction): # TODO: test
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

class Edge(frozenset):
    """
    Representación de un edge. Un edge es una arista que conecta dos tiles.
    """
    def __init__(self, *initial_values):
        if len(*initial_values) != 2:
            raise ValueError("Edge must have 2 tiles")

        if not Tile.are_all_adjacent(*initial_values): 
            raise ValueError("Tiles are not adjacent")

        frozenset.__init__(initial_values)

    def __str__(self):
        ret = "Edge: "
        for t in self:
            ret += f"{t} "
        return ret

    def adjacent_tiles(self) -> set[Tile]:
        return set(self)

    def adjacent_edges(self) -> set['Edge']:
        """
        Un edge A es adyacente A un edge B siempre y cuando:
        - A y B compartan un tile
        - El nuevo tile sea adyacente a los dos tiles de A

        Sin tener en cuenta los limites del grid, un edge tiene 4 edges adyacentes
        """
        adjacent_intersect = Tile.get_all_adjacent(set(self))
        return set(Edge(a,b) for a,b in it.product(adjacent_intersect, self))

    def adjacent_vertexes(self) -> set['Vertex']:
        """
        Un vertex V es adyacente a un edge E siempre y cuando:
        - V comparta dos tiles con E
        - El tercer tile de V sea adyacente a los dos tiles de E

        Sin tener en cuenta los limtes del grid, un edge tiene 2 vertexes adyacentes
        """
        adjacent_intersect = Tile.get_all_adjacent(set(self))
        return set(Vertex(a,b,c) for a,b,c in it.combinations(adjacent_intersect, 3))

class Vertex(frozenset):

    def __init__(self, *initial_values):
        if len(*initial_values) != 3:
            raise ValueError("Vertex must have 3 tiles")

        if not Tile.are_all_adjacent(*initial_values): 
            raise ValueError("Tiles are not adjacent")

        frozenset.__init__(initial_values)

    def __str__(self):
        ret = "Vertex: "
        for t in self:
            ret += f"{t} "
        return ret

    def adjacent_tiles(self) -> set[Tile]:
        return set(self)

    # def adjacent_edges(self) -> set[Edge]: # TODO
    #     return set(it.combinations(self.tiles, 2))

    # def adjacent_vertexes(self): #TODO
        


class Grid:
    """
    Clase que representa un grid hexagonal y contiene la funcionalidad necesaria para trabajar con este.
    No almacena atributos, para esto se usara un 
    wrapper.
    """
    def __init__(self, radius):
        self.radius = radius
        self.marks = set() # utilizado para debuggear principalmente
        self.tiles = set()
        for q in range(-self.radius, self.radius + 1):
            for r in range(max(-self.radius, -q - self.radius), min(self.radius, -q + self.radius) + 1):
                self.tiles.add(Tile(q, r))

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