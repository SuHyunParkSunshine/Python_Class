import pandas as pd

data = {'이름': ['John', 'Steve', 'Sarah', 'Ann', 'Mike'],
        '나이': [25, 32, 28, 35, 41],
        '성별': ['남', '남', '여', '여', '남'],
        '키': [175, 180, 163, 155, 190]}
df = pd.DataFrame(data)
print(df)
print('-' * 50)
# 1.'학년' 열을 추가하고, 모든 행에 '3학년'이라는 값으로 채워 넣으세요.
df['학년'] = '3학년'
print(df)
print('-' * 50)
# 2.'국적' 열을 추가하고, 각 행에 해당하는 사람의 국적을 채워 넣으세요.
df['국적'] = ['미국', '영국', '일본', '한국', '중국']
print(df)
print('-' * 50)
# 3.'성별'이 '여'인 행만 남기고 나머지 행을 삭제하세요.
df = df[df['성별'] == '여']
print(df)
print('-' * 50)
# 4.'나이' 열을 기준으로 내림차순으로 행을 정렬하세요.
df = df.sort_values(by='나이', ascending=False)
print(df)
print('-' * 50)
# 5.인덱스가 2인 행을 삭제하세요.
df = df.drop(2)
print(df)
print('-' * 50)
# 6.아래 새로운 행 3개를 추가하세요.
new_row = [{'이름': 'Alex', '나이': 22, '성별': '남', '키': 180, '학년': '2학년', '국적': '미국'}, {'이름': 'Emily', '나이': 29, '성별': '여', '키': 165, '학년': '1학년', '국적': '캐나다'}, {'이름': 'Daniel', '나이': 33, '성별': '남', '키': 175, '학년': '3학년', '국적': '호주'}]
df = df.append(new_row, ignore_index=True)
print(df)
print('-' * 50)
# 7.'이름' 열을 기준으로 오름차순으로 행을 정렬하세요.
df = df.sort_values('이름', ascending=True)
print(df)
print('-' * 50)
# 8.'키' 열의 값을 cm에서 m로 변환하세요.
df['키'] = df['키'] / 100
print(df)
print('-' * 50)
# 9.'성별' 열을 삭제하세요.
df = df.drop('성별', axis=1)
print(df)
print('-' * 50)
