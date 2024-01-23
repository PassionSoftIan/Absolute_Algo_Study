import sys

sys.stdin = open("2003_sum_of_nums2_input.txt")

N, M = map(int, input().split())

nums = list(map(int, input().split()))

i = 0
j = 1

result = 0

total = nums[0] + nums[1]
while i <= j < N:
    if total == M:
        result += 1
        j += 1
        if j == N:
            break
        total += nums[j]
    elif total < M:
        j += 1
        if j == N:
            break
        total += nums[j]
    else:
        total -= nums[i]
        i += 1
        if j < i:
            j += 1

print(result)