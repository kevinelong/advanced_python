"""
Draughts is played by two opponents, 
on opposite sides of the gameboard.
 One player has the dark pieces; 
 the other has the light pieces. 
 Players alternate turns. 
 A player may not move an opponent's piece. 
 A move consists of moving a piece diagonally to an adjacent unoccupied square. 
 If the adjacent square contains an opponent's piece, 
 and the square immediately beyond it is vacant, 
 the piece may be captured (and removed from the game) 
 by jumping over it.

Only the dark squares of the checkered board are used. 
A piece may move only diagonally into an unoccupied square. 
When presented, capturing is mandatory in most official rules, 
although some rule variations make capturing optional.[3] 
In almost all variants, 
the player without pieces remaining, 
or who cannot move due to being blocked, loses the game. 

NOUNS (): Player Piece Board Square Turn Game
VERB: Move Capture Alternate(Switch whose turn)
ADJ: Color(Light Dark) WhoseTurn Direction, Remaining occupied=(True/False), (Man or King), whose_turn

RELATIONSHIPS:

Game has Player List
Player has a Color (light/dark)
Game has a alternating turn (whose turn is it) LightPlayer or DarkPlayer
Player has list pieces
Player can Move a piece to valid square for that piece
Board has squares squares have color.
Board has list of light squares and list of dark squares.
Piece is a man or king.
Game knows who turn it is.

The tasks:
    Create a board
    add a piece to the board
    show the board

    create a player
    add player to game
    toggle current player
    display whose turn it is (light/or dark to play)

save is_valid? for  last

1. create empty classes for the nouns from simplest to most complex
2. make sure code runs
"""
class Color:
    pass

class Piece: 
    pass

class Player:
    pass

class Square:
    pass

class Board:
    def __init__(self, size=8):
        self.size = size
        self.rows = []
        self.clearBoard()
    def clearBoard(self):
        count = 0
        rows = []
        for _ in range(self.size):
            row = []
            for __ in range(self.size):
                if count % 2 == 0: #even or odd using modulus operator
                    row.append('.')
                else:
                    row.append(',')
                count += 1
            rows.append(row)
            count += 1
        self.rows = rows
    def place(self, row, column, symbol):
        self.rows[row][column] = symbol
    def display(self):
        for row in self.rows:
            for col in row:
                print(col, end=" ")
            print("")
class Game:
    def __init__(self):
        self.board = Board(8)
board = Board()
board.place(3,3,"@")
board.place(7,7,"O")
board.display()

# print( 14 % 2) # modulo division remainder operator

# size = 8
# rows = []
# count = 0

# for index in range(size):
#     row = []
#     for _ in range(size):
#         if count % 2 == 0: #even or odd using modulus operator
#             row.append('.')
#         else:
#             row.append(',')
#         count += 1
#     rows.append(row)
#     count += 1
# print(rows)

# for row in rows:
#     for col in row:
#         print(col, end=" ")
#     print("")

# EXPECTED OUTPUT
"""
. , . , . , . ,
, . , . , . , .
. , . , . , . ,
, . , . , . , .
. , . , . , . ,
, . , . , . , .
. , . , . , . ,
, . , . , . , .
"""