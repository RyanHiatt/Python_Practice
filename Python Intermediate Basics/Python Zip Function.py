x = [1, 2, 3, 4]
y = [7, 6, 2, 1]
z = ['a', 'b', 'c', 'd']

# for a,b,c in zip(x, y, z):
#     print(a, b)

# print(zip(x, y, z))
#
# for i in zip(x, y, z):
#     print(i)
#
# print(list(zip(x, y, z)))
#
# print(dict(zip(x, y)))
#
# [print(a, b, c) for a, b, c in zip(x, y, z)]

[print(x, y) for x, y in zip(x, y)]
print(x)

[print(a, b) for a, b in zip(x, y)]

#variable a is saved
for a, b in zip(x, y):
    print(a, b)
print(a)

for x, y in zip(x, y):
    print(x, y)
print(x)