'''
임의의 개수를 가진 양수 수열을 Bubble sort 알고리즘을 활용해
오름차순으로 정렬하는 코드를 작성하라.
▶중복되는 숫자는 없다고 가정한다.
▶수열은 사용자가 입력한다.
▶sort() 함수는 사용하지 말 것
'''

def bubbleSort(arr): #함수선언
    n = len(arr) #문자열의 개수 안내

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]: #바로 앞의 숫자가 뒤의 숫자보다 크다면
                arr[j], arr[j + 1] = arr[j + 1], arr[j] #위치 변경
    return (arr)


a = input("input : ").split() #공백을 기준으로 숫자를 구분함
a = list(map(int, a)) #문자를 숫자로 변환

print("output : ", bubbleSort(a))


