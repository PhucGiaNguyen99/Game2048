import random


class Week2:
    # Constructor: Given height and width, create the initial board.
    def __init__(self, grid_height, grid_width):
        self.grid_height = grid_height
        self.grid_width = grid_width
        self.board = self.reset()

    # set the board to an empty board.
    # Call method new_tile twice to place 2 random number to the empty.
    def reset(self):
        self.board = [[0 for i in range(self.grid_width)] for j in range(self.grid_height)]
        self.new_tile()
        self.new_tile()
        return self.board

    # 3. Choose a random value to place in the random grid. Return 2 with 90%, and 4 with 10%.
    # Based on the given percentage of each number, add the number of it to the weighted list.
    # Return a random grid with a random index in range of the length of teh weighted list.
    def get_random_value(self):
        weighted_list = [2] * 9 + [4]
        return weighted_list[random.randrange(10)]

    def new_tile(self):
        # Python does not have do- while loop. Therefore, loop condition is True, so the loop stops only
        # when you encounter an empty grid.
        # 1. Choose a random empty grid.
        # 2. Looping until get an empty grid.

        # Get a random value
        rand_val = self.get_random_value()
        while True:
            rand_row = random.randrange(self.grid_height)
            rand_col = random.randrange(self.grid_width)
            # break the loop if the random grid is empty
            if (self.get_tile(rand_row, rand_col) == 0):
                break
        self.set_tile(rand_row, rand_col, rand_val)

    # helper methods
    # Return the height of the grid
    def get_grid_height(self):
        return self.grid_height

    # Return the width of the grid
    def get_grid_width(self):
        return self.grid_width

    # Return string representing the board
    def __str__(self):
        str_result = ""
        for i in range(self.grid_height):
            for j in range(self.grid_width):
                str_result += str(self.board[i][j]) + " "
            str_result += "\n"
        return str_result

    def set_tile(self, row, col, value):
        if (value >= 0 and (row >= 0 and row < self.grid_height) and (col >= 0 and col < self.grid_width)):
            self.board[row][col] = value

    def get_tile(self, row, col):
        return self.board[row][col]


if __name__ == '__main__':
    game = Week2(4, 4)
    # print("Width: ", game.get_grid_width())
    # print("Height: ", game.get_grid_height())
    # print(random.randrange(1, 19))
    print(game.__str__())

    # Test get a random element of a list
    # for i in range(100):
    #   print("Time", i, ": ", game.get_random_value())
'''
    # expected_str = "0 0 0 0\n0 0 0 0\n0 0 0 0\n0 0 0 0\n"
    print("Before: ")
    print(game.__str__())
    row = int(input("Enter row: "))
    col = int(input("Enter col: "))
    val = int(input("Enter val: "))
    print("Replace 1 at board[" + str(row) + "][" + str(col) + "]: ")
    game.set_tile(row, col, val)
    print(game.__str__())'''
