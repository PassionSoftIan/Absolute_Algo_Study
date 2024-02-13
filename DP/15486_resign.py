import sys
sys.stdin = open("15486_resign_input.txt")

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dp = [0] * (N + 1)  # Bottom-Up을 위한 DP 테이블 생성

# Bottom-Up 방식으로 DP 테이블 채우기
for i in range(N - 1, -1, -1):  # 큰 문제에서부터 작은 문제로
    if i + arr[i][0] <= N:  # 해당 일자에 상담이 끝나는 날이 퇴사 전인 경우
        dp[i] = max(arr[i][1] + dp[i + arr[i][0]], dp[i + 1])  # 현재 일자를 선택하는 경우와 선택하지 않는 경우 중 큰 값 선택
    else:  # 퇴사 전에 일을 끝낼 수 없는 경우
        dp[i] = dp[i + 1]  # 현재 일자 선택하지 않음

print(dp[0])  # 결과 출력

#
#
# def backtracking(depth):
#     # global ans
#     if depth > N:
#         return -10000000
#     # ans = max(ans, total)
#     if depth == N:
#         return 0
#     if dp[depth] != -1:
#         return dp[depth]
#     # backtracking(depth + arr[depth][0], total + arr[depth][1])
#     # backtracking(depth + 1)
#     dp[depth] = max(backtracking(depth + arr[depth][0]) + arr[depth][1], backtracking(depth + 1))
#     return dp[depth]
#     # backtracking(depth + 1, total)
#
#
# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
# # ans = -1000000000
#
# dp = [-1] * N
#
# print(backtracking(0))
#
# print(dp)
# print(arr)
#
# # print(ans)