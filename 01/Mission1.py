# price = int(input("가격을 입력하시오: "))
# count = int(input("개수을 입력하시오: "))

# totalAmt = price * count * 1.1
# print(f"납부하실 금액은 {totalAmt}입니다")

#1
# sec = int(input("초를 입력하시오: "))
# fsec = sec % 60
# fmin = sec / 60
# print(f"해당 초는 {fmin:.0f200}분 {fsec}입니다")

#2
# x = int(input("몇 분을 계산해주깝쇼: "))
# # // -> 몫 구하는 연산자
# date = x // 1440
# hour = (x - (1440 * date)) // 60
# min = (x - (1440 * date)) % 60

# print(f"해당 x는 {date}일 {hour}시간 {min}분입니다")

#3
# amount = int(input("원금을 입력하시오: "))
# interest = int(input("연이율을 입력하시오: "))
# duration = int(input("운용기간을 입력하시오: "))

# result = amount * (1 + (interest * 1/100))**duration
# print(f"원리금은 {result:.0f}입니다")

#4
# n = int(input("몇까지 더해줄까욤?"))
# result = n * (n + 1) / 2
# print(f"{n}까지의 합은 {result:.0f}입니다")

#5
grape = int(input("포도의 개수를 입력하시오: "))
strawberry = int(input("딸기의 개수를 입력하시오: "))

result = (75 * grape) + (113.5 * strawberry)
print(f"포도와 딸기의 무게는 {result}입니다")
