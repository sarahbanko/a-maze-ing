def adjacent(v: tuple) -> list[tuple]:
    edges = []
    x, y = v

    if y - 1 >= 0 and (x, y - 1) in grid:
        edges.append((x, y - 1))

    if x + 1 < width and (x + 1, y) in grid:
        edges.append((x + 1, y))

    if y + 1 < height and (x, y + 1) in grid:
        edges.append((x, y + 1))

    if x - 1 >= 0 and (x - 1, y) in grid:
        edges.append((x - 1, y))

    return edges


if __name__ == "__main__":
    width = 3
    height = 3
    grid = [(x, y) for x in range(width) for y in range(height)]
    discovered = set()

    stack = []
    start = (0, 0)

    stack.append(adjacent(start))
    discovered.add(start)

    while stack:
        if stack[-1]:
            neighbor = stack[-1].pop()

            # doing down
            if neighbor not in discovered:
                discovered.add(neighbor)
                stack.append(adjacent(neighbor))
        else:
            stack.pop()

    for d in discovered:
        print(d)
