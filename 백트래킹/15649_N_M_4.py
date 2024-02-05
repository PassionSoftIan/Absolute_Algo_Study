import sys
sys.stdin = open("15649_N_M_4_input.txt")


def backtracking(depth, n, m, start):
    if depth == m:
        print(*result)
        return

    for i in range(start, n + 1):
        result.append(i)
        backtracking(depth + 1, n, m, i)
        result.pop()

N, M = map(int, input().split())

result = []

backtracking(0, N, M, 1)