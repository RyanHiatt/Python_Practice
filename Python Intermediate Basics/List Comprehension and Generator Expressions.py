# Ctrl + / on highlighted code comments out all the highlighted lines
# i = range(99999)
# for f in i:
#     print(f)

# Ctrl + z = undo
# Ctrl + Shift + z = redo


#List Comprehension []
#Generator ()


# List Comprehension
#xyz = [i for i in range(5)]
# print(xyz)

# xyz = []
# for i in range(5):
#     xyz.append(i)
# print(xyz)

# Generator
# xyz = [i for i in range(5)]
# print('done')
# xyz = (i for i in range(5))
# print(xyz)


input_list = [5, 8, 2, 10, 15, 20, 5, 2, 1, 3, 12, 25, 4]

def div_by_five(num):
    if num % 5 == 0:
        return True
    else:
        return False

xyz = (i for i in input_list if div_by_five(i))

# xyz = []
# for i in input_list:
#     if div_by_five(i):
#         xyz.append(i)

# Option 1
# for i in xyz:
#     print(i)

#Option 2
#[print(i) for i in xyz]
#print(xyz)

xyz = [i for i in input_list if div_by_five(i)]
#print(xyz)
#(print(i) for i in xyz)


#[[print(i, ii) for ii in range(5)] for i in range(5)]
#This is equivalent to:
# for i in range(5):
#     for ii in range(5):
#         print(i, ii)

# xyz =  (((i, ii) for ii in range(1000)) for i in range(1000))
#
# for i in xyz:
#     for ii in i:
#         print(ii)

xyz = (print(i) for i in range(5))

for i in xyz:
    i



