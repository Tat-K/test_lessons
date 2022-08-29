with open('example.txt') as f:
    s = ' '.join([line.strip() for line in f])
numbers = []
letters = {}

for i in s:
    if i.isdigit():
        numbers.append(i)
    else:
        if i not in letters:
            letters[i] = 1
        else:
            letters[i] += 1
print(sum(map(int, numbers)))
print(*sorted(letters.items()))
