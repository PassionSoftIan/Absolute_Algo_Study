import sys
sys.stdin = open("2467_solution_input.txt")

N = int(input())

solution = list(map(int, input().split()))

solution_a = 0
solution_b = 0

l = 0
r = N - 1

dist = int(1e9) * 2

while l < r:
    check = abs(solution[l] + solution[r])

    if check == 0:
        print(solution[l], solution[r])
        exit()

    if check < dist:
        dist = check
        solution_a = solution[l]
        solution_b = solution[r]
        if abs(solution_a) < abs(solution_b):
            r -= 1
        else:
            l += 1
    else:
        if abs(solution[l]) < abs(solution[r]):
            r -= 1
        else:
            l += 1

print(solution_a, solution_b)