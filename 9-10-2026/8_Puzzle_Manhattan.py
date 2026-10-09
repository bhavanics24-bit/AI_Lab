import heapq

start = (2, 8, 3,
         1, 6, 4,
         7, 0, 5)

goal = (1, 2, 3,
        8, 0, 4,
        7, 6, 5)


# Calculate Manhattan Distance
def manhattan(state):
    distance = 0

    for i in range(9):
        tile = state[i]

        if tile != 0:
            goal_pos = goal.index(tile)

            current_row = i // 3
            current_col = i % 3

            goal_row = goal_pos // 3
            goal_col = goal_pos % 3

            distance += abs(current_row - goal_row)
            distance += abs(current_col - goal_col)

    return distance


# Print puzzle
def display(state):
    for i in range(0, 9, 3):
        print(state[i], state[i + 1], state[i + 2])
    print()


# A* Search Algorithm
def solve():
    open_list = []
    heapq.heappush(
        open_list,
        (manhattan(start), 0, start, [start])
    )

    visited = set()

    while open_list:
        f, g, state, path = heapq.heappop(open_list)

        if state in visited:
            continue

        visited.add(state)

        if state == goal:
            print("Solution found!")
            print("Initial Manhattan Distance:", manhattan(start))
            print("Total moves:", len(path) - 1)
            print("\nSolution path:")

            for step, puzzle in enumerate(path):
                print("Step", step)
                display(puzzle)

            return

        blank = state.index(0)

        moves = [-3, 3, -1, 1]

        for move in moves:
            new_pos = blank + move

            if new_pos < 0 or new_pos >= 9:
                continue

            # Prevent moving across rows
            if move == -1 and blank % 3 == 0:
                continue

            if move == 1 and blank % 3 == 2:
                continue

            new_state = list(state)
            new_state[blank], new_state[new_pos] = (
                new_state[new_pos], new_state[blank]
            )

            new_state = tuple(new_state)

            if new_state not in visited:
                new_g = g + 1
                new_h = manhattan(new_state)
                new_f = new_g + new_h

                heapq.heappush(
                    open_list,
                    (new_f, new_g, new_state, path + [new_state])
                )

    print("No solution found!")


solve()
