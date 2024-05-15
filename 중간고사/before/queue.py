class Queue:
    def __init__(self, capacity=10):
        self.data = [None] * capacity
        self.capacity = capacity
        self.front = 0
        self.rear = 0

    def empty(self):
        return self.front == self.rear

    def full(self):
        return self.front == (self.rear + 1) % self.capacity

    def size(self):
        return (self.rear - self.front) % self.capacity

    def enqueue(self, e):
        if not self.full():
            self.rear = (self.rear + 1) % self.capacity
            self.data[self.rear] = e

    def dequeue(self):
        if not self.empty():
            self.front = (self.front + 1) % self.capacity
            return self.data[self.front]

    def peek(self):
        if not self.empty():
            return self.data[(self.front + 1) % self.capacity]      # TODO: 틀림

class Deque(Queue):
    def __init__(self, capacity=10):
        super().__init__(capacity)

    def push_front(self, e):
        if not self.full():
            self.data[self.front] = e
            self.front = (self.front - 1) % self.capacity

    def push_rear(self, e):
        self.enqueue(e)

    def delete_front(self):
        return self.dequeue()

    def delete_rear(self):
        if not self.empty():
            item = self.data[self.rear]
            self.rear = (self.rear - 1) % self.capacity
            # return self.data[self.rear + 1]   # TODO: 틀림
            return item

    def get_front(self):
        return self.peek()

    def get_rear(self):
        if not self.empty():    # TODO: 이 조건문 안 씀
            return self.data[self.rear]

    def __str__(self):
        ret = '['
        for i in range(self.front + 1, self.front + 1 + self.size()):
            ret += f'{self.data[i % self.capacity]} '
        return ret[:-1] + ']'

if __name__ == '__main__':
    # import random
    #
    # q = Queue(8)
    #
    # while not q.full():
    #     v = random.randint(0, 100)
    #     print(f'enqueue {v}')
    #     q.enqueue(v)
    #
    # print('---------')
    #
    # while not q.empty():
    #     print(q.dequeue(), end=' ')

    dq = Deque()

    for i in range(9):
        if i % 2 == 0:
            dq.push_rear(i)
        else:
            dq.push_front(i)
    print(dq)

    for i in range(2):
        dq.delete_front()
    print(dq)

    for i in range(3):
        dq.delete_rear()
    print(dq)

    for i in range(9, 14):
        dq.push_front(i)
    print(dq)
