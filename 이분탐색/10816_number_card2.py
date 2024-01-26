import sys
sys.stdin = open("10816_number_card2_input.txt")

N = int(input())

nlist = sorted(list(map(int, input().split())))

M = int(input())

mlist = list(map(int, input().split()))

print(nlist)

for i in mlist:

    s = 0
    e = 0

    l = -1
    while s <= e:
        mid = (s + e) // 2
        if nlist[mid] < i:
            s = s + 1

        elif nlist[mid] > i:
            e = e - 1