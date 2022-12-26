import main


class Game2048:
    def __init__(self, board):
        self.board = board

    def print(self):
        for i in self.nums:
            print(i, end=" ")

    def merge(self, nums):
        # prev is used to compare, while next_ is used to traverse the list
        prev = None
        result_list = []
        for next_ in nums:
            # print("prev: " + str(prev) + "\n")
            # print("Next: " + str(next_) + " ")
            # if next_ is not 0, skip the loop
            if not next_:
                continue
            if prev is None:
                prev = next_
            elif prev == next_:
                # skip the comparison of the previous element and the next_ element after merging that pair
                # by resetting prev to None
                result_list.append(prev + next_)
                prev = None
            else:
                result_list.append(prev)
                prev = next_
        if prev is not None:
            result_list.append(prev)
        # fill in 0s in the remaining positions of the result list
        result_list.extend([0] * (len(nums) - len(result_list)))
        return result_list


if __name__ == '__main__':
    list = [8, 16, 16, 8]
    game_play = Game2048(list)
    # game_play.print()
    for i in game_play.merge(game_play.nums):
        print(i, end=" ")
