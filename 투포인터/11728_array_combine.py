import sys

sys.stdin = open("11728_array_combine_input.txt")

N, M = map(int, input().split())

arr = list(map(int, input().split()))

temp = list(map(int, input().split()))

for num in temp:
    arr.append(num)

arr.sort()

print(*arr)