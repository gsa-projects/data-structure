# 리스트와 집합은 원소들 사이에 순서가 없고, 중복을 허용하지 않는다는 차이점 존재 -> 집합은 선형 자료 구조라고 볼 수 없음 (순서 없어서)

class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link

    def append(self, node):
        if node is not None:
            node.link = self.link
            self.link = node

    def pop_next(self):
        next = self.link
        if next is not None:
            self.link = next.link

        return next

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def is_full(self):
        return False  # 무한 용량

    def get_node(self, pos: int) -> Node | None:
        # if pos < 0:
        #     raise ValueError('pos must be non-negative')
        if pos < 0:
            return None

        ptr = self.head
        for i in range(pos):
            if ptr is None:
                # raise IndexError('index out of range')
                return None

            ptr = ptr.link

        return ptr

    def __getitem__(self, pos: int):
        node = self.get_node(pos)
        return None if node is None else node.data

    def insert(self, pos: int, value):
        node = Node(value, None)
        before = self.get_node(pos - 1)

        if before is None:  # head 자리에 넣는 경우, head가 가리키던 걸 node가 가리키게 한 후 다시 head는 맨 앞을 가리키도록.
            node.link = self.head
            self.head = node
        else:  # 뒷 노드에 넣는 경우
            before.append(node)

    def __setitem__(self, pos: int, value):
        node = self.get_node(pos)

        if node is None:
            raise IndexError(f"{pos} index is not valid")

        node.data = value

    def pop(self, pos: int) -> Node:
        before = self.get_node(pos - 1)

        if before is None:
            before = self.head
            if self.head is not None:
                self.head = self.head.link

            return before
        else:
            return before.pop_next()

    def __delitem__(self, pos: int):
        self.pop(pos)

    def __len__(self):
        ptr = self.head
        cnt = 0
        while ptr is not None:
            ptr = ptr.link
            cnt += 1

        return cnt

    def __str__(self):
        ptr = self.head
        ret = ''
        while ptr is not None:
            ret += f'{ptr.data} → '
            ptr = ptr.link
        ret += 'None'

        return ret

if __name__ == '__main__':
    l = LinkedList()
    print(l)

    l.insert(0, 10)
    l.insert(0, 20)
    l.insert(1, 30)
    l.insert(len(l), 40)
    l.insert(2, 50)
    print(l)

    l[2] = 90
    print(l)

    del l[2]
    l.pop(3)
    del l[0]
    print(l)
