import random

lotto = set()
while len(lotto) < 6:
    n = random.randint(1, 45)
    lotto.add(n)    
print(lotto)
print(sorted(lotto))

#연습문제 1: 학생들의 성적을 딕셔너리로 저장하고, 성적 평균을 계산하는 프로그램을 작성해보세요.
data = {
    "Alice": [85, 90, 95],
    "Bob": [75, 80, 85],
    "Charlie": [95, 95, 95]
}
for name, grade_list in data.items():
    avg = sum(grade_list) / len(grade_list)
    print(name, ":", avg)
print('='*30)
#연습문제 2: 숫자들이 들어있는 리스트에서 중복된 숫자를 제거하고, 남은 숫자들의 합을 계산하는 프로그램을 작성해보세요
numlist = [1, 2, 2, 3, 3, 3, 4, 4, 5]
newSet = set(numlist)
sum = 0
for s in newSet:
    sum += s
print(sum)

'''total = sum(set([1, 2, 2, 3, 3, 3, 4, 4, 5]))
print(total)'''

print('='*30)

#연습문제 3: 주어진 문자열에서 각 알파벳의 빈도수를 구하는 프로그램을 작성하시오.
text = "Hello, world!"
freq_dict = {}
for char in text:
    if char not in freq_dict:
        freq_dict[char] = 1
    else:
        freq_dict[char] += 1
print(freq_dict)
print('='*30)

#연습문제 4: 두 개의 리스트가 주어졌을 때, 두 리스트에 공통으로 포함된 요소를 모두 담은 리스트를 반환하는 프로그램을 작성하시오.
set1 = set([1, 2, 3, 4, 5])
set2 = set([2, 4, 6, 8, 10])
print(list(set1 & set2))
print(list(set1.intersection(set2)))