from implement import Stack
from queue import LifoQueue

def check_bracket(statement):
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

    stack = Stack(len(statement))
    mapping = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for ch in statement:
        if ch in ('(', '{', '['):
            stack.push(ch)
        elif ch in (')', '}', ']'):
            if stack.is_empty():
                return False
            else:
                p = stack.pop()
                if mapping[ch] != p:
                    return False

    return stack.is_empty()

def check_bracket_python(statement):
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
    mapping = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for ch in statement:
        if ch in ('(', '{', '['):
            stack.append(ch)
        elif ch in (')', '}', ']'):
            if len(stack) == 0:
                return False
            else:
                p = stack.pop()
                if mapping[ch] != p:
                    return False

    return len(stack) == 0

def check_bracket_lifo(statement):
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

    stack = LifoQueue(maxsize=len(statement))
    mapping = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for ch in statement:
        if ch in ('(', '{', '['):
            stack.put(ch)
        elif ch in (')', '}', ']'):
            if stack.empty():
                return False
            else:
                p = stack.get()
                if mapping[ch] != p:
                    return False

    return stack.empty()
