#some_fileimport os
#print(os.getcwd())
#p = os.getcwd()
#f = open('new_dir1/new_dir2/new_dir3/some_file.txt', 'r', encoding='utf-8')
#f.write('python')
#f.close()




#try:
    #f = open('some_file.txt', 'r', encoding='utf-8')
    #f.write('python')
#except:
    #print('Произошла ошибка')
#finally:
    #print('файл закрыт')
    #f.close()

with open('some_file.txt', 'r', encoding='utf-8') as f:
    print(*f)
    