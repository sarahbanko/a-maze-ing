import random
from config_parser import load_config

NORTH = 1 << 0
EAST = 1 << 1
SOUTH = 1 << 2
WEST = 1 << 3
ALL_WALLS = 0b1111

def adjacent(
    v: tuple[int, int],
    grid: list[tuple[int, int]],
    rng: random.Random
) -> list[tuple[int, int]]:
    edges = []
    x, y = v
    if (x, y - 1) in grid:
        edges.append((x, y - 1))
    if (x + 1, y) in grid:
        edges.append((x + 1, y))
    if (x, y + 1) in grid:
        edges.append((x, y + 1))
    if (x - 1, y) in grid:
        edges.append((x - 1, y))
    rng.shuffle(edges)
    return edges


def carve_passage(
    current: tuple[int, int],
    neighbor: tuple[int, int],
    walls: dict[tuple[int, int], int]
) -> None:
    x, y = current
    if neighbor == (x, y - 1):
        walls[current] &= ~NORTH
        walls[neighbor] &= ~SOUTH
    elif neighbor == (x + 1, y):
        walls[current] &= ~EAST
        walls[neighbor] &= ~WEST
    elif neighbor == (x, y + 1):
        walls[current] &= ~SOUTH
        walls[neighbor] &= ~NORTH
    elif neighbor == (x - 1, y):
        walls[current] &= ~WEST
        walls[neighbor] &= ~EAST


def dfs(config: dict) -> dict[tuple[int, int], int]:
    width = config["WIDTH"]
    height = config["HEIGHT"]
    seed = config["SEED"]
    rng = random.Random(seed)
    grid = [
        (x, y)
        for x in range(width)
        for y in range(height)
    ]
    parents = {}
    discovered = set()
    stack = []
    walls = {
        cell: ALL_WALLS
        for cell in grid
    }
    start = (0, 0)
    current = start
    parents[start] = start
    discovered.add(start)
    stack.append(adjacent(start, grid, rng))
    while stack:
        if stack[-1]:
            neighbor = stack[-1].pop()
            if neighbor not in discovered:
                parents[neighbor] = current
                carve_passage(current, neighbor, walls)
                discovered.add(neighbor)
                stack.append(
                    adjacent(neighbor, grid, rng)
                )
                current = neighbor
        else:
            stack.pop()
            if current != start:
                current = parents[current]
    return walls

def print_maze(
    walls: dict[tuple[int, int], int],
    width: int,
    height: int
) -> None:

    # teto do labirinto
    print("+" + "---+" * width)

    for y in range(height):
        middle = "|"
        bottom = "+"

        for x in range(width):
            cell = walls[(x, y)]

            # conteúdo da célula
            middle += "   "

            # parede EAST
            if cell & EAST:
                middle += "|"
            else:
                middle += " "

            # parede SOUTH
            if cell & SOUTH:
                bottom += "---+"
            else:
                bottom += "   +"

        print(middle)
        print(bottom)

if __name__ == "__main__":
    config = load_config("config.txt")
    print_maze(dfs(config), config["WIDTH"], config["HEIGHT"])