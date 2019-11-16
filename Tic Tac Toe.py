from itertools import  *
import random


nums = [0,0,1,1,2,2]
master = list(set(permutations(nums,2)))
random.shuffle(master)
print(master)


board = [['_' * 3] * 3]
board = [['_', '_','_'] ,['_', '_','_'] ,['_', '_','_'] ]
next = 1

def play(next):
    while bool(next):
        for row in board:
            for blank in row:
                print("\t\t", blank, end=" ")
            print("\n")

        coordinates = input("Give the coordinates of the place where you want to input in the form (X,Y).\n")

        x = int(coordinates[1]) ;y = int(coordinates[3]);

        temp = (int(x), int(y))
        attempts = []
        if (temp not in attempts) and (temp in master):
            board[x][y] = 'X'
            usrcoors = (x,y)
            attempts.append(usrcoors)
            master.remove(usrcoors)
        else:
            print("Position alraedy occupied.")
        xc = master[0][0]; yc = master[0][1];
        board[xc][yc] = 'O'

        master.remove(master[0])

        for i in range(0, len(board)):
            if((board[0][i] == board[1][i] == board[2][i] != '_') | (board[i][0] == board[i][1] == board[i][2] != '_')):
                if (bool(board[i][0] == 'X') | bool(board[0][i] == 'X')):
                    print("Human wins!!!!")
                else:
                    print("AI is the future!!!!")
                next = 0
            elif((board[0][0] == board[1][1] == board[2][2] != '_') | (board[2][0] == board[0][2] == board[1][1] != '_')):
                if (board[0][0] == 'O') | (board[0][2] == 'O'):
                    print("AI is the future!!!!")
                next = 0


    for row in board:
        for blank in row:
            print("\t\t", blank, end=" ")
        print("\n")

play(next)