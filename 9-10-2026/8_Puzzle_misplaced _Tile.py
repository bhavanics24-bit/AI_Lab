from heapq import heappush, heappop

start = (2, 8, 3, 1, 6, 4, 7, 0, 5)
goal = (1, 2, 3, 8, 0, 4, 7, 6, 5)

def heuristic(state):
    count = 0
    for i in range(9):
        if state[i] != 0 and state[i] != goal[i]:
            count += 1
    return count

def solve():
    open_list = []
    heappush(open_list, (heuristic(start), 0, start, []))
    visited = set()

    while open_list:
        f, g, state, path = heappop(open_list)

        if state in visited:
            continue
        visited.add(state)
        path = path + [state]

        if state == goal:
            for s in path:
                print(s[:3])
                print(s[3:6])
                print(s[6:])
                print()
            return

        zero = state.index(0)
        row, col = divmod(zero, 3)

        for move in [-3, 3, -1, 1]:
            new_pos = zero + move

            if new_pos < 0 or new_pos > 8:
                continue
            if move == -1 and col == 0:
                continue
            if move == 1 and col == 2:
                continue

            new_state = list(state)
            new_state[zero], new_state[new_pos] = (
                new_state[new_pos], new_state[zero]
            )
            new_state = tuple(new_state)

            if new_state not in visited:
                heappush(open_list, (
                    g + 1 + heuristic(new_state),
                    g + 1,
                    new_state,
                    path
                ))

solve()
