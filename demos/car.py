# ENUM ENUMERATION IN PYTHON
class CardinalDirection:
    NORTH = 0  # UP
    EAST = 1  # RIGHT
    SOUTH = 2  # DOWN
    WEST = 3  # LEFT


class TurnDirection:
    LEFT = 0
    RIGHT = 1


# possible_directions = [0, 1, 2, 3]
# possible_directions = ['N', 'E', 'S', 'W']
# NORTH = 0
# EAST = 1
# SOUTH = 2
# WEST = 3


class Player:
    symbols = {
        0: "^",
        1: ">",
        2: "v",
        3: "<",
    }
    symbols = [
        "^",
        ">",
        "v",
        "<",
    ]

    symbols = "^>v<"
    symbols = "North, East, South, West".split(", ")
    # CONSTRUCTOR
    def __init__(self):
        self.facing = CardinalDirection.EAST
        # self.facing = 1  # index into 'E'
        # self.facing = possible_directions[1]  # actual string 'E'

    def turn(self, direction):
        # USE MODULO DIVISION OPERATOR TO WRAP AROUND
        if direction == TurnDirection.LEFT:
            self.facing = (self.facing - 1) % 4
        elif direction == TurnDirection.RIGHT:
            self.facing = (self.facing + 1) % 4

    def show(self):
        # A SWITCH STATEMENT IN PYTHON IS JUST A LOT OF ELIFS
        if self.facing == 0:
            symbol = "^"
        elif self.facing == 1:
            symbol = ">"
        elif self.facing == 2:
            symbol = "v"
        elif self.facing == 3:
            symbol = "<"
        else:
            raise ValueError
        print(symbol)


if __name__ == "__main__":
    p = Player()

    p.show()

    p.turn(TurnDirection.RIGHT)
    p.show()
    p.turn(TurnDirection.RIGHT)
    p.show()
    p.turn(TurnDirection.RIGHT)
    p.show()
    p.turn(TurnDirection.RIGHT)
    p.show()

# screen = (
#     (0, 0, 0, 0, 0, 0, 0, 0, 0),
#     (0, 0, 0, 0, 0, 0, 0, 0, 0),
#     (0, 0, 0, 0, 0, 0, 0, 0, 0),
#     (0, 0, 0, 0, 0, 0, 0, 0, 0),
#     (0, 0, 0, 0, 0, 0, 0, 0, 0),
#     (0, 0, 0, 0, 0, 0, 0, 0, 0),
#     (0, 0, 0, 0, 0, 0, 0, 0, 0),
#     (0, 0, 0, 0, 0, 0, 0, 0, 0),
#     (0, 0, 0, 0, 0, 0, 0, 0, 0),
# )
# p.player(1, 4, 4)
