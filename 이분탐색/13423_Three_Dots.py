import sys
sys.stdin = open("13423_Three_Dots_input.txt")

Test_Case = int(input())

for tc in range(Test_Case):
    N = int(input())
    arr = sorted(list(map(int, input().split())))
    count = 0
    for i in range(N - 2):
        for j in range(N-1, i+1, -1):
            s = i
            e = j
            check = (arr[s] + arr[e]) / 2
            if check - int(check) == 0:
                while s < (e - 1):
                    mid = (s + e) // 2
                    if arr[mid] < check:
                        s = mid
                    elif arr[mid] > check:
                        e = mid
                    else:
                        count += 1
                        break
            else:
                continue

    print(count)