import sys
sys.stdin = open("15649_N_M_2_input.txt")


def backtracking(depth, n, m, start):
    if depth == m:
        print(*result)
        return

    for i in range(start, n + 1):
        if i not in result:
            result.append(i)
            backtracking(depth + 1, n, m, i)
            result.pop()


N, M = map(int, input().split())

check = []
result = []

backtracking(0, N, M, 1)