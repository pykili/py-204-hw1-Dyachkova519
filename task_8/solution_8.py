# your code here
n = int(input())
n1 = 'a' * n #создаем строку длиной n
summ = 0 #счетчик суммы чисел
count = 0 #счетчик количества слагаемых
for i in n1:
    num = int(input())
    summ = summ + num
    count = count + 1
    if num == 0: 
        print(summ / count)
