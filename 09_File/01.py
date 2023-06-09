#파일 읽기
file = open("example.txt", "r")

# 파일 내용 전체를 읽습니다.
content = file.read()
print(content)
file.close()
print('-' * 50)

# 파일에서 한 줄을 읽습니다.
line = file.readline()
print(line)

# 파일 전체를 읽고 각 줄을 리스트로 반환합니다.
lines = file.readlines()
print(lines)

file.close()  # 파일을 닫습니다.
print("-" * 50)

file = open("example.txt", "w")
file.write("Hello world \n")
file.write("This is an example file \n")
file.close()

#regular expression
import re

# 문자열의 시작부터 정규표현식과 매칭되는 패턴 찾기
pattern = r"python"
string1 = "python is easy"
string2 = "I love python"
string3 = "Python is fun"

match1 = re.match(pattern, string1)
match2 = re.match(pattern, string2)
match3 = re.match(pattern, string3)

if match1:
    print("매칭된 문자열:", match1.group())  # 매칭된 문자열: python
else:
    print("매칭되지 않음")

if match2:
    print("매칭된 문자열:", match2.group())
else:
    print("매칭되지 않음")

if match3:
    print("매칭된 문자열:", match3.group())
else:
    print("매칭되지 않음")
