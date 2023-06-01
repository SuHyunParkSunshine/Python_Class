# 연습문제 1
'''cm = int(input("cm길이를 입력하시오"))
if(cm >= 0):
    inch = cm / 2.54
    print(f"{cm}cm는 {inch:.2f}inch 입니다")
else:
    print("잘못 입력하였습니다.")'''

# 연습문제 2
'''score = int(input("학점을 입력하시오: "))

if score >= 80:
    print("졸업반입니다.")
elif score >= 40:
    print("2학년입니다.")
else:
    print("1학년입니다.")'''


# 연습문제 3
'''currentT = int(input("시간을 입력하시오: "))
choose = int(input("(1)am (2)pm: "))
aheadT = int(input("경과시간을 입력하시오: "))

if choose == 1:
    if currentT + aheadT > 12:
        result = (currentT + aheadT) - 12
        print(f"New hour: {result} pm")
    else:
        result = (currentT + aheadT)
        print(f"New hour: {result} am")
else:
    if currentT + aheadT > 12:
        result = (currentT + aheadT) - 12
        print(f"New hour: {result} am")
    else:
        result = (currentT + aheadT)
        print(f"New hour: {result} pm")'''

# 연습문제_교수님코드
time = int(input("현재시간: "))
apm = input("am or pm: ")
over_time = int(input("추가시간: "))

new_time = (time + over_time) % 12

if new_time == 0:
    new_time = 12
if (time + over_time) // 12 % 2 == 1:
    if apm == "am":
        apm = "pm"
    else:
        apm = "am"

print(f"최종 시간: {new_time} {apm}")
