number = int(input("주민등록번호를 입력하세요:"))
if number//1000000 in (1,3):
    print('남')
elif number//1000000 in (2,4):
    print('여')
