psNumber = list(input("학번을 입력하세요:"))
psNumber = list(map(int, psNumber))
print(sorted(psNumber, reverse=True))