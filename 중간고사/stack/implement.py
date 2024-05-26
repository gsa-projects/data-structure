class Stack:
    capacity: int
    _array: list
    _top: int

    def __init__(self, capacity: int):
        self.capacity = capacity
        self._array = [None] * capacity
        self._top = -1

    def __repr__(self):
        return f'Stack[{self.capacity}]'

    def is_empty(self):
        return self._top == -1

    def is_full(self):
        return self._top == self.capacity - 1

    def push(self, e):
        if not self.is_full():
            self._top += 1
            self._array[self._top] = e
        else:
            raise OverflowError

    def pop(self):
        if not self.is_empty():
            self._top -= 1
            return self._array[self._top + 1]
        else:
            raise OverflowError("underflow")

    def peek(self):
        if not self.is_empty():
            return self._array[self._top]

    def size(self):
        return self._top + 1

if __name__ == "__main__":
    msg = input("문자열 입력: ")

    stack = Stack(len(msg))     # 그냥 __class_getitem__ 써보고 싶었음
    for c in msg:
        stack.push(c)

    print("문자열 출력: ", end='')
    while not stack.is_empty():
        print(stack.pop(), end='')
    print()
