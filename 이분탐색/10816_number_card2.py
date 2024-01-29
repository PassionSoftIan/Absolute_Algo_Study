import sys
sys.stdin = open("10816_number_card2_input.txt")

N = int(input())

nlist = sorted(list(map(int, input().split())))

M = int(input())

mlist = list(map(int, input().split()))

print(nlist)

for i in mlist:

    s = 0
    e = N - 1

    l = 0
    while s <= e:
        mid = (s + e) // 2
        if nlist[mid] < i:
            s = mid + 1

        elif nlist[mid] > i:
            e = mid - 1

        elif nlist[mid] == i:
            if mid > 0 and nlist[mid - 1] == i:
                e = mid - 1
            else:
                l = mid
                break

    s = 0
    e = N - 1

    r = 0
    while s <= e:
        mid = (s + e) // 2
        if nlist[mid] < i:
            s = mid + 1

        elif nlist[mid] > i:
            e = mid - 1

        elif nlist[mid] == i:
            if mid < N-1 and nlist[mid + 1] == i:
                s = mid + 1
            else:
                r = mid + 1
                break
    print(r - l, end=' ')
