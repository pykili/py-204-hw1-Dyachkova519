count = 1
a = ''
b = ''
c = ''
form = ''
lemma = ''
k = ''
for i in 'k' * 10:
    string = input()
    if string != '' and string[0] != '#':
        for i in string:
            if i == '\t':
                c = b
                b = a
                a = count
            count = count + 1
        count = 1
        for t in string:
            if count > c and count < b:
                form = form + t
            count = count + 1
        count = 1
        for x in string:
            if count > b and count < a:
                lemma = lemma + x
            count = count + 1
        if form != lemma:
            print(form, lemma)  
