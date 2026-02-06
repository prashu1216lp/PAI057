import heapq

# Goal state
GOAL = ((1, 2, 3),
        (4, 5, 6),
        (7, 8, 0))

# Directions for moving blank tile
MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def manhattan(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                goal_x = (value - 1) // 3
                goal_y = (value - 1) % 3
                distance += abs(i - goal_x) + abs(j - goal_y)
    return distance

def get_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def get_neighbors(state):
    neighbors = []
    x, y = get_blank(state)

    for dx, dy in MOVES:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [list(row) for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(tuple(tuple(row) for row in new_state))

    return neighbors

def a_star(start):
    pq = []
    heapq.heappush(pq, (manhattan(start), 0, start, []))
    visited = set()

    while pq:
        f, g, state, path = heapq.heappop(pq)

        if state in visited:
            continue

        visited.add(state)
        path = path + [state]

        if state == GOAL:
            return path

        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                h = manhattan(neighbor)
                heapq.heappush(pq, (g + 1 + h, g + 1, neighbor, path))

    return None


# Example start state
start_state = ((1, 2, 3),
               (4, 0, 6),
               (7, 5, 8))

solution = a_star(start_state)

if solution:
    print("Solution found in", len(solution) - 1, "moves:\n")
    for step in solution:
        for row in step:
            print(row)
        print()
else:
    print("No solution exists")
