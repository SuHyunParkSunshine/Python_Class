# sen = input("문장 입력하시오!")

#문자열의 문자수를 출력하라
# print(len(sen))

#문자열을 10번 반복한 문자열을 출력하라
#print(sen * 10)

#문자열의 첫 번째 문자를 출력하라
#print(sen[0])

#문자열에서 처음 3문자를 출력하라
#print(sen[:3])

#문자열에서 마지막 3문자를 출력하라
# print(sen[-3:])

#문자열의 문자를 거꾸로 출력하라
# print(sen[::-1])

#문자열에 7번째 문자가 있으면 출력하고 없으면 '문자가 없습니다'라는 메시지를 출력하라
# if(len(sen) >= 7):
#     print(sen[6])

#문자열에서 첫 번째 문자와 마지막 문자를 제거한 문자열을 출력하라


#문자를 모두 대문자로 변경하여 출력하라


#문자를 모두 소문자로 변경하여 출력하라


#문자열에서 'a'를 'e'로 대체하여 출력하라


#문자 'a'가 들어가는 단어를 키보드에서 입력 받아 첫 번째 줄에는 'a'까지의 문자열을 출력하고 두 번째 줄에는 나머지 문자열을 출력하는 프로그램을 작성하라.
'''word = input("단어를 입력하세요.")
index_a = word.find('a')

if index_a != -1:
    print(word[:index_a + 1])
    print(word[index_a + 1:])
else:
    print(word)'''

#연습문제 2
#예시
num = str(input("숫자를 입력하세요"))

sum = 0
for s in num:
    sum += int(s)
print(sum)

#1~1000까지의 숫자의 각 자리수의 합
for num in range(1, 1001):
    sum = 0
    for s in str(num):
        sum += int(s)
print(sum)