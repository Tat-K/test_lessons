with open('some_file.txt', 'r', encoding='utf-8') as f:
    #print(f.name, f.encoding, f.closed)
    #lines = [line.strip() for line in f.readlines()]
    print(f.readline())

#print(lines)
