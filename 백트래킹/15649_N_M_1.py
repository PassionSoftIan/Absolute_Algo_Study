import sys
sys.stdin = open("15649_N_M_1_input.txt")


def backtracking(depth, n, m):
    if depth == m:
        print(*result)
        return

    for i in range(1, n+1):
        if i not in result:
            result.append(i)
            backtracking(depth+1, n, m)
            result.pop()


N, M = map(int, input().split())

result = []

backtracking(0, N, M)