import os
impassable = "MX*|_-="
interactive = "@$"
terrain = " /#"

#Ititializes a L * W * H Map
class Board:
    board = []

    def __init__(self, l: int, w: int, h:int):
        #Creates a gameboard. A list of lists, the first list is each floor, the second list is the row, and the third is the place along the row.
        
        board = []
        for height in range(h):
            floor = []
            for length in range(l):
                row = []
                for width in range(w):
                    row.append(f"|{length}{width}{height}|")
                floor.append(row)
            board.append(floor)
        self.board = board
        print(board)

    def display(self):
        """Interprets and prints board"""
        floor = 0
        board = []
        for height in range(len(self.board)):
            floors = []
            floor += 1
            disped = False
            for length in range(len(self.board[height])):
                disp = ''.join(self.board[height][length])
                if disped == False:
                    print(f'\nThis is floor {floor} of {len(self.board)}\n')
                    disped = True
                print(disp)

    def movement(self, pos:list , underpos: str):
        """Moves player on a board, knowing its initial position."""
        global impassable
        global interactive
        global terrain
        x, y, z = pos[0], pos[1], pos[2]
        while True:
            inputvar = input("Awaiting input: ")
            #Checks each character in the input to check if it's relevant.
            for char in inputvar:
                #Same chunk of code 4 times for each direction.
                if char == 'w':
                    print("You moved up!")
                    if self.board[z][y-1][x] in terrain:
                        self.board[z][y][x] = underpos
                        underpos = self.board[z][y-1][x]