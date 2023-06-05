#remove
'''my_list = [1, 2, 3, 4]
my_list.remove()
print(my_list)'''

#Mission1
namelist = ['예진', '원준', '수연']
namelist.insert(0, '지은')
namelist.insert(2, '아무개')
namelist.append('누구누구')
print(namelist)

#Mission2
numlist = [1, 2, 3]
del numlist[1]
numlist.insert(1, 17)
numlist += [4, 5, 6]
del numlist[0]
numlist.sort()
numlist.insert(3, 25)
print(numlist)

#연습문제1
lis = []
'''for s in range(0, 50):
    lis.append(s)
print(lis)'''

for ss in range(0, 51):
    lis.append(ss**2)
print(lis)

#연습문제 2
L = [1, 2, 3]
M = [4, 5, 6]
newList = []
for i in len(L):
    l = L[i] + M[i]
    newList.append(l)
print(newList)