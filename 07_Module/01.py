import random, os, mymath

print(help(random.choice))
print("-" * 50)
print(os.getcwd())

#사용자 정의 모듈을 작성하여 간단한 수학 연산을 수행해 보세요.
print(mymath.add(5, 2))
print(mymath.subtract(4, 3))
print(mymath.multiply(6, 2))
print(mymath.divide(4, 2))
print(mymath.divide(5, 0))