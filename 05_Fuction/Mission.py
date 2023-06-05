#연습문제 1: 1~n까지의 합을 계산하는 함수
def sum_(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total
print(sum_(50))