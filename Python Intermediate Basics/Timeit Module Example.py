#Using timeit to test speeds of generator vs list comprehension
import timeit

# input_list = range(100)
#
# def div_by_five(num):
#     if num % 5 == 0:
#         return True
#     else:
#         return False
#
# #Generator
# xyz = (i for i in input_list if div_by_five(i))
# #List Comprehension
# xyz = [i for i in input_list if div_by_five(i)]
# #Generator converted to list
# xyz = list(i for i in input_list if div_by_five(i))

#timeit Example
# print(timeit.timeit('1+3', number = 500000000))
# time ~ 3.82 seconds to add '1+3' 500000000 times


print(timeit.timeit('''input_list = range(100)

def div_by_five(num):
    if num % 5 == 0:
        return True
    else:
        return False

#Generator
xyz = (i for i in input_list if div_by_five(i))
#List Comprehension
xyz = [i for i in input_list if div_by_five(i)]
#Generator converted to list
xyz = list(i for i in input_list if div_by_five(i))''', number = 5000))

#Time Comparisons
#As a generator time ~ 0.00232 seconds
#As a list comprehension time ~ 0.06322
#Converting a generator to a list time ~ 0.0651