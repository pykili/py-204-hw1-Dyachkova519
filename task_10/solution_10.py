# your code here
string = input()
a = ''
for i in string:
    a = i + a
is_palindrom = a == string
print(is_palindrom)
