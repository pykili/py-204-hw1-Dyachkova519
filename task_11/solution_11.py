# your code here
string = input()
count = 1
first = ''
second = ''
firsecond = ''
a = ''
count1 = 0
count2 = 0
for i in string:
    if i == ' ':
        a = count
    count = count + 1
count = 1
for t in string:
    if count < a:
        first = first + t
    elif count > a:
        second = second + t
    count = count + 1
for y in second:
    count2 = count2 + 1
    for z in first:
        count1 = count1 + 1
        if z == y and count1 == count2:
            firsecond = firsecond + z
    count1 = 0
if firsecond == first:
    print('Левое слово существует в правом')
else:
    print('Левое слово не существует в правом')
