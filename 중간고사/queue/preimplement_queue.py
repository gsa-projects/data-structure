import random
from queue import Queue

if __name__ == "__main__":
    q = Queue(maxsize=8)

    print('삽입 순서: ', end='')
    while not q.full():     # is_full -> full
        v = random.randint(0, 100)
        q.put(v)    # enqueue -> put
        print(v, end=' ')
    print()

    print('삭제 순서: ', end='')
    while not q.empty():    # is_empty -> empty
        print(q.get(), end=' ')     # dequeue -> get
    print()

    print('Queue is FIFO')
