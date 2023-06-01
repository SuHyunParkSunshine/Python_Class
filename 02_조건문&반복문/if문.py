#if-elif-else문
"""score = int(input("성적을 입력하시오: "))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"당신의 학점은 {grade}입니다.")"""

#한 문장의 if-else문
#사용자로부터 입력받은 수가 양수인 경우에만 제곱근을 구하고, 그 외에는 "잘못된 입력입니다."라는 메세지를 출력하는 프로그램

'''import math
num = float(input("양수를 입력하세요: "))
result = math.sqrt(num) if num > 0 else "잘못된 입력입니다."
print("결과: ", result)'''

#Mission "성적계산기를 작성하세요"
lang = int(input("국어점수 커몬: "))
eng = int(input("영어점수 커몬: "))
math = int(input("수학점수 커몬: "))

total = ((lang * 0.4) + (eng * 0.4) + (math * 0.2))

if total >= 90:
    grade = "A"
elif total >= 80:
    grade = "B"
elif total >= 70:
    grade = "C"
elif total >= 80:
    grade = "D"
else:
    grade = "F"

print(f"국어: {lang}, 영어: {eng}, 수학: {math}\n총 평균 점수: {total:.2f}\n학점: {grade}")
# print(f"총 평균 점수: {total:.2f}")
# print(f"학점: {grade}")