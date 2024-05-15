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

class DNode:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

    def append(self, node):
        if node is not None:
            node.next = self.next
            node.prev = self
            # if self.next is not None:
            #     self.next.prev = node     TODO: 둘 다 됨
            if node.next is not None:
                node.next.prev = node
            self.next = node

    def pop_next(self):
        node = self.next
        if node is not None:
            self.next = node.next
            if self.next is not None:
                self.next.prev = self
        return node

