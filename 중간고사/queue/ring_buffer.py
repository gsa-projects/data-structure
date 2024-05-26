from implement_queue import ArrayQueue

if __name__ == "__main__":
    q = ArrayQueue(8)

    for i in range(6):
        q.force_enqueue(i)
    q.print('삽입 0-5')

    # capacity 넘어서면 front와 rear가 +1로 평행 이동하기 때문에 앞(front)에서부터 데이터가 잘림
    q.force_enqueue(6)
    q.force_enqueue(7)
    q.print('삽입 6, 7')

    q.force_enqueue(8)
    q.force_enqueue(9)
    q.print('삽입 8, 9')

    q.dequeue()
    q.dequeue()
    q.print('삭제 2번')
