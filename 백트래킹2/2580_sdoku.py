import sys
sys.stdin = open("2580_sdoku_input.txt")


def square(check, n, m):
    return


def row(check, n, m):
    return


def column(check, n, m):
    return


def backtracking(depth, n, m,):
    if depth <= 9:
        if square(go, n, m) and row(go, n, m) and column(go, n, m):

    for go in range(1, 10):


arr = [list(map(int, input().split())) for _ in range(9)]

check = 0

for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            backtracking(0, i, j)

for i in arr:
    print(*i)