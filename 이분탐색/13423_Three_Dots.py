import sys
sys.stdin = open("13423_Three_Dots_input.txt")

Test_Case = int(input())

for tc in range(Test_Case):
    N = int(input())
    arr = sorted(list(map(int, input().split())))
    count = 0
    for i in range(N - 2):
        l = i
        r = N - 1
        while l < r - 1:
            check = (arr[l] + arr[r])/2
            if check in arr:
                count += 1
                print(arr[l], int(check), arr[r])
                r -= 1

            else:
                mid = (l + r) // 2
                if check < arr[mid]:
                    break
                else:
                    r -= 1
    print(count)