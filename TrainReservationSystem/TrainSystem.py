import sys,copy

f = open("C:/Users/LGS1/Desktop/EoN16기활동/TrainList.txt", 'r')
List = []
indlist = []
while True:
    line = f.readline().split()
    List.append(line)
    if not line:
        break
f.close()
del List[0] #앞에 0을 안지우면 오류
del List[len(List) - 1]

modyList = copy.deepcopy(List)
reservation_list = []
ind = None


for i in range(20): #열차가 총 20종류임
    del modyList[i][2]
    modyList[i][0] = modyList[i][0].replace(":", "")
    modyList[i][0] = int(modyList[i][0])


class TrainSystem:
#메뉴 띄우기
    def train_menu(self):
        while True:
            print("1. 빠른 시간 기차 검색 및 예매")
            print("2. 전체 기차 시간대 보기 ")
            print("3. 나의 예매 현황 및 예약 취소")
            print("4. 프로그램 종료 ")
            try:
                menu = int(input("메뉴를 입력하세요 : "))
            except:
                print("숫자를 입력하세요") #어떤 오류든지
                self.train_menu()

            if menu == 1:
                self.search_train()
            elif menu == 2:
                self.show_all()
            elif menu == 3:
                self.my_reserved_train()
            elif menu == 4:
                self.program_off()
                break
            else:
                print("1,2,3,4 중 하나를 입력하세요 !") #이상한 숫자 입력 시
                self.train_menu()


#1번
    def search_train(self):
        print("☆ 가장 가까운 시간대의 기차를 조회하려면 1을 입력하세요.")
        print("☆ 뒤로가기")
        search_train_menu = input("입력 : ")
        if search_train_menu == "1":
            des_train = list(input(
                "☆ 조회할 시간(hh:mm), 출발역, 도착역, 열차종류 입력"
                "\n☆ 뒤로가기"
                "\n입력 : ").split())
            tmp_TL = copy.deepcopy(modyList)

            for i in range(20):
                tmp_TL[i].pop()

            time_list = [365, 395, 435, 522]
            # 열차 시간이 총 4가지며
            # mytime을 계산했을 때 나올 수 있는 결과들
            tmp_mytime = int(des_train[0].replace(":", ""))
            a, b = divmod(tmp_mytime, 100)
            mytime = a * 60 + b
            des_train[0] = close_time(mytime, time_list)
            closed_T = []

            for i in range(20):
                if tmp_TL[i] == des_train:
                    closed_T = tmp_TL[i].copy()
                    closed_T.append(List[i][5])
                    ind = i
                    print("\n===== 가장 가까운 시간의 기차 정보 =====\n")
            a, b = divmod(closed_T[0], 100)
            a = str(a)
            b = str(b)
            if int(b) // 10 == 0:  #b가 10분, 20분, 30분...이면
                closed_T[0] = ''.join(['0', a, ':', '0', b])
            else:
                closed_T[0] = ''.join(['0', a, ':', b])
            print('|', end=' ')
            for a in closed_T:
                print(a, end=' | ')
            while True:
                reservation = input("\n해당 기차표를 예매하시겠습니까? [Y/N]"
                                    "\n입력 : ")
                if reservation == 'Y':
                    if List[ind][5] != "매진":
                        reservation_list.append(List[ind])
                        List[ind][5] = int(List[ind][5]) - 1  # 잔여좌석 -1
                        print("\n예매가 완료되었습니다.")
                        indlist.append(ind)
                        if List[ind][5] == 0:
                            List[ind][5] = "매진"
                        break
                    else:
                        print("\n매진됐지롱")
                        break
                elif reservation == "N":
                    break
                else:
                    print("Y 또는 N을 입력하세요 !")
            return ind
        else:
            self.train_menu()

# 2번
    def show_all(self):
        print("☆ 모든 기차의 시간대를 확인하려면 1을 입력하세요.")
        print("☆ 뒤로가기")
        show_all_menu = input("입력 : ")
        if show_all_menu == "1":
            print("====== 전체 기차 시간표 ======")
            i = 0
            while i < len(List):
                a, b, c, d, e, f = List[i]
                print(a, b, c, d, e, f)
                i += 1
        else:
            self.train_menu()


# 3번
    def my_reserved_train(self):
        print("☆ 나의 예매현황을 확인하려면 1을 입력하세요.")
        print("☆ 뒤로가기")
        my_reserved_train_menu = input("입력 : ")
        if my_reserved_train_menu == "1":
            if ind == None:
                print("\n예매된 기차가 없습니다.")
            elif reservation_list == []:
                print("\n예매된 기차가 없습니다.")
            else:
                print("\n==== 예매 내역 ====\n")
                i = 0
                while i < len(reservation_list):
                    a, b, c, d, e, f = reservation_list[i]
                    print(a, b, c, d, e, f)
                    i += 1
                    print(reservation_list)

                cancel = input("\n예매를 취소하시겠습니까? [Y/N]"
                               "\n☆ 뒤로가기"
                               "\n입력 : ")

                if cancel == 'Y':  # 잔여좌석 +1
                    if List[indlist[len(indlist) - 1]][5] == '매진':
                        List[indlist[len(indlist) - 1]][5] = 1
                        reservation_list.pop()
                    else:
                        List[indlist[len(indlist) - 1]][5] = List[indlist[len(indlist) - 1]][5] + 1
                        reservation_list.pop()
                    indlist.pop()
                    print('\n취소가 완료되었습니다.')
        else:
            self.train_menu()


# 4번
    def program_off(self):
        print("☆ 프로그램을 종료하려면 1을 입력하세요.")
        print("☆ 뒤로가기")
        program_off_menu = input("입력 : ")
        if program_off_menu == "1":
            print("Good Bye-!")
            sys.exit()
        else:
            self.train_menu()


# 가까운 시간의 열차를 찾는 함수
def close_time(mytime, time_list):  # 근접한 값 찾는 함수
    a = mytime
    b = time_list.copy() # [365, 395, 435, 522]
    real_time_list = [605, 635, 715, 842]
    abs_list = []
    for i in range(len(b)):
        abs_list.append(abs(a - b[i]))
    ind = abs_list.index(min(abs_list))
    return real_time_list[ind]


if __name__ == "__main__":
    myStart = TrainSystem()
    print(myStart.train_menu())
