import sys
sys.stdin = open("1912_continuity_sum_input.txt")

N = int(input())

arr = list(map(int, input().split()))

prefix_sum = [0] * (N + 1)

for go in range(N):
    prefix_sum[go + 1] = prefix_sum[go] + arr[go]

max_result = 0
for i in range(1, N + 1):
    for j in range(1, i):
        check = prefix_sum[i] - prefix_sum[j]
        if max_result < check:
            max_result = check


print(prefix_sum)

print(max_result)