#연습문제 1: 1~n까지의 합을 계산하는 함수
def sum_(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total
print(sum_(50))
print("-" * 50)

#연습문제 1: 두 개의 매개변수 n, m을 전달받아 m x n개의 * 상자를 출력하는 프로그램을 함수로 작성
def multi(m, n):
    for i in range(m):
        for j in range(n):
            print("*", end="")
        print()
print(multi(2, 4))
print("-" * 50)

#연습문제 2: 하나의 숫자를 전달받아 숫자의 자리 합을 구하는 함수를 작성
def strCal(int):
    strInt = str(int)
    sum = 0
    for i in range(len(strInt)):
        sum += int(strInt[i])
print(strCal(123))
print("-" * 50)

#연습문제 3: 두 개의 문자열이 서로 다른 처음 위치를 반환하는 함수를 작성. 두 개의 문자열이 같으면 -1을 반환
import math

def str_comp(str1, str2):
    flag = 0
    length = min(len(str1), len(str2))
    for i in range(length):
        if str1[i] != str2[i]:
            if i != 0:
                return i
    return -1
str_comp('abcf', 'abbd')

#연습문제 4: 문자열과 하나의 문자를 전달받아 문자열에서 문자의 위치를 모두 찾아 리스트로 반환하는 함수를 작성

#연습문제 5: 재귀 함수를 이용하여 1부터 100까지의 합을 계산하는 프로그램

#연습문제 1: enumerate() 내장 함수를 이용하여 사용자가 입력한 문자열에서 'a' 문자의 위치를 모두 찾아 출력하는 프로그램을 작성하라. 'a'가 없으면 "a가 없습니다'라는 메시지를 출력하라.
str = input("문자열을 입력하시요: ")

flag = 0

for index, a in enumerate(str):
    if a == "a":
        print(index, a)
        flag = 1

    if flag == 0:
        print("a가 없습니다")

#연습문제 2: 두 수의 합(sum), 차(sub), 곱(mul), 나누기(div)를 수행하는 함수를 각각 정의하라. 딕셔너리를 이용하여 사용자가 '1'을 입력하면 sum()을 호출하고, '2'를 입력하면 sub(), '3'을 입력하면 mul(), '4'를 입력하면 div() 함수를 호출하여 두 수의 연산을 수행하는 프로그램을 작성하라
def sum (a, b):
    return a + b

def sub (a, b):
    return a - b

def mul (a, b):
    return a * b

def div (a, b):
    return a / b

table = {'1' : sum, '2' : sub, '3' : mul, '4' : div}
op = input('하고 싶은 연산을 입력하시요(1, 2, 3, 4): ')
func = table[op]
print(func(2, 3))

#연습문제 3: 다음과 같이 구성되는 문자열을 구분 문자(&, =)로 분리하여 딕셔너리로 반환하는 함수 작성 
#예: 문자열 'led=on&motor=off&switch=off'이고 구분 문자가 '&', '='일 때 {'led':'on', 'motor':'off', 'switch':off'} 반환. 
#Hint: dict([['a','b'], ['c', 'd']]) ->{'a': 'b', 'c': 'd'}
str = 'led=on&motor=off&switch=off'

def query_parse(str):
    items = str.split('&')
    temp = []
    for item in items:
        temp.append(item.split("="))    
    return dict(temp) #dictionary로 변환

print(query_parse(str))