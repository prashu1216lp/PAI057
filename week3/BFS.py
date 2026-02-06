from collections import deque

def water_jug_bfs(capA, capB, target):
    visited = set()
    queue = deque()

    # start state
    queue.append((0, 0))
    visited.add((0, 0))

    while queue:
        x, y = queue.popleft()

        # check goal
        if x == target or y == target:
            print("Target reached at state:", (x, y))
            return True

        # all possible next states
        next_states = [
            (capA, y),          # Fill jug A
            (x, capB),          # Fill jug B
            (0, y),             # Empty jug A
            (x, 0),             # Empty jug B
            (x - min(x, capB - y), y + min(x, capB - y)),  # Pour A -> B
            (x + min(y, capA - x), y - min(y, capA - x))   # Pour B -> A
        ]

        for state in next_states:
            if state not in visited:
                visited.add(state)
                queue.append(state)

    print("Target not reachable")
    return False


# Example
capA = 4
capB = 3
target = 2

water_jug_bfs(capA, capB, target)
