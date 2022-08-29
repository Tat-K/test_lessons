with open('users_file.txt', 'a+', encoding='utf-8') as f:
    while True:
        s = input()
        if s != '':
            f.write(s + '\n')
        else:
            break


