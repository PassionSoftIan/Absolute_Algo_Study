import sys

sys.stdin = open("10815_number_card_input.txt")

N = int(input())

nlist = sorted(list(map(int, input().split())))

M = int(input())

mlist = list(map(int, input().split()))

for i in range(M):
    s = 0
    e = N - 1
    result = 0
    while s <= e:
        mid = (s + e) // 2
        if mlist[i] < nlist[mid]:
            e = mid - 1

        elif mlist[i] > nlist[mid]:
            s = mid + 1

        else:
            result = 1
            break
    print(result, end=' ')