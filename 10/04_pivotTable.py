import pandas as pd

# 나이 데이터 생성
ages = pd.DataFrame({'age': [22, 44, 65, 86, 27, 19, 51, 92, 33, 35, 38, 42, 14, 50, 78]})

# 연령대 구간 지정
bins = [0, 20, 40, 60, 80, 100]

# 연령대 카테고리 생성
age_categories = pd.cut(ages['age'], bins)
ages['age_categories'] = age_categories
print(ages)
print('-' * 50)

# 데이터프레임에 새로운 카테고리 열 추가
ages['age_categories'] = age_categories

# 결과 확인
print(ages)
print('-' * 50)

#연령대별 빈도수 count 가능
result = pd.pivot_table(ages, index='age_categories', aggfunc='count')

print(result)
print('=' * 50)

#--------------------------------------------------------------------------------------------------------------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 예시 데이터프레임 생성
data = {'Grade': np.random.randint(1, 4, size=30),
        'Score': np.random.randint(50, 100, size=30),
        'Subject': np.random.choice(['Math', 'English', 'Korean'], size=30)}
df = pd.DataFrame(data)

# 과목별 평균 성적 계산
pivot_table = df.pivot_table(index='Grade', columns='Subject', values='Score', aggfunc='mean')

# 선 그래프 그리기
pivot_table.plot(kind='line', marker='o')
plt.title('Average Score by Subject and Grade')
plt.xlabel('Grade')
plt.ylabel('Average Score')
plt.legend(title='Subject')
plt.xticks(pivot_table.index)
plt.show()
print('=' * 50)

#--------------------------------------------------------------------------------------------------------------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 예시 데이터프레임 생성
data = {'Grade': np.random.randint(1, 4, size=30),
        'Score': np.random.randint(50, 100, size=30),
        'Subject': np.random.choice(['Math', 'English', 'Korean'], size=30)}
df = pd.DataFrame(data)

# 과목별 평균 성적 계산
pivot_table = df.pivot_table(index='Grade', columns='Subject', values='Score', aggfunc='mean')

# 막대 그래프 그리기
pivot_table.plot(kind='bar')
plt.title('Average Score by Subject and Grade')
plt.xlabel('Grade')
plt.ylabel('Average Score')
plt.legend(title='Subject')
plt.xticks(rotation=0)
plt.show()
