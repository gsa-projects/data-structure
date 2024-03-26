# 리스트와 집합은 원소들 사이에 순서가 없고, 중복을 허용하지 않는다는 차이점 존재 -> 집합은 선형 자료 구조라고 볼 수 없음 (순서 없어서)

class DNode:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

    def append(self, node):
        # A, B, C = self, node, self.next
        if node is not None:
            node.next = self.next   # B -> C 링크
            node.prev = self    # B -> A 링크

            if node.next is not None:   # 원래 node.next가 self.next이므로 node.next.prev는 self 였는데 이걸 node로 바꿈
                node.next.prev = node   # C -> B 링크
            self.next = node    # A -> B 링크

    def pop_next(self):
        next = self.next
        if next is not None:
            self.next = next.next
            if self.next is not None:
                self.next.prev = self

        return next

class DblLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def is_full(self):
        return False  # 무한 용량

    def get_node(self, pos: int) -> DNode | None:
        # if pos < 0:
        #     raise ValueError('pos must be non-negative')
        if pos < 0:
            return None

        ptr = self.head
        for i in range(pos):
            if ptr is None:
                # raise IndexError('index out of range')
                return None

            ptr = ptr.next

        return ptr

    def __getitem__(self, pos: int):
        node = self.get_node(pos)
        return None if node is None else node.data

    def insert(self, pos: int, value):
        node = DNode(value, None)
        before = self.get_node(pos - 1)

        if before is None:  # head 자리에 넣는 경우, head가 가리키던 걸 node가 가리키게 한 후 다시 head는 맨 앞을 가리키도록.
            node.next = self.head
            if node.next is not None:
                node.next.prev = node
            self.head = node
        else:  # 뒷 노드에 넣는 경우
            before.append(node)

    def __setitem__(self, pos: int, value):
        node = self.get_node(pos)

        if node is None:
            raise IndexError(f"{pos} index is not valid")

        node.data = value

    def pop(self, pos: int) -> DNode:
        before = self.get_node(pos - 1)

        if before is None:
            before = self.head
            if self.head is not None:
                self.head = self.head.next
            if self.head is not None:
                self.head.prev = None

            return before
        else:
            return before.pop_next()

    def __delitem__(self, pos: int):
        self.pop(pos)

    def __len__(self):
        ptr = self.head
        cnt = 0
        while ptr is not None:
            ptr = ptr.next
            cnt += 1

        return cnt

    def __str__(self):
        ptr = self.head
        ret = ''
        while ptr is not None:
            ret += f'{ptr.data} ↔ '
            ptr = ptr.next
        ret += 'None'

        return ret

if __name__ == '__main__':
    dl = DblLinkedList()
    print(dl)

    dl.insert(0, 10)
    dl.insert(0, 20)
    dl.insert(1, 30)
    dl.insert(len(dl), 40)
    dl.insert(2, 50)
    print(dl)

    dl[2] = 90
    print(dl)

    del dl[2]
    dl.pop(3)
    del dl[0]
    print(dl)
