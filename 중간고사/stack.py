from queue import LifoQueue
import pytest

class Stack:
    def __init__(self, capacity):
        self.data = [None] * capacity
        self.top = -1
        self.capacity = capacity

    def empty(self):
        return self.top == -1

    def full(self):
        return self.top == self.capacity - 1

    def push(self, e):
        if not self.full():
            self.top += 1
            self.data[self.top] = e
        else:
            print("stack overflow")
            exit()

    def pop(self):
        if not self.empty():
            self.top -= 1
            return self.data[self.top + 1]
        else:
            print("stack underflow")
            exit()

    def peek(self):
        if not self.empty():
            return self.data[self.top]
        else:
            pass

    def size(self):
        return self.top + 1

mappings = {')': '(', '}': '{', ']': '['}

def check_bracket(expr):
    """
    >>> check_bracket('{ A[(i+1)]=0; }')
    True
    >>> check_bracket("if ((x<0) && (y<3)")
    False
    >>> check_bracket("while (n<8)) {n++;}")
    False
    >>> check_bracket("arr[(i+1])=0;")
    False
    """

    stack = Stack(len(expr))

    for ch in expr:
        if ch in ('(', '[', '{'):
            stack.push(ch)
        elif ch in (')', ']', '}'):
            if stack.empty():
                return False
            else:
                p = stack.pop()
                if not ((p == '(' and ch == ')') or (p == '[' and ch == ']') or (p == '{' and ch == '}')):
                    return False

    return stack.empty()

def check_bracket_python(expr):
    """
    >>> check_bracket_python('{ A[(i+1)]=0; }')
    True
    >>> check_bracket_python("if ((x<0) && (y<3)")
    False
    >>> check_bracket_python("while (n<8)) {n++;}")
    False
    >>> check_bracket_python("arr[(i+1])=0;")
    False
    """

    stack = []

    for ch in expr:
        if ch in ('(', '[', '{'):
            stack.append(ch)    # TODO: push 아니고 append
        elif ch in (')', ']', '}'):
            if not stack:
                return False
            else:
                v = stack.pop()
                if not ((v == '(' and ch == ')') or (v == '[' and ch == ']') or (v == '{' and ch == '}')):
                    return False

    return not stack

def check_bracket_lifo(expr):
    """
    >>> check_bracket_lifo('{ A[(i+1)]=0; }')
    True
    >>> check_bracket_lifo("if ((x<0) && (y<3)")
    False
    >>> check_bracket_lifo("while (n<8)) {n++;}")
    False
    >>> check_bracket_lifo("arr[(i+1])=0;")
    False
    """

    stack = LifoQueue(maxsize=len(expr))

    for ch in expr:
        if ch in ('(', '[', '{'):
            stack.put(ch)
        elif ch in (')', ']', '}'):
            if stack.empty():
                return False
            else:
                v = stack.get()
                if (v == '(' and ch != ')') or (v == '[' and ch != ']') or (v == '{' and ch != '}'):
                    return False

    return stack.empty()

def hanoi(n, start, tmp, to):
    if n == 1:
        print(f'1: {start} -> {to}')
    else:
        hanoi(n - 1, start, to, tmp)
        print(f'{n}: {start} -> {to}')
        hanoi(n - 1, tmp, start, to)

# hanoi(4, 'A', 'B', 'C')
