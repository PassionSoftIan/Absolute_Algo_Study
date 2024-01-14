import sys

sys.stdin = open("15736_blue_flag_white_flag_input.txt")

print(int(int(input()) ** 0.5))

# N = int(input())
#
# count = 1
# check = 3
# i = 1
# while check + i <= N:
#     count += 1
#     i += check
#     check += 2
#
# print(count)