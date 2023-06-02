#while문
'''num = int(input("10진수를 입력하세요: "))
binary = ""

while num > 0:
    remainder = num % 2
    binary = str(remainder) + binary
    num = num // 2

print("입력한 수의 2진수 표현: ", binary)'''

#for문
#문자열의 각 문자를 순차적으로 출력하는 예제
'''text = "Python"
for char in text:
    print(char)'''

#range()함수
'''type(range(1,10))'''

#Mission
#3의 배수와 5의 배수의 합 구하기
'''n = int(input("양의 정수 n을 입력하세요: "))
sum = 0
for i in range(1, n+1):
    if(i % 3 == 0 or i % 5 == 0):
        sum += i
result = f"1부터 {n}까지의 자연수 중에서 3과 5의 배수의 합: {sum}"
print(result)'''

#최댓값과 최솟값 찾기
'''max_num = 0
min_num = 100

for i in range(5):
    num = int(input(f"{i + 1}번째 숫자를 입력하세요: "))
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num

result = f"최댓값: {max_num} & 최솟값: {min_num}"
print(result)'''

#숫자의 합이 100보다 작을 때까지 입력 받기
'''sum = 0
while sum < 100:
    num = int(input("숫자를 입력하세요: "))
    sum += num
result = f"입력받은 숫자들의 합: {sum}"
print(result)'''

#피보나치 수열의 n번째 항을 출력
'''n = int(input("몇 번째 항을 출력할까요? "))

if n == 1 or n == 2:
    result = 1
else:
    a, b = 1, 1
    i = 3
    while (i <= n):
        result = a + b
        b = result
        i += 1
output = f"피보나치 수열의 {n}번째 항은 {result}입니다."
print(output)'''

#주사위 게임
import random
'''dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)

sum = dice1 + dice2
print(f"dice1 : {dice1}, dice2 : {dice2}")
if (sum == 7):
    print("You Win")
else:
    print("You Lose")'''

#계산기 프로그램
'''while(True):
    num1 = input("첫 번째 수를 입력하세요('exit'입력 시 종료): ")

    if num1 == 'exit':
        print("프로그램을 종료합니다")
        break
    
    num2 = input("두 번째 수를 입력하세요: ")
    op = input("연산자를 입력하세요(+, -, *, /): ")
    result = 0

    num1 = int(num1)
    num2 = int(num2)

    if(op == "+"):
        result = num1 + num2           
    elif(op == "-"):
        result = num1 - num2        
    elif(op == "*"):
        result = num1 * num2        
    elif(op == "/"):
        result = num1 / num2       
    print("결과 값은", result," 입니다")'''

#숫자 맞추기 게임 프로그램
'''import random
ran = random.randint(1, 100)
print("random: ", ran)
i = 0
while (i < 5):
    num = int(input("숫자를 입력하시요"))
    if(num == ran):
        print("random figure: ", ran)
        print("num you selected: ", num)
        print("You got it!!")
        break
    else:
        i += 1
        if(i == 5):
            print("You Loseeee")
            break'''
#야바위 게임
'''from random import randint
stake = 50

while(True):
    coin = randint(1,2)
    print("코인은: ", coin)
    sel = int(input("1, 2중에서 선택하시오: "))
    if(sel == coin):
        stake = stake + 9
        if(stake >= 100):
            print("현재 ", {stake}, "$를 획득하여 프로그램을 종료합니다")
            break
    else:
        stake = stake - 10
        if (stake <= 0):
            print("판돈을 모두 잃어 프로그램을 종료합니다", {stake}, "$ 마이너스입니다")
            break'''
#최대공약수
'''num1 = int(input("첫번째 수를 입력하시옹: "))
num2 = int(input("두번째 수를 입력하시옹: "))

if(num1 > num2):
    while(num2 > 0):
        res = num1 % num2        
        num1 = num2
        num2 = res
    print("최대공약수는: ", num1, " 입니다")
else:
     while(num1 > 0):
        res = num2 % num1
        num2 = num1
        num1 = res
print("최대공약수는: ", num2, " 입니다")'''
