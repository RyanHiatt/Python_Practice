example = ['left', 'right', 'up', 'down']

#Method 1
for i in range(len(example)):
    print(i, example[i])

#Method 2 "Correct"
for i, j in enumerate(example):
     print(i, j)

#Example
new_dict = dict(enumerate(example))
print(new_dict)
[print(i, j) for i, j in enumerate(new_dict)]
