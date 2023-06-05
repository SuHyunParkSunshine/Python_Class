#다음 딕셔너리에 대해 물음에 답하라. 
'''days = {'January':31, 'February':28, 'March':31, 'April':30, 'May':31, 'June':30, 'July':31, 'August':31, 'September':30, 'October':31, 'November':30, 'December':31}'''
#사용자가 월을 입력하면 해당 월에 일수를 출력하라
'''sen = input("월을 입력하세요")
print('일수는 ',days.get(sen)) ''' 
#알파벳 순서로 모든 월을 출력하라
'''days_key = days.keys()
print(sorted(days_key))'''

#일수가 31인 월을 모두 출력하라
'''for mon in days:
    if days[mon] == 31:
        print(mon, end=" ")
print()'''

#월의 일수를 기준으로 오름차순으로 (key-value) 쌍을 출력하라
'''days_item = days.items()
r_days = [(day, month) for (month, day) in days_item] #월과 일의 위치를 바꿔서 일을 앞으로 보내는 코드
r_days.sort()
days2 = [(month, day) for (day, month) in r_days]
print(days2)'''

#사용자가 월을 3자리만 입력하면 월의 일수를 출력하라.(Jan, Feb 등)
'''sen = input("월을 3자리까지 입력하시오: ")
for mon in days:
    if mon[0:3] == sen.title():
        print(days[mon]) #days[키값]을 넣어서 value를 들고 오는 것'''
#---------------------------------------------------------------------------------------------------------------------

#리스트안에 요소들로 딕셔너리가 들어가 있음
d = [{'name':'Todd', 'phone':'555-1414', 'email':'todd@mail.net'}, {'name':'Helga', 'phone':'555-1618', 'email':'helga@mail.net'},{'name':'Princess', 'phone':'555-3141', 'email':''},{'name':'LJ', 'phone':'555-2718', 'email':'lj@mail.net'}]

#전화번호가 8로 끝나는 사용자 이름을 출력하라
for people in d:
    if people['phone'][7] == '8':
        print(people['name'])
print("="*30)
#이메일이 없는 사용자 이름을 출력하라
for people in d:
    if people['email'] == '':
        print(people['name'])
print("="*30)
#사용자 이름을 입력하면 전화번호, 이메일을 출력하라. 이름이 없으면 '이름이 없습니다'라는 메시지를 출력하라
s_name = input("이름을 입력하세요: ")
flag = 1 #순차탐색

for people in d:
    if people['name'] == s_name:
        print(people['phone'], people['email'])
        flag = 0
if flag == 1:
        print("없는 이름입니다")