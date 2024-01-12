import sys

sys.stdin = open("11659_prefix_sum4_input.txt")

N, M = map(int, input().split())

arr = list(map(int, input().split()))

# prefix_sum = [0] * (N + 1)
#
# for go in range(N):
#     prefix_sum[go + 1] = prefix_sum[go] + arr[go]

prefix_sum = [0]

temp = 0
for go in range(N):
    temp += arr[go]
    prefix_sum.append(temp)

for mc in range(M):
    i, j = map(int, input().split())
    print(prefix_sum[j] - prefix_sum[i - 1])