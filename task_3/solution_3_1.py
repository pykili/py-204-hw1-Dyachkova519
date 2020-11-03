# your code here
user_input = input()
alphabet = ''
for i in user_input:
    if i not in alphabet:
        alphabet = alphabet + i
print(alphabet)
