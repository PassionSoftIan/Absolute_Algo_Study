import sys
sys.stdin = open("2304_container_polygon_input.txt")
# input = sys.stdin.readline

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

arr.sort()

result = 0

max_high = arr[0][1]
x = arr[0][0]

for i in range(N - 1):
    if arr[i][1] < arr[i+1][1]:
        result += (arr[i+1][0] - x) * max_high
        x = arr[i+1][0]
        max_high = arr[i+1][1]



print(arr)