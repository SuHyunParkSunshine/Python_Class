#경로를 읽을 수 없는경우 하기처럼 절대경로로 하면 콘솔에 찍힘
import pandas as pd
df = pd.read_csv('C:/Python/10/tips.csv')
print(df.head())