test_cases = int(input("test할 케이스의 수 : "))

for _ in range(test_cases):
    n, m = list(map(int, input("작업 수 / 작업 번호 : ").split()))
    input_list = list(map(int, input("작업 우선순위 : ").split()))
    index = list(range(len(input_list)))
    index[m] = 'target'

    # 순서
    order = 0

    while True:
        # 첫번째 if: input_list의 첫번째 값 = 최댓값?
        if input_list[0] == max(input_list):
            order += 1

            # 두번째 if: index의 첫 번째 값 = "target"?
            if index[0] == 'target':
                print(order,"분")
                break
            else:
                input_list.pop(0)
                index.pop(0)

        else:
            input_list.append(input_list.pop(0))
            index.append(index.pop(0))