import sys
sys.stdin = open("1759_making_password_input.txt")


def backtracking(depth, start):
    if depth == L:
        count = 0
        for ck in check:
            if ck in bowls:
                count += 1
        if L - count >= 2 and count > 0:
            print(*check, sep="")
        return

    for i in range(start, C):
        check.append(arr[i])
        backtracking(depth + 1, i+1)
        check.pop()


L, C = map(int, input().split())

arr = sorted(list(map(str, input().split())))

check = []

bowls = ['a', 'e', 'i', 'o', 'u']

# print(arr)

backtracking(0, 0)