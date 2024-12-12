

#Агафонов Х-71 уровень сложный
#number 1
#n2

number = int(input('ведите число от 1 до 10'))
flag = False
while not flag:
    if number <= 0 or number > 10:
        print('от 1 до 10')
        number = int(input('введите число от 1 до 10'))
    else :
        flag = True
for i in range (1,11):
    print(number * i)
#n3
import math
n = int(input())
k = int(input())
def C(n,k) :
    print(math.factorial(n) / (math.factorial(n) * math.factorial(n-k)))

