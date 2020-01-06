import logging

# class range_examp:
#     def __init__(self, end, step = 1):
#         self.current = 0
#         self.end = end
#         self.step = step
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.current >= self.end:
#             raise StopIteration()
#         else:
#             return_val = self.current
#             self.current += self.step
#             return return_val
#
#
# x = range_examp(5)
#
# x.__next__()
# next(x)
#
# for i in x:
#     print(i)

logging.basicConfig(filename='testlogfile.log', level=logging.INFO)

def range_gen(end):
    current = 0
    while current < end:
        yield current
        current += 1

logging.info('the current iteration of range_gen is {}'.format(str(range_gen)))

for i in range_gen(5):
    print(i)

x = range_gen(5)

x.__next__()

for i in x:
    print(i)

logging.info('the current iteration of x is {}'.format(str(x)))