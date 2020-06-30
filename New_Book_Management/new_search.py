def search_book(self,textfile_data):
    textfile_length = len(textfile_data)

    if self == 1:
        user_input1 = str(input("검색할 내용 입력 : "))
        for i in range(textfile_length):
            if user_input1 in textfile_data[i]:
                print(textfile_data[i])
        print("검색종료")

    else:
        print("메뉴로 돌아갑니다.")