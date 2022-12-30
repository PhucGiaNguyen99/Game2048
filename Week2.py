class Week2:
    # Constructor: Given height and width, create the initial board.
    def __init__(self, grid_height, grid_width):
        self.grid_height = grid_height
        self.grid_width = grid_width
        self.board = [0 for i in range(self.grid_width) for j in range(self.grid_height)]

    # helper methods
    # Return the height of the grid
    def get_grid_height(self):
        return grid_height

    # Return the width of the grid
    def get_grid_width(self):
        return grid_width

    # Return string representing the board
    def __str__(self):
        str_result = ""
        for i in range(grid_height):
            for j in range(grid_width):
                str_result += board[i][j] + " "
            str_result += "\n"


if __name__ == '__main__':
    game = Week2(4, 4)
    print("Width: ", game.get_grid_width())
    print("Height: ", game.get_grid_height())
