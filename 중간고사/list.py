class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link

    def append(self, node):
        if node is not None:
            node.link = self.link
            self.link = node

    def pop_next(self):
        node = self.link
        if node is not None:
            self.link = node.link
        return node

class DNode:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

    def append(self, node):
        if node is not None:
            node.next = self.next
            if self.next is not None:
                self.next.prev = node
            node.prev = self    # prev 설정 여기서 해도 됨
            self.next = node

    def pop_next(self):
        node = self.next
        if node is not None:
            self.next = node.next
            if self.next is not None:
                self.next.prev = self
        return node
