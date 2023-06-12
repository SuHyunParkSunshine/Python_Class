#그래프 예제1 ------------------------------------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt

months = np.arange(1, 13)  # 월별 데이터
sales = np.array([120, 145, 98, 156, 104, 176, 155, 140, 135, 120, 148, 170])  # 월별 판매량
#plt.style.use('default') --> 전의 스타일 때문에 스타일 적용이 전의 것과 같이 되는 경우, default로 해서 초기화 시켜주기
plt.plot(months, sales, color='blue', marker="o")
plt.grid(True)

plt.title('Monthly Sales Performance')
plt.xlabel('Months')
plt.ylabel('Sales')

plt.show()

#그래프 예제2 ------------------------------------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt

months = np.arange(1, 13)  # 월별 데이터
product1_sales = np.array([120, 145, 98, 156, 104, 176, 155, 140, 135, 120, 148, 170])  # 물건 1 월별 판매량
product2_sales = np.array([90, 110, 80, 120, 105, 140, 130, 125, 115, 100, 130, 150])  # 물건 2 월별 판매량

plt.plot(months, product1_sales, color='blue', marker='o', label='Product 1')
plt.plot(months, product2_sales, color='red', marker='o', label='Product 2')
plt.grid()

plt.title('Monthly Sales Performance')
plt.xlabel('Months')
plt.ylabel('Sales')

plt.show()

#그래프 예제3 ------------------------------------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt

#fig = plt.figure(figsize=(3, 2)) --> 그래프 사이즈 변경 하는 법

years = np.arange(2010, 2021)  # 연도 데이터
gdp_a = np.array([100, 120, 150, 160, 180, 200, 220, 240, 260, 280, 300])  # A 나라의 연도별 GDP
gdp_b = np.array([80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180])  # B 나라의 연도별 GDP
gdp_c = np.array([200, 220, 240, 250, 260, 270, 280, 290, 300, 310, 320])  # C 나라의 연도별 GDP

bar_width = 0.25
index = np.arange(len(years))
print(index)

plt.bar(index, gdp_a, 0.25, color='blue', label='Country A')
plt.bar(index + bar_width, gdp_b, 0.25, color='red', label='Country B')
plt.bar(index + bar_width*2, gdp_c, 0.25, color='green', label='Country C')
plt.xticks(index + bar_width, years) #index에다가 years의 값을 넣어라
plt.grid()

plt.title('GDP Comparison by Country')
plt.xlabel('Years')
plt.ylabel('GDP(in billions)')

plt.show()

#그래프 예제4 ------------------------------------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt

years = np.arange(2010, 2021)
gdp = np.array([100, 120, 150, 160, 180, 200, 220, 240, 260, 280, 300])
sales = np.array([50, 70, 30, 45, 60, 80, 70, 90, 110, 100, 120])
prices = np.array([10, 12, 15, 16, 18, 20, 22, 24, 26, 28, 30])

#그리드 설정
fig = plt.figure()

#첫 번째 서브플롯
ax1 = plt.subplot2grid((3, 3), (0, 0), 1, 3)
ax1.plot(years, gdp, color='blue', marker='o')
ax1.set_title('GDP')
ax1.set_xlabel('Years')
ax1.set_ylabel('GDP(in billions)')

#두 번째 서브플롯
ax2 = plt.subplot2grid((3,3), (1, 0), 1, 2)
ax2.bar(years, sales, color='green')
ax2.set_title('Sales')
ax2.set_xlabel('Years')
ax2.set_ylabel('Quantity Sold')

#세 번째 서브플롯
ax3 = plt.subplot2grid((3, 3), (2, 0), 1, 2)
ax3.plot(years, sales, color='blue', marker='o')
ax3.set_title('Sales')
ax3.set_xlabel('Years')
ax3.set_ylabel('Quantity Sold')

#네 번째 서브플롯
ax4 = plt.subplot2grid((3, 3), (1, 2), 2, 1)
ax4.scatter(years, prices, color='red', marker='o', s=10)
ax4.set_title('Prices')
ax4.set_xlabel('Years')
ax4.set_ylabel('Price')

#그래프 간격 조정
plt.tight_layout()

#그래프 표시
plt.show()

#DataFrame 정보 확인 예제 ------------------------------------------------------------------------------------------------------
import pandas as pd

# 데이터프레임 생성
data = {'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'age': [25, 30, 35, 40, 45],
        'city': ['New York', 'Paris', 'London', 'Berlin', 'Tokyo']}
df = pd.DataFrame(data)
# 데이터프레임 정보 출력
print(df.head())
#열선택과 행선택을 동시에 사용해서 그래프를 그리는 예제 ------------------------------------------------------------------------------------------------------
# year 열에서 2019년 이상의 데이터를 선택하고, 그에 해당하는 year, A_product_sales, B_product_sales 열을 선택
import pandas as pd
import matplotlib.pyplot as plt
data = {
    'year': [2017, 2018, 2019, 2020, 2021],
    'A_product_sales': [6, 7, 8, 9, 10],
    'B_product_sales': [11, 12, 13, 14, 15],
    'C_product_sales': [9, 8, 7, 6, 5]
}
df = pd.DataFrame(data)
df = df.loc[df['year'] >= 2019, ['year', 'A_product_sales', 'B_product_sales']]
plt.plot(df['year'], df['A_product_sales'], marker='o', label='A_product')
plt.plot(df['year'], df['B_product_sales'], marker='o', label='B_product')

plt.legend()
plt.show()

#데이터 입출력 예제 ------------------------------------------------------------------------------------------------------
import pandas as pd
df = pd.read_csv('C:\Python\10\tips.csv')
print(df.head())