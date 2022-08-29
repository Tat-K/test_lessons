with open('some_file.txt', 'r', encoding='utf-8') as f:
    #print(f.name, f.encoding, f.closed)
    #lines = [line.strip() for line in f.readlines()]
    print(f.read(100))
    print(f.read(5))
    print(f.seek(0))
    print(f.read(10))