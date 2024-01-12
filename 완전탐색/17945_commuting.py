import sys, math

sys.stdin = open("17945_input.txt")

a, b = map(int, input().split())

if -a+int(math.sqrt(a**2-b)) == -a-int(math.sqrt(a**2-b)):
    print(-a+int(math.sqrt(a**2-b)))
else: print(-a-int(math.sqrt(a**2-b)), -a+int(math.sqrt(a**2-b)))