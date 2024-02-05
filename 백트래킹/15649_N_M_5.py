import sys
sys.stdin = open("15649_N_M_5_input.txt")


def backtracking(depth, n, m):
    if depth == m:
        print(*result)
        return

    for i in range(n):
        if visited[i] == 0:
            result.append(arr[i])
            visited[i] = 1
            backtracking(depth + 1, n, m)
            result.pop()
            visited[i] = 0


N, M = map(int, input().split())

arr = sorted(list(map(int, input().split())))

result = []
visited = [0] * N

backtracking(0, N, M)