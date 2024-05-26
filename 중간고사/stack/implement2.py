capacity = 10
array = [None] * capacity
top = -1

def is_empty():
    return top == -1

def is_full():
    return top == capacity - 1

def push(e):
    global top

    if not is_full():
        top += 1
        array[top] = e
    else:
        raise OverflowError

def pop():
    global top

    if not is_empty():
        top -= 1
        return array[top + 1]
    else:
        raise OverflowError("underflow")

def peek():
    if not is_empty():
        return array[top]

def size():
    return top + 1

if __name__ == "__main__":
    msg = input("문자열 입력: ")  # 문자열을 입력받음
    for c in msg:  # 문자열의 각 문자 c에 대해
        push(c)  # c를 스택에 삽입

    print("문자열 출력: ", end='')
    while not is_empty():  # 스택이 공백상태가 아니라면
        print(pop(), end='')  # 하나의 요소를 꺼내서 출력
    print()
