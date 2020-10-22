alphabet = ''
a = ''
for i in 'a' * 10:
    user_input = input()
    a = a + user_input
for t in a:
    if t not in alphabet:
        alphabet = alphabet + t
print(alphabet)
