N = 8

def heuristic(s):
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            if s[i] == s[j] or abs(s[i]-s[j]) == abs(i-j):
                count += 1
    return count

def hill_climbing():
    s = [0, 4, 7, 5, 2, 6, 1, 3]
    step = 1

    while True:
        cost = heuristic(s)
        print("Step", step)
        print("State:", s)
        print("Attacking pairs:", cost)

        if cost == 0:
            print("Goal reached!")
            break

        best = s[:]
        best_h = cost

        for c in range(N):
            for r in range(N):
                t = s[:]
                t[c] = r
                if r != s[c] and heuristic(t) < best_h:
                    best = t
                    best_h = heuristic(t)

        if best_h >= cost:
            print("Local minimum reached.")
            break

        print("Queen moved to get a better state.")
        s = best
        step += 1

hill_climbing()
