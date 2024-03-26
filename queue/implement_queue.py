# 원형 큐

class ArrayQueue:
    # front는 첫 요소 전의 인덱스를 가리키고, rear는 마지막 요소의 인덱스를 가리킴
    def __init__(self, capacity=10):
        self.data = [None] * capacity
        self.capacity = capacity
        self.front = 0
        self.rear = 0

    def is_empty(self):
        return self.front == self.rear

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    # 원형 큐에서 enqueue를 할 때 rear가 1부터 삽입되므로 -> 원형 큐는 capacity - 1 개의 요소를 넣을 수 있다.
    def enqueue(self, item):
        if not self.is_full():
            self.rear = (self.rear + 1) % self.capacity
            self.data[self.rear] = item

    def force_enqueue(self, item):  # 원형 큐를 링 버퍼로 활용
        self.rear = (self.rear + 1) % self.capacity     # 일단 삽입
        self.data[self.rear] = item

        if self.is_empty():     # is front == rear ?
            # rear를 밀었을 때 front와 같아지면 front도 밀어줘서 계속 full 상태를 유지시킴 (front, rear가 평행이동 한 셈)
            self.front = (self.front + 1) % self.capacity

    def dequeue(self):
        if not self.is_empty():
            self.front = (self.front + 1) % self.capacity
            return self.data[self.front]

    def peek(self):
        if not self.is_empty():
            return self.data[(self.front + 1) % self.capacity]

    def size(self):
        return (self.rear - self.front + self.capacity) % self.capacity

    def print(self, msg):
        print(msg, end=': [')
        for i in range(self.front + 1, self.front + 1 + self.size()):  # range(self.front + 1, self.rear + 1) 하면 self.rear < self.front 인 경우 작동 x
            print(self.data[i % self.capacity], end=' ')
        print(']')

# 내가 만든 것의 개선안:
# 1. capacity 입력한 것과 용량(요소 최대 개수)이 실제로 일치함
# 2. 프로그래밍 철학인 [a, b) 구간 철학을 유지. front는 첫 요소를 가리키고, rear는 끝 요소 다음 인덱스를 가리킴.
class ArrayQueue2:
    def __init__(self, capacity=10):
        self.capacity = capacity + 1
        self.data = [None] * self.capacity
        self.front = 0
        self.rear = 0

    def is_empty(self):
        return self.front == self.rear

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    # 원형 큐에서 enqueue를 할 때 rear가 1부터 삽입되므로 -> 원형 큐는 capacity - 1 개의 요소를 넣을 수 있다.
    def enqueue(self, item):
        if not self.is_full():
            self.data[self.rear] = item
            self.rear = (self.rear + 1) % self.capacity

    def dequeue(self):
        if not self.is_empty():
            v = self.data[self.front]
            self.front = (self.front + 1) % self.capacity
            return v

    def peek(self):
        if not self.is_empty():
            return self.data[self.front]

    def size(self):
        return (self.rear - self.front + self.capacity) % self.capacity

if __name__ == "__main__":
    import random

    q = ArrayQueue(8)   # 7개 넣을 수 있음

    while not q.is_full():
        v = random.randint(0, 100)
        print(f'enqueue {v}')
        q.enqueue(v)

    print('---------')

    while not q.is_empty():
        print(q.dequeue(), end=' ')
