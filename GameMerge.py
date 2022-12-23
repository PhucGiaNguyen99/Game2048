from queue import Queue


class GameMerge:
    '''
        Method Merge implementations:
        1. Put non-zero elements into a queue.
        2. Compare previous element and current element that the previous is the newest element in the
        new list and the current one is the element dequeued from the queue.
            If they are equal, update the element at index i with 2*current element, change boolean to True, update the previous element.
            Otherwise, add the element at index (i+1) with current element and update the previous element.

            We merge when boolean is false and the current and previous one are equal.
        '''

    # constructor
    def __init__(self, row):
        self.row = row
        self.queue_row = Queue(4)
        self.result_list = [0] * 4  # later: you need to generalize with the size of the row/ column

    def create_queue(self):
        for i in self.row:
            if (i != 0):
                # print("\nAdd: ", str(self.queue_row.put(i)))
                self.queue_row.put(i)
        return self.queue_row

    def get_dequeued_element(self):
        return self.queue_row.get()

    def game_play(self):
        # initialize the index in the result list with -1, and increment by 1 while updating the index later
        index = -1

        # initialize the prev element and current element with 0
        prev = 0
        curr = 0
        added_value = 0

        # boolean is used to control merge or not
        is_merged_yet = False

        # 1. put non-zero elements into the queue
        self.create_queue()
        print("Hello!")  #

        # work with the queue until the queue is empty
        # continue the loop when there is still element in the queue and have not merged yet
        while ((not self.queue_row.empty()) and (is_merged_yet == False)):
            # update the current element with the element dequeued
            curr = self.get_dequeued_element()

            # compare the current element and the previous element
            # if not equal, update the index to index+1.
            # Otherwise, double the current value.
            # update the element at index (index) with the current element
            if (curr != prev):
                # increment the index by 1
                index = index + 1
                added_value = curr
            else:
                added_value = 2 * curr
            self.result_list[index] = added_value
            # update prev with the lastest element you do in the result (the current element)
            prev = curr

        # [2, 2, 4, 4]


if __name__ == '__main__':
    # practice get user input
    # print("Enter the list of 4 numbers!")
    # list = [] * 4
    # for i in range(4):
    #   list.append(input("Enter a number: "))

    list = [2, 0, 16, 8]
    list2 = [True, False, True]
    # game = GameMerge(list)
    # game.game_play()

    # for i in game.row:
    # print(i, end=" ")
    # while (not game.create_queue().empty()):
    #    print(game.get_dequeued_element())

    # Note: queue is not iterable like list
    # while (not queue.empty()):
    #  print(game.queue_row.get(), end="\n")
    # result_list = [0] * 4
    # result_list[1] = 4
    # for i in result_list:
    #  print(i, end=" ")
    for i in list2:
        if (not i):
            print(i)
