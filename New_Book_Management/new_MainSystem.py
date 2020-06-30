import os
import sys
from New_Book_Management import new_search

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'input.txt')
textfile_data = open(my_file,'r')
#textfile_data = textfile_data.readlines()
textfile_data = textfile_data.read().splitlines()
#textfile_data = [line.rstrip('\n') for line in open(my_file, 'r')]


# 메뉴띄우기
class BookMgtSystem:


    def system_menu(self, textfile_data):
        self.textfile_data = textfile_data
        while True:
            print("\n==== menu ====")
            print("1.도서 추가")
            print("2.도서 검색")
            print("3.도서 정보 수정")
            print("4.도서 삭제")
            print("5.현재 도서 목록")
            print("6.저장")
            print("7.종료")
            print("==============")

            try:
                menu = int(input("메뉴를 선택하세요 : "))
            except:
                print("숫자를 입력하세요")
                self.system_menu(self, textfile_data)

            if menu == 1:  # 추가
                self.add(textfile_data)
            elif menu == 2:  # 검색
                self.search(textfile_data)
            elif menu == 3:  # 정보 수정
                self.modify(textfile_data)
            elif menu == 4:  # 삭제
                self.delete(textfile_data)
            elif menu == 5:  # 총 도서목록
                self.show_all()
            elif menu == 6:  # 저장
                self.save(textfile_data)
            elif menu == 7:  # 나가기
                self.finish(textfile_data)
                break
            else:
                print("1~7 중 하나를 입력하세요 !")
                self.system_menu()


# menu에 따른 함수 설정

    # 1번(도서추가 add)
    def add(self, textfile_data):
        add1 = str(input("도서명, 저자명, 출판연도, 출판사명, 장르를 입력하세요"
              "\n공백으로 구분합니다\n")).splitlines()
        print(add1)
        textfile_data.extend(add1)
        print("추가되었습니다.")
        return self.system_menu(textfile_data)


    # 2번(도서검색 search)
    def search(self, textfile_data):
        self.user_option = int(input("★ 검색하려면 1을 입력 : "))

        if self.user_option == 1:
            new_search.search_book(1,textfile_data)


    # 3번(도서정보수정 modify)
    def modify(self, textfile_data):
        for i in range(len(textfile_data)):
            print(i)
            print(textfile_data[i])
        num = int(input("수정할 도서의 번호를 입력하세요 (0은 최상위 도서) : "))
        print(textfile_data[num])
        textfile_data[num] = str(input("도서명, 저자명, 출판연도, 출판사명, 장르를 입력하세요\n:"))
        print("수정되었습니다.")
        return textfile_data, self.system_menu(textfile_data)


    # 4번(도서삭제 delete)
    def delete(self, textfile_data):
        my_delete = int(input("몇번째 파일을 삭제할까요? (0은 최상위 도서) : "))
        textfile_data.pop(my_delete)
        print(my_delete)
        print("번째의 도서를 삭제했습니다.")
        return textfile_data, self.system_menu(textfile_data)

    # 5번(도서목록출력 show_all)
    def show_all(self):
        print("   ====== 도서 목록 ======\n")
        for i in range(len(textfile_data)):
            print(textfile_data[i])
        return self.system_menu(textfile_data)


    # 6번(저장 save)
    def save(self, textfile_data):
        save_confirm = int(input("저장하려면 1을 입력 : "))
        if save_confirm == 1:
            with open('input.txt', 'w') as file:
                textfile_data = self.addEnter(textfile_data)
                file.writelines(textfile_data)



    def addEnter(self, textData):
        for i in range(len(textData)):
            textData[i] = textData[i] + "\n"
        return textData


    # 7번(종료 finish)
    def finish(self, textfile_data):
        with open('input.txt', 'w') as file:
            textfile_data = self.addEnter(textfile_data)
            file.writelines(textfile_data)
        print("시스템을 종료합니다.")
        sys.exit()


b=BookMgtSystem()
b.system_menu(textfile_data)