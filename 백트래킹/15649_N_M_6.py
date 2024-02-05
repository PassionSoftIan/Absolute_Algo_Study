import sys
sys.stdin = open("15649_N_M_6_input.txt")


def backtracking(depth, n, m, start):
    if depth == m:
        print(*result)
        return

    for i in range(start, n):
        result.append(arr[i])
        backtracking(depth + 1, n, m, i + 1)
        result.pop()


N, M = map(int, input().split())

arr = sorted(list(map(int, input().split())))

result = []

backtracking(0, N, M, 0)