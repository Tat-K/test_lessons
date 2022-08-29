import os
#print(os.getcwd())
p = os.getcwd()
#f = open('../../some_file4.txt', 'r', encoding='utf-8')
f = open('new_dir1/new_dir2/new_dir3/some_file.txt', 'r', encoding='utf-8')
print(*f)

