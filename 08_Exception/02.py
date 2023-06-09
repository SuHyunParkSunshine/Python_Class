#ValueError 처리 예시
try:
    user_input = input("Enter a number: ")
    number = int(user_input)
except ValueError:
    print("Invalid input. Please enter a valid number.")
print("-" * 50)

#연습문제: data = {"Sun": 0, "Mon": 1, "Tue": 2, "Wed": 3, "Thu": 4, "Fri": 5, "Sat": 6} 이 주어질 때 try-except문을 이용하여 다음과 같이 동작하는 프로그램을 작성하라.
data = {"Sun": 0, "Mon": 1, "Tue": 2, "Wed": 3, "Thu": 4, "Fri": 5, "Sat": 6}

#try-except문 사용
while True:
    try:   
        user_input = input("요일을 입력하세요: ")
        value = data[user_input]
        print(value)
    except KeyError:
        print("항목이 없습니다")
        break
#try-except문 미사용
while True:
    user_input = input("요일을 입력하세요: ")
    value = data.get(user_input)

    #python 에서는 0, null, None 은 false 양수, 음수는 모두 True!!
    if value is not None:
        print(value)
    else:
        print("항목이 없습니다")
        break