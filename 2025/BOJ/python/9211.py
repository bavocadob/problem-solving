import sys


def solve():
    N, l, t = map(int, input().split())

    forces = list(map(float, input().split()))
    adj_out = [[] for _ in range(N)]
    A = [0.0] * N
    adj = [set() for _ in range(N)]

    for _ in range(l):
        s, t_dest, p = input().split()
        s, t_dest, p = int(s), int(t_dest), float(p)

        adj_out[s].append((t_dest, p))
        A[s] += p

        adj[s].add(t_dest)
        adj[t_dest].add(s)

    for _ in range(t):
        next_forces = [0.0] * N
        for i in range(N):
            remain = forces[i] * (1.0 - A[i])
            next_forces[i] += remain

            for neighbor, proportion in adj_out[i]:
                temp_move = forces[i] * proportion
                next_forces[neighbor] += temp_move

        forces = next_forces

    min_force = float('inf')

    for i in range(N):
        temp_force = forces[i]

        for neighbor in adj[i]:
            temp_force += forces[neighbor]

        min_force = min(min_force, temp_force)

    if min_force == float('inf'):
        print(0.0)
    else:
        print(min_force)


def main():
    T = int(input())
    for _ in range(T):
        solve()


if __name__ == "__main__":
    main()
