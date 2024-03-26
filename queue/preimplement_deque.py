import random
from collections import deque

if __name__ == "__main__":
    dq = deque()    # maxsize=inf

    print('덱은 공백 상태 아님' if dq else '덱은 공백 상태')

    for i in range(9):
        if i % 2 == 0:
            dq.append(i)    # push_back -> append
        else:
            dq.appendleft(i)    # push_front -> appendleft
    print('홀수는 전단, 짝수는 후단 삽입\t', dq)

    for i in range(2):
        dq.popleft()    # remove_front -> popleft
    print('전단 삭제 2번\t\t\t', dq)

    for i in range(3):
        dq.pop()
    print('후단 삭제 3번\t\t\t', dq)

    for i in range(9, 14):
        dq.appendleft(i)    # push_back -> append
    print('전단에 9-13 삽입\t\t', dq)
