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

    stack = Stack(10)

    for char in expr:
        if char in mappings.values():
            stack.push(char)
        elif char in mappings.keys():
            if stack.empty():   # TODO: 틀림, 안 적음
                return False

            if mappings[char] != stack.pop():
                return False

    return stack.empty()    # TODO: 틀림, return True

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

    for char in expr:
        if char in mappings.values():
            stack.append(char)
        elif char in mappings.keys():
            if len(stack) == 0:
                return False

            if mappings[char] != stack.pop():
                return False

    return len(stack) == 0  # TODO: 틀림, len(stack) != 0

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

    from queue import LifoQueue
    stack = LifoQueue(maxsize=len(expr))

    for char in expr:
        if char in mappings.values():
            stack.put(char)
        elif char in mappings.keys():
            if stack.empty():
                return False

            if mappings[char] != stack.get():
                return False

    return stack.empty()

def check_bracket_teacher(statement):
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

    stack = Stack(100)

    for ch in statement:
        if ch in ('(', '{', '['):
            stack.push(ch)
        elif ch in (')', '}', ']'):
            if stack.empty():
                return False
            else:
                left = stack.pop()
                if (ch == ')' and left != '(') or (ch == '}' and left != '{') or (ch == ']' and left != '['):
                    return False

    return stack.empty()

def hanoi(n, start, tmp, to):
    if n == 1:
        print(f'1: {start} -> {to}')
    else:
        hanoi(n - 1, start, to, tmp)
        print(f'{n}: {start} -> {to}')
        hanoi(n - 1, tmp, start, to)

hanoi(4, 'A', 'B', 'C')
