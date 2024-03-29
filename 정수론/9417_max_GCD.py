import sys

sys.stdin = open("9417_max_GCD_input.txt")

N = int(input())

result = []
for tc in range(N):
    arr = sorted(list(map(int, input().split())))
    M = len(arr)
    max_result = 0
    for i in range(M - 1):
        for j in range(i + 1, M):
            a = arr[j]
            b = arr[i]
            while b != 0:
                temp_a = a
                a = b
                b = temp_a % b
            if max_result < a:
                max_result = a
    result.append(max_result)

for check in result:
    print(check)

# N = int(input())
#
# result = []
# for tc in range(N):
#     arr = sorted(list(map(int, input().split())))
#     M = len(arr)
#     max_result = 0
#     for i in range(M - 1):
#         for j in range(i + 1, M):
#             for p in range(1, arr[i] + 1):
#                 if arr[i] % p == 0 and arr[j] % p == 0:
#                     if max_result < p:
#                         max_result = p
#     result.append(max_result)
#
# for check in result:
#     print(check)