numbers_1 = (1, 2, 3)
numbers_2 = (6,)
numbers_3 = (7, 8, 9, 10, 11, 12, 13)
t = numbers_1 * 2 + numbers_2 * 9 + numbers_3
l = list(t)
l2 = l[::2]
l3 = sum(t)
l4 = l2.append(int(l3))
print(l2)
print(l3)
