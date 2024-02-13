import sys
sys.stdin = open("1182_sum_of_partial_sequence_input.txt")


def backtracking(depth, start):
    global answer

    if depth <= N:
        if sum(result) == S and result:
            answer += 1
            print(*result)
    else:
        return

    for i in range(start, N):
        result.append(arr[i])
        backtracking(depth + 1, i+1)
        result.pop()


N, S = map(int, input().split())

arr = list(map(int, input().split()))

answer = 0

result = []

check = []

backtracking(0, 0)

print(answer)