class Node:
    def __init__(self, key, value, height, left=None, right=None):
        self.key = key
        self.value = value
        self.height = height
        self.left = left
        self.right = right

    def __str__(self):
        return str((self.key, self.value))

def _display_aux(root: Node, use_key_only=True) -> tuple[list[str], int, int, int]:
    """
    :return: list of strings, width, height, and horizontal coordinate
    """

    # 단말 노드일 때
    if root.right is None and root.left is None:
        line = str(root.key) if use_key_only else str(root)
        width = len(line)
        height = 1
        middle = width // 2

        return [line], width, height, middle

    # left만 있을 때
    if root.right is None:
        lines, n, p, x = _display_aux(root.left, use_key_only)

        s = str(root.key) if use_key_only else str(root)
        u = len(s)

        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
        second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
        shifted_lines = [line + u * ' ' for line in lines]

        return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

    # right만 있을 때
    if root.left is None:
        lines, n, p, x = _display_aux(root.right, use_key_only)

        s = str(root.key) if use_key_only else str(root)
        u = len(s)

        first_line = s + x * '_' + (n - x) * ' '
        second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
        shifted_lines = [u * ' ' + line for line in lines]

        return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

    # left, right 둘 다 존재할 때
    left, n, p, x = _display_aux(root.left, use_key_only)
    right, m, q, y = _display_aux(root.right, use_key_only)

    s = str(root.key) if use_key_only else str(root)
    u = len(s)

    first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
    second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '

    if p < q:
        left += [n * ' '] * (q - p)
    elif q < p:
        right += [m * ' '] * (p - q)

    zipped_lines = zip(left, right)
    lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]

    return lines, n + m + u, max(p, q) + 2, n + u // 2

class AVL:
    def __init__(self):
        self.root = None

    def height(self, n):
        if n is None:
            return 0
        return n.height

    def insert(self, key, value):
        self.root = self.insert_item(self.root, key, value)

    def insert_item(self, n, key, value):
        # BST의 삽입 연산과 똑같음
        if n is None:
            return Node(key, value, 1)

        if key < n.key:
            n.left = self.insert_item(n.left, key, value)
        elif key > n.key:
            n.right = self.insert_item(n.right, key, value)
        else:
            n.value = value
            return n

        n.height = max(self.height(n.left), self.height(n.right)) + 1
        return self.balance(n)

    def delete(self, key):
        self.root = self.delete_item(self.root, key)

    def delete_item(self, n, key):
        if n is None:
            return None

        if key < n.key:
            n.left = self.delete_item(n.left, key)
        elif key > n.key:
            n.right = self.delete_item(n.right, key)
        else:
            if n.right is None:
                return n.left
            if n.left is None:
                return n.right

            target = n
            n = self.min(target.right)  # 우측 서브 트리의 최솟값. 즉 오른쪽 후계자
            n.right = self.delete_min(target.right)
            n.left = target.left

        n.height = max(self.height(n.left), self.height(n.right)) + 1
        return self.balance(n)

    def delete_min(self, n):    # 최솟값 삭제
        if n.left is None:
            return n.right
        n.left = self.delete_min(n.left)
        n.height = max(self.height(n.left), self.height(n.right)) + 1

        return self.balance(n)

    def min_item(self, n):
        if n.left is None:
            return n
        return self.min_item(n.left)

    def balance(self, n):
        if self.bf(n) > 1:  # left > right
            if self.bf(n.left) < 0:
                n.left = self.rotate_left(n.left)       # LR
            n = self.rotate_right(n)    # LL
        elif self.bf(n) < -1:   # left < right
            if self.bf(n.right) > 0:
                n.right = self.rotate_right(n.right)    # RL
            n = self.rotate_left(n)     # RR

        return n

    def bf(self, n):
        return self.height(n.left) - self.height(n.right)

    def rotate_right(self, n):
        x = n.left
        n.left = x.right
        x.right = n

        n.height = max(self.height(n.left), self.height(n.right)) + 1
        x.height = max(self.height(x.left), self.height(x.right)) + 1

        return x

    def rotate_left(self, n):
        x = n.right
        n.right = x.left
        x.left = n

        n.height = max(self.height(n.left), self.height(n.right)) + 1
        x.height = max(self.height(x.left), self.height(x.right)) + 1

        return x

    def min(self, n):
        if n is None:
            return None
        return self.min_item(n)

    def __str__(self):
        lines, *_ = _display_aux(self.root)
        return '\n'.join(lines)

if __name__ == "__main__":
    avl = AVL()

    avl.insert(75, "apple")
    print(avl)
    avl.insert(80, "grape")
    print(avl)
    avl.insert(85, "lime")
    print(avl)
    avl.insert(20, "mango")
    print(avl)
    avl.insert(10, "strawberry")
    print(avl)
    avl.insert(50, "banana")
    print(avl)
    avl.insert(30, "cherry")
    print(avl)
    avl.insert(40, "watermelon")
    print(avl)
    avl.insert(70, "melon")
    print(avl)
    avl.insert(90, "plum")
    print(avl)
    print()

    avl.delete(75)
    avl.delete(85)
    print("75와 85 삭제\n", avl)
    print()
