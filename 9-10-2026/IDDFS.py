graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}


def DLS(node, goal, depth, path):
    print(node, end=" ")

    if node == goal:
        path.append(node)
        return True

    if depth == 0:
        return False

    for child in graph[node]:
        path.append(node)

        if DLS(child, goal, depth - 1, path):
            return True

        path.pop()

    return False


def IDDFS(start, goal):
    depth = 0

    while True:
        path = []
        print("\n\nIteration", depth + 1)
        print("Depth limit:", depth)
        print("Nodes visited:", end=" ")

        if DLS(start, goal, depth, path):
            print("\nGoal found!")
            print("Path:", " -> ".join(path))
            break

        print("\nGoal not found.")
        depth += 1


IDDFS('A', 'G')
