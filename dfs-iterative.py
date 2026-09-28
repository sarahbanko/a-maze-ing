def adjacent(v: tuple, grid: list) -> list[tuple]:
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
    return edges

def dfs(config: dict) -> dict:
    grid = [(x, y) for x in range(config["WIDTH"]) for y in range(config["HEIGHT"])]
    parents = {}
    discovered = set()
    stack = []
    start = (0, 0)
    parents[start] = (start)
    stack.append(adjacent(start, grid))
    discovered.add(start)
    while stack:
        if stack[-1]:
            neighbor = stack[-1].pop()
            if neighbor not in discovered:
                discovered.add(neighbor)
                stack.append(adjacent(neighbor, grid))
                parents[stack.peek()] = neighbor
        else:
            stack.pop()
