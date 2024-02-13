import sys
sys.stdin = open("2304_container_polygon_input.txt")
# input = sys.stdin.readline

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

arr.sort()

result = 0

max_high = arr[0][1]
max_high_idx = 0
x = arr[0][0]

for i in range(1, N):
    if max_high <= arr[i][1]:
        result += (arr[i][0] - x) * max_high
        x = arr[i][0]
        max_high = arr[i][1]
        max_high_idx = i

max_high = arr[-1][1]
x = arr[-1][0]

for i in range(N-1, max_high_idx - 1, -1):
    if max_high <= arr[i][1]:
        result += (x - arr[i][0]) * max_high
        x = arr[i][0]
        max_high = arr[i][1]

result += max_high

print(result)