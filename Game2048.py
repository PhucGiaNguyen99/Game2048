
"""
Merge function for 2048 game.
"""
def merge(nums):
    """
    Function that merges a single row or column in 2048.
    """
    # If the line is with length 1, then we cannot merge it. Return the given line.
    if (len(nums) == 1):
        return nums
    else:
        # prev is used to compare, while next_ is used to traverse the list
        prev = None
        result_list = []

        for next_ in nums:
            # if next_ is not 0, skip the loop
            if not next_:
                continue
            # if there is no prev saved, then set prev to the current next considered
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


def merge_test(test):
    """
    Tests whether the merge function passes the given input/ output case.
    Accepts a tuple with 2 values: (input_line, expected_output_line)
    """
    input_line, expected_output_line = test
    if merge(input_line) == expected_output_line:
        return 'PASSED'
    else:
        return 'FAILED'


class Game2048:
    def __init__(self, input_tests):
        self.tests = input_tests

    def run_tests(self):
        """
        Run all the tests in the test suite for the merge function.
        """
        for index, test in enumerate(self.tests):
            print('Test ', str(index + 1) + ': ', str(test[0]), '-->', str(test[1]), '-', merge_test(test))

    def add_test(self, test):
        """
        Adds a test to the test suite.
        :param test:
        :return:
        """
        self.tests.append(test)


tests = [
    ([2, 0, 2, 4], [4, 4, 0, 0]),
    ([0, 0, 2, 2], [4, 0, 0, 0]),
    ([2, 2, 0, 0], [4, 0, 0, 0]),
    ([2, 2, 2, 2, 2], [4, 4, 2, 0, 0]),
    ([8, 16, 16, 8], [8, 32, 8, 0]),
]

merge_test_suite = Game2048(tests)
merge_test_suite.run_tests()
