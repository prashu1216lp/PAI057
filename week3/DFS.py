def water_jug_dfs(capA, capB, target):
    visited = set()

    def dfs(x, y):
        if (x, y) in visited:
            return False

        print("Visiting state:", (x, y))
        visited.add((x, y))

        # goal check
        if x == target or y == target:
            print("Target reached at state:", (x, y))
            return True

        # possible moves
        next_states = [
            (capA, y),          # Fill jug A
            (x, capB),          # Fill jug B
            (0, y),             # Empty jug A
            (x, 0),             # Empty jug B
            (x - min(x, capB - y), y + min(x, capB - y)),  # Pour A -> B
            (x + min(y, capA - x), y - min(y, capA - x))   # Pour B -> A
        ]

        for state in next_states:
            if dfs(state[0], state[1]):
                return True

        return False

    return dfs(0, 0)


# Example
capA = 4
capB = 3
target = 2

water_jug_dfs(capA, capB, target)

