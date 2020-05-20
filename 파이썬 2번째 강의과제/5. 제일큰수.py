import sys
mxNumber = 0
numbers = list(map(int,sys.stdin.readline().split()))
for i in numbers:
    if mxNumber < (i):
        mxNumber = (i)
print(mxNumber)