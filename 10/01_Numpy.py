import numpy as np
import matplotlib.pyplot as plt

#1차원 배열
arr1 = np.random.rand(5)
print(arr1)
print("-" * 50)

#linspace함수
#기본 사용법
arr1 = np.linspace(0, 1, num=5)
print(arr1)
print("-" * 50)

#선 그래프
#x, y 데이터 생성
x = np.arange(0, 10, 0.1)
y = np.sin(x)
# 선 그래프 그리기
plt.plot(x, y)

# 그래프 타이틀과 축 라벨 설정
plt.title('Sine Wave')
plt.xlabel('x')
plt.ylabel('y')

# 그래프 출력
plt.show()
print("-" * 50)

#산점도
import numpy as np
import matplotlib.pyplot as plt
# x, y 데이터 생성
x = np.random.rand(100)
y = np.random.rand(100)

# 산점도 그리기
plt.scatter(x, y)

# 그래프 타이틀과 축 라벨 설정
plt.title('Scatter Plot')
plt.xlabel('x')
plt.ylabel('y')

# 그래프 출력
plt.show()

#색상변경
import matplotlib.pyplot as plt
import numpy as np

# 색상 변경 예제
x = np.arange(0, 10, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, color='blue')
plt.plot(x, y2, color='#FF5733')
plt.title('Sine and Cosine Waves')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
