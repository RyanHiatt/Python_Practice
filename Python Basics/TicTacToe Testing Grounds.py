#import itertools
'''
player_choice = itertools.cycle([1, 2])

for i in range(10):
    print(next(player_choice))
'''

# iterable: a thing we can iterate over
#iterator: a special object with next() method
'''
x = [1, 2, 3, 4]  # iterable

for i in x:
    print(i)
'''

#n = itertools.cycle(x) # iterator

'''
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))
'''


#for i in n:
#    print(i)
'''
y = iter(x)

for i in y:
    print(i)
'''

'''
players = [1, 0]

choice = 1
for i in range(10):
    current_player = choice+1
    print(current_player)
    choice = players[choice]
'''


game_size = 3

print("   0  1  2")

s = "   "+"  ".join([str(i) for i in range(game_size)])

print(s)



