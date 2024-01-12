import sys

sys.stdin = open("15996_factorial_devide_input.txt")

N, A = map(int, input().split())

Temp_N = N
while N != 1:
    N -= 1
    Temp_N *= N

while Temp_N 
print(Temp_N)