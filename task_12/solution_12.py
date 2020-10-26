# your code here
a = input()
count1 = 0
count2 = 0
b = a[0]
c = a[0]
occured_twice = False
for i in a:
    bi1 = b + i
    count2 = 0
    count1 += 1
    for t in a:
        bi2 = c + t
        count2 += 1
        if bi1 == bi2 and count1 != count2 and count1 != 1 and count2 != 1:
            occured_twice = True
        c = t
    b = i
print(occured_twice)
