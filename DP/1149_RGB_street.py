import sys
sys.stdin = open("1149_RGB_street_input.txt")


def backtracking(depth, prev, total):
    global result
    if depth == N:
        result = min(result, total)
        return

    for i in range(3):
        if i == prev:
            continue
        backtracking(depth + 1, i, total + arr[depth][i])


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [int(1e9)] * N
result = 1e9

backtracking(0, -1, 0)

print(result)
