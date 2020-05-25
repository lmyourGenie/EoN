'''
후입 선출(LIFO : Last In First Out)
'''


print("==== 메뉴 ====")
print("PUSH : 1\nPOP : 2\nSHOW : 3\n")
print("(종료하려면 1,2,3 이외의 수 입력)\n")
list = []

while True:
    menu = input("메뉴를 입력하세요 : ")
    try:
        number = int(menu)
        if number == 1:
            Userinput = int(input("수 입력 : "))
            list.append(Userinput) #리스트에 입력한 숫자를 덧붙인다
            continue #아래의 코드는 실행하지 않고 건너뛴 뒤 다음 반복을 시작한다
        elif number == 2:
            if len(list): #리스트에 요소가 있으면 True
                list.pop()
            else:
                print("더이상 삭제할 수 없습니다")
            continue
        elif number == 3:
            print(list)
            continue
        else:
            print("==== 스택 프로그램을 종료합니다 ====")
            break
    except:  #문자,기호 입력 등으로 오류 발생 시
        print("숫자를 입력하세요")
        continue