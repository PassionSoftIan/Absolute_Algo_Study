import sys
sys.stdin = open("3273_sum_of_two_nums_input.txt")

N = int(input())

arr = sorted(list(map(int, input().split())))

X = int(input())

i = 0
j = N - 1

result = 0
while i < j:
    if arr[i] + arr[j] > X:
        j -= 1
    elif arr[i] + arr[j] < X:
        i += 1
    else:
        result += 1
        i += 1

print(result)