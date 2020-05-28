import sys
a = list(map(int,sys.stdin.readline().split()))
b = list(map(int,sys.stdin.readline().split()))
count = 0
while True:
    b = sorted(b)
    print("b의 값",b)
    value = b[0] + (b[1] * 2)
    print("value의 값:",value)
    count += 1
    b.append(value)
    b = sorted(b)
    del b[0:2]
    if value >= a[1] :
        print("count값:",count)
        break