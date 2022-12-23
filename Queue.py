from queue import Queue

q = Queue(maxsize=4)
q.put('a')
q.put('b')

if __name__ == '__main__':
    print(q.qsize())  # qsize() is to return the number of elements in the queue
    print("\nFull: ", q.full())

    # Remove elements from the queue
    print("Elements dequeued from the queue: ")
    while (not q.empty()):
        print(q.get(), end=" ")
