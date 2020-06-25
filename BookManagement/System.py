import sys
import numpy as np
from Book_Management.db import database
import Book_Management.db


# 메뉴띄우기
class BookMgtSystem:
    def __init__(self, filepath):
        self.text = database(filepath)
        self.system_menu()

    def system_menu(self):
        while True:
            self.array = np.array(self.text.DB, str)
            print("""
                =======menu=======
                1.도서 추가
                2.도서 검색
                3.도서 정보 수정
                4.도서 삭제
                5.현재 총 도서 목록
                6.저장
                7.나가기
                ===================""")
            try:
                menu = int(input("메뉴를 선택하세요 : "))
            except:
                print("숫자를 입력하세요")
                self.system_menu()
            if menu == 1:  # 추가
                self.add()
            elif menu == 2:  # 검색
                self.search()
            elif menu == 3:  # 정보 수정
                self.modify()
            elif menu == 4:  # 삭제
                self.delete()
            elif menu == 5:  # 총 도서목록
                self.show_all()
            elif menu == 6:  # 저장
                self.save()
            elif menu == 7:  # 나가기
                self.finish()
                break
            else:
                print("1~7 중 하나를 입력하세요 !")
                self.system_menu()


    #menu에 따른 함수 설정


    #1번(도서추가 add)
    def add(self):
        self.add_input = input("추가할 도서의 정보를 입력하세요")
        self.bookname = input("도서명 : ")
        self.author = input("저자명 : ")
        self.published = input("출판연도 : ")
        self.publisher = input("출판사명 : ")
        self.genre = input("장르 : ")
        self.text.DB = np.append(self.text.DB,
                                 [[self.bookname, self.author, self.published, self.publisher, self.genre]], axis=0)
        print(self.text.DB)

    #2번(도서검색 search)
    def search(self):
        print("""
        ==================
        1.도서명으로 검색
        2.저자로 검색
        3.출판연도로 검색
        4.출판사명으로 검색
        5.장르로 검색
        ===================""")
        self.option = int(input("검색할 메뉴를 선택하세요 : "))

        if self.option == 1: #도서명으로 검색
            self.bookname = input("도서명 : ")
            # 이 밑은 다 비슷함
            self.array = np.array(self.text.DB, str)
            for i in range(len(self.text.title)):
                self.list1 = []
                self.list2 = []
                self.a = np.append(self.list2, [self.bookname], axis=0)
                self.b = np.append(self.list1, [self.array[i][0]], axis=0)
                # array[x][y] 에서 x가 커지는건 행을 키워 내려감
                # y가 커지는건 열을 키워 오른쪽으로감
                if self.b[0] == self.a[0]:
                    print(self.array[i])

        elif self.option == 2: #저자명으로 검색
            self.author = input("저자명 : ")
            self.array = np.array(self.text.DB, str)
            for i in range(len(self.text.title)):
                self.list1 = []
                self.list2 = []
                self.a = np.append(self.list2, [self.bookname], axis=0)
                self.b = np.append(self.list1, [self.array[i][1]], axis=0)
                if self.b[0] == self.a[0]:
                    print(self.array[i])

        elif self.option == 3: #출판연도로 검색
            self.published = input("출판연도를 입력하세요: ")
            self.array = np.array(self.text.DB,str)
            for i in range(len(self.text.published)):
                self.list1 = []
                self.list2 = []
                self.a = np.append(self.list2,[self.published],axis = 0)
                self.b = np.append(self.list1, [self.array[i][2]], axis=0)
                if self.b[0] == self.a[0]:
                    print(self.array[i])

        elif self.option == 4: #출판사명으로 검색
            self.publisher = input("출판사명을 입력하세요: ")
            self.array = np.array(self.text.DB,str)
            for i in range(len(self.text.publisher)):
                self.list1 = []
                self.list2 = []
                self.a = np.append(self.list2,[self.publisher],axis = 0)
                self.b = np.append(self.list1, [self.array[i][3]], axis=0)
                if self.b[0] == self.a[0]:
                    print(self.array[i])

        elif self.option == 5: #장르로 검색
            self.genre = input("장르를 입력하세요: ")
            self.array = np.array(self.text.DB,str)
            for i in range(len(self.text.genre)):
                self.list1 = []
                self.list2 = []
                self.a = np.append(self.list2,[self.genre],axis = 0)
                self.b = np.append(self.list1, [self.array[i][4]], axis=0)
                if self.b[0] == self.a[0]:
                    print(self.array[i])



    #3번(도서정보수정 modify)
    def modify(self):
        self.array = np.array(self.text.DB, str)
        print(self.array)
        self.change = int(input("수정할 내용을 선택하세요"
                                "\n0:도서명,1:저자,2:출판연도,3:출판사명,4:장르"
                                "\n입력 : "))

        if self.change == 0:#도서명 수정
            self.num = int(input("행을 선택하세요(0은 가장 위의 도서):"))
            self.name = input("수정할 내용을 입력하세요: ")
            for i in range(len(self.text.DB)):
                if i == self.num:
                    self.text.DB[i][0] = self.name
                    print(self.text.DB[i])
        elif self.change == 1:#저자 수정
            self.num = int(input("수정할 번째를 입력하세요(0은 제일 위 ):"))
            self.name = input("수정할 내용을입력하세요: ")
            for i in range(len(self.text.DB)):
                if i == self.num:
                    self.text.DB[i][1] = self.name
                    print(self.text.DB[i])
        elif self.change == 2:#출판연도 수정
            self.num = int(input("수정할 번째를 입력하세요(0은 제일 위 ):"))
            self.name = input("수정할 내용을입력하세요: ")
            for i in range(len(self.text.DB)):
                if i == self.num:
                    self.text.DB[i][2] = self.name
                    print(self.text.DB[i])
        elif self.change == 3:#출판사명 수정
            self.num = int(input("수정할 번째를 입력하세요(0은 제일 위 ):"))
            self.name = input("수정할 내용을입력하세요: ")
            for i in range(len(self.text.DB)):
                if i == self.num:
                    self.text.DB[i][3] = self.name
                    print(self.text.DB[i])
        elif self.change == 4:#장르 수정
            self.num = int(input("수정할 번째를 입력하세요(0은 제일 위 ):"))
            self.name = input("수정할 내용을입력하세요: ")
            for i in range(len(self.text.DB)):
                if i == self.num:
                    self.text.DB[i][4] = self.name
                    print(self.text.DB[i])



    #4번(도서삭제 delete)
    def delete(self):
        self.array = np.array(self.text.DB,str)
        print(self.text.DB)
        self.tt = int(input("삭제할 도서 번호(0은 가장 위의 도서): "))
        for i in range(len(self.text.DB)):
            if i == self.tt:
               self.text.DB = np.delete(self.text.DB,(i), axis = 0)
               print(self.text.DB)


    #5번(도서목록출력 show_all)
    def show_all(self):
        print(self.text.DB)


    #6번(저장 save)
    def save(self):
        save_confirm = int(input("저장하려면 1을 입력 : "))
        if save_confirm ==1:
            np.save("C:/Users/LGS1/Desktop/input1.txt", self.text.DB)
            self.saveload = np.load("C:/Users/LGS1/Desktop/output.txt.npy")
            print(self.saveload)


    #7번(종료 finish)
    def finish(self):
        np.save("C:/Users/LGS1/Desktop/input1.txt", self.text.DB)
        self.saveload = np.load("C:/Users/LGS1/Desktop/output.txt.npy")
        print(self.saveload)
        sys.exit()



if __name__ == "__main__":
    app = BookMgtSystem("input.txt")