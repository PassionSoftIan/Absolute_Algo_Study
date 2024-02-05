import sys
sys.stdin = open("15649_N_M_7_input.txt")


def backtracking(depth, n, m):
    if depth == m:
        print(*result)
        return

    for i in range(n):
        result.append(arr[i])
        backtracking(depth + 1, n, m)
        result.pop()


N, M = map(int, input().split())

arr = sorted(map(int, input().split()))

result = []

backtracking(0, N, M)