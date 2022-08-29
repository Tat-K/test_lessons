a = [[1, 2, 3],
[4, 5, 6],
[7, 8, 9],
[5, 4, 3]]
m = [[row[i] for row in a[::-1]] for i in range(len(a[0]))]

m1 = [[row[i] for row in m[::-1]] for i in range(len(m[0]))]
print(m1)
