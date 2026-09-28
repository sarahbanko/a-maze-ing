from collections import deque

if __name__ == "__main__":
    height = 3
    width = 3

    visited = set()
    parents = {}
    queue = deque()

    grad = [(x, y) for x in range(width) for y in range(height)]
    start = (0, 0)
    queue.append(start)
    visited.add(start)
    parents[start] = (start)

    while queue:
        x, y = queue.popleft()

        if (y - 1) >= 0 and (x, y - 1) in grad:
            if (x, y - 1) not in visited:
                queue.append((x, y - 1))
                visited.add((x, y - 1))
                parents[(x, y - 1)] = (x, y)

        if (y + 1) < height and (x, y + 1) in grad:
            if (x, y + 1) not in visited:
                queue.append((x, y + 1))
                visited.add((x, y + 1))
                parents[(x, y + 1)] = (x, y)

        if (x - 1) >= 0 and (x - 1, y) in grad:
            if (x - 1, y) not in visited:
                queue.append((x - 1, y))
                visited.add((x - 1, y))
                parents[(x - 1, y)] = (x, y)

        if (x + 1) < width and (x + 1, y) in grad:
            if (x + 1, y) not in visited:
                queue.append((x + 1, y))
                visited.add((x + 1, y))
                parents[(x + 1, y)] = (x, y)

    for k, v in parents.items():
        print(f" {k} is {v} parent")
