x =  list(map(int,input("두 수를 입력하세요:").split()))
a = max(x)
b = min(x)
while True:
    c = 0
    c = a % b
    a = b
    b = c
    if b == 0:
        print(a)
        break

