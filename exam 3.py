with open('some_file.txt', encoding='utf-8') as f:
    lines = [line.strip() for line in f]
for i, l in enumerate(lines, 1):
    print(i, len(l))
print(len(lines))
