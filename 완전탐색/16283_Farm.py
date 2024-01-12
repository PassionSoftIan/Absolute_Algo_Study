import sys

sys.stdin = open("16283_input.txt")

a, b, n, w = map(int, input().split())

result = []

for count in range(1, n):
    if a * (n - count) + b * count == w:
        result.append([n - count, count])
        if len(result) > 1:
            print(-1)
            exit()

if not result:
    print(-1)
else:
    print(*result[0])