'''
Implement the Mimi-project 2048:
- A given tile can only merge once on any given turn, although many pairs of tiles could merge on a single turn.
- Week 1: Implement the merge function. Steps:
1. Start with a result list that contains the same number of 0's as the length of the line argument.
2. Iterate over the line input looking for non-zero entries. For each non-zero entry, put the value into the next available entry of the result list. Starting at position 0.
Ex: [2, 0, 2, 2]-> [2, 2, 2, 0]

REMEMBER: Any tile should only be merged once and that these merges should happen in order from lowest to highest index.
Ex: [2, 0, 4, 4]-> [2, 4, 4, 0]-> [2, 8, 0, 0]
[0, 0, 2, 2]-> [0, 2, 2, 0]-> [2, 2, 0, 0]-> [4, 0, 0, 0]

'''
if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    # numbers[-1:]
    # for i in numbers[-1:]:
    #     print(i)
    # print(numbers[:-1])
    # print(numbers[1:])
