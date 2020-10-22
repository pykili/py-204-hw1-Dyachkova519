# your code here
a = 'a' * 100
count = 1
count1 = 1
b = 0
for i in a:
    b = b + count
    c = count1 * count1
    count = count + 2
    count1 = count1 + 1
    print(b == c) #я не совсем поняла, какие данные должны выводиться в задаче, поэтому программа 100 раз выдаст True
