'''
game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]


def game_board(game_map, player=0, row=0, column=0, just_display = False):
    try:
        print("   0  1  2")
        if not just_display:
            game_map[row][column] = player
        for count, row in enumerate(game_map):
            print(count, row)
        return game_map

    except IndexError as e:
        print("Error: make sure you input row/column as 0, 1, or 2.", e)

    except Exception as e:
        print("Something went very wrong!", e)
game = game_board(game, just_display=True)
game = game_board(game, player=1, row=3, column=1)
'''


#mutability of a string example
'''
game = [1, 2, 3]
#print(id(game))

def game_board(player=0, row=0, column=0, just_display = False):
    game[1] = 99
#    print(id(game))
    print(game)

print(game)
game_board()
print(game)
#print(id(game))
'''

#mutability example of a string using global
'''game = "I want to play a game"
print(id(game))

def game_board(player = 0, row = 0, column = 0, just_display = False):
    global game
    game = "A game"
    print(id(game))
    print(game)

game_board()
print(game)
print(id(game))
'''


'''
game = [[1, 0, 2],
        [1, 1, 0],
        [2, 2, 1]]
'''


#win conditions
#horizontally
#vertically
#diagnolly


#horizontal
'''
def win(current_game):
    for row in game:
        print(row)
        if row.count(row[0]) == len(row) and row[0] != 0:
            print("Winner!")

win(game)
'''

#vertical
'''
for col in range(len(game)):
    check = []

    for row in game:
        #print(row[0])
        check.append(row[col])

    if check.count(check[0]) == len(check) and check[0] != 0:
        print("Winner!")
'''

#diagnol

#hard coded, not dynamic
'''
if game [0][0] == game[1][1] == game[2][2]:
    print("Winner!")
if game[2][0] == game[1][1] == game [0][2]:
    print("Winner!")
'''


#for col, row, in zip(reversed(range(len(game))), range(len(game))):
#    print(col, row)


#actual diagnol
'''
diags = []
for col, row in enumerate(reversed(range(len(game)))):
    diags.append(game[row][col])

diags = []
for ix in range(len(game)):
    diags.append(game[ix][ix])
'''


'''
diags = []
for ix in range(len(game)):
    diags.append(game[ix][ix])
print(diags)
'''


#Putting it together
import itertools


def win(current_game):

    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
        else:
            return False

    # Horizontal
    for row in game:
        print(row)
        if all_same(row):
            print(f"Player {row[0]} is the winner horizontally '-'!")
            return True

    # Vertical
    for col in range(len(game)):
        check = []

        for row in game:
            check.append(row[col])

        if all_same(check):
            print(f"Player {check[0]} is the winner vertically '|'!")
            return True

    # / Diagonal
    diags = []
    for col, row in enumerate(reversed(range(len(game)))):
        diags.append(game[row][col])
    if all_same(diags):
        print(f"Player {diags[0]} is the winner diagonally '/'!")
        return True

    # \ Diagnal
    diags = []
    for ix in range(len(game)):
        diags.append(game[ix][ix])
    if all_same(diags):
        print(f"Player {diags[0]} is the winner diagonally '\\'!")
        return True

    return False


def game_board(game_map, player=0, row=0, column=0, just_display = False):
    try:
        if game_map[row][column] != 0:
            print("This position has already been selected! Choose another position!")
            return game_map, False
        print("   " + "  ".join([str(i) for i in range(len(game_map))]))
        if not just_display:
            game_map[row][column] = player
        for count, row in enumerate(game_map):
            print(count, row)
        return game_map, True

    except IndexError as e:
        print("Error: make sure you input row/column as 0, 1, or 2.", e)
        return game_map, False

    except Exception as e:
        print("Something went very wrong!", e)
        return game_map, False


play = True
players = [1, 2]
while play:
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]

    game_won = False
    game, _ = game_board(game, just_display=True)
    player_choice = itertools.cycle([1, 2])
    while not game_won:
        current_player = next(player_choice)
        print(f"Current Player: {current_player}")
        played = False

        while not played:
            column_choice = int(input("What column do you want to play? (0, 1, 2): "))
            row_choice = int(input("What row do you want to play? (0, 1, 2): "))
            game, played = game_board(game, current_player, row_choice, column_choice)

        if win(game):
            game_won = True
            again = input("The game is over, would you like to play again? (y/n)")
            if again.lower() == "y":
                print("Restarting")
            elif again.lower() == "n":
                print("Hope you enjoyed! Goodbye!")
                play = False
            else:
                print("Not a valid answer.")
                play = False
