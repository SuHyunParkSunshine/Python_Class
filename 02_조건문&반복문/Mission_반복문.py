#Mission
#No.1
'''num = int(input("숫자를 입력하시오: "))

print(num, "의 약수는 [", end="")
for i in range(1, num + 1):
    if(num % i == 0):
        print(i, " ", end="")
        break
print("] 입니다")'''

#No.2
'''while(True):
    num = int(input("숫자를 입력하시오: "))
    if(num < 0):
        print("프로그램을 종료합니다")
        break
    elif (num >= 90):
        grade = 'A'        
    elif (num >= 80):
        grade = 'B'
    elif (num >= 60):
        grade = 'C'
    elif (num >= 40):
        grade = 'D'
    else:
        grade = 'F'
    print(grade)'''

#No.3
num = int(input("숫자를 입력하시요: "))
cnt = 0

print("1부터 ", num, "까지의 소수- ", end="")
for i in range(2, num + 1):
    boolean = True
    for k in range(2, i):
        if i % k == 0:
            boolean = False
            break
    if boolean is True:
        print(i, ' ', end='')
        cnt += 1
print("\n1부터 ", num, "까지의 소수의 개수는 : ", cnt, "이다")