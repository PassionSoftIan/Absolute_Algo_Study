import sys
sys.stdin = open("2309_seven_dwarfs_input.txt")


dwarfs = [int(input()) for _ in range(9)]

dwarfs.sort()

check = sum(dwarfs) - 100

l = 0
r = 1

while l < r < 9:
    if dwarfs[l] + dwarfs[8] < check:
        l += 1
        r += 1
        continue

    if dwarfs[l] + dwarfs[r] == check:
        dwarfs.pop(l)
        dwarfs.pop(r-1)
        for go in dwarfs:
            print(go)
        exit()

    elif dwarfs[l] + dwarfs[r] < check:
        r += 1
    else:
        l += 1
        r = l + 1