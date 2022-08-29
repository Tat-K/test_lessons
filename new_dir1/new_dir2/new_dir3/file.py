import os
#print(os.getcwd())
p = os.getcwd()
f = open('../../some_file4.txt', 'r', encoding='utf-8')
print(*f)

