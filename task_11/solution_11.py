# your code here
string = input()
count = 1
first = ''
second = ''
firsecond = ''
for i in string:
    if i == ' ':
        a = count
    count = count + 1
count = 1
for t in string:
    if count < a:
        first = first + t
    elif count > a:
        second = second + i
for y in second:
    for z in first:
        if z == y:
            firsecond = firsecond + z
if firsecond == first:
    print('Левое слово существует в правом')
else:
    print('Левое слово не существует в правом')
