# 덱(원형 덱)은 큐(원형 큐)와 매유 유사하므로 상속으로 구현.
# 다른 점은 덱은 양방향 삽입/삭제를 해야 하니 반시계 회전도 구현해야 함.

from implement_queue import ArrayQueue

class CircularDeque(ArrayQueue):
    def __init__(self, capacity=10):
        super().__init__(capacity)

    def push_front(self, item):
        if not self.is_full():
            self.data[self.front] = item
            self.front = (self.front - 1) % self.capacity

    def push_back(self, item):  # 동일
        self.enqueue(item)

    def remove_front(self):     # 동일
        return self.dequeue()

    def remove_back(self):
        if not self.is_empty():
            v = self.data[self.rear]
            self.rear = (self.rear - 1) % self.capacity
            return v

    def peek_front(self):       # 동일
        return self.peek()

    def peek_back(self):
        if not self.is_empty():
            return self.data[self.rear]

if __name__ == "__main__":
    dq = CircularDeque()

    for i in range(9):
        if i % 2 == 0:
            dq.push_back(i)
        else:
            dq.push_front(i)
    dq.print('홀수는 전단, 짝수는 후단 삽입')

    for i in range(2):
        dq.remove_front()
    dq.print('전단 삭제 2번')

    for i in range(3):
        dq.remove_back()
    dq.print('후단 삭제 3번')

    for i in range(9, 14):
        dq.push_front(i)
    dq.print('전단에 9-13 삽입')
