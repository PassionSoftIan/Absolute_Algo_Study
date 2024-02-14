import sys
sys.stdin = open("1149_RGB_street_input.txt")


def backtracking(depth, prev):
    if depth == N:
        return 0

    if dp[depth][prev] != -1:
        return dp[depth][prev]

    min_cost = int(1e9)

    for i in range(3):
        if i == prev:
            continue
        cost = arr[depth][i] + backtracking(depth + 1, i)
        min_cost = min(min_cost, cost)

    dp[depth][prev] = min_cost
    return dp[depth][prev]


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1] * 3 for _ in range(N)]


print(backtracking(0, -1))