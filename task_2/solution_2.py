# your code here
a = input()
count1 = 0
ma = 0
count = 0
letter = t
for i in a:
    count1 += 1
    count2 = 0
    for t in a:
        count2 += 1
        if i == t and count1 != count2:
            count += 1
            if count > ma:
                ma = count
                letter = t
            count = 0
if ma > 0:
    print(letter)
else:
    print("Все символы встречаются одинаково часто")
