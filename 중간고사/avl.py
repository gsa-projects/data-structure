class BSTNode:
    def __init__(self, key, value, height=0, left=None, right=None):
        self.key = key
        self.value = value
        self.height = height
        self.left = left
        self.right = right


def height(root: BSTNode | None) -> int:
    return 0 if root is None else root.height


def bf(root: BSTNode) -> int:
    return height(root.left) - height(root.right)


def rotate_right(n: BSTNode) -> BSTNode:
    x = n.left
    n.left = x.right
    x.right = n

    x.height = max(height(x.left), height(x.right)) + 1
    n.height = max(height(n.left), height(n.right)) + 1

    return x


def rotate_left(n: BSTNode) -> BSTNode:
    x = n.right
    n.right = x.left
    x.left = n

    x.height = max(height(x.left), height(x.right)) + 1
    n.height = max(height(n.left), height(n.right)) + 1

    return x


def balance(root: BSTNode) -> BSTNode:
    if bf(root) > 1:
        if bf(root.left) < 0:
            root.left = rotate_left(root.left)
        root = rotate_right(root)
    elif bf(root) < -1:
        if bf(root.right) > 0:
            root.right = rotate_right(root.right)
        root = rotate_left(root)

    return root


def search(root: BSTNode, key) -> BSTNode | None:
    if root is None:
        return None

    if key < root.key:
        return search(root.left, key)
    elif key > root.key:
        return search(root.right, key)
    else:
        return root


def search_value(root: BSTNode, value) -> BSTNode | None:
    if root is None:
        return None
    if root.value == value:
        return root

    searched = search_value(root.left, value)
    if searched is None:
        searched = search_value(root.right, value)

    return searched


def insert(root: BSTNode, node: BSTNode) -> BSTNode | None:
    if root is None:
        node.height = 1
        return node

    if root.key == node.key:
        return root  # TODO: node 라고 써서 틀림. 트리에 영향을 안 주려면 트리 그 자체를 반환해야지.
    elif root.key < node.key:
        root.right = insert(root.right, node)
    else:
        root.left = insert(root.left, node)

    root.height = max(height(root.left), height(root.right)) + 1  # TODO: 아예 빼먹음. 삽입과 삭제 후에는 높이가 달라지니 재갱신이 필요함.
    return balance(root)


def delete(root: BSTNode, key) -> BSTNode | None:
    if root is None:
        return None

    if key < root.key:
        root.left = delete(root.left, key)
    elif key > root.key:
        root.right = delete(root.right, key)
    else:
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left

        succ = root.right
        while succ.left is not None:
            succ = succ.left

        root.key = succ.key
        root.value = succ.value
        root.right = delete(root.right, succ.key)

    root.height = max(height(root.left), height(root.right)) + 1  # TODO: 까먹음
    return balance(root)


def print_tree(msg: str, root: BSTNode):
    def _display_aux(root: BSTNode, use_key_only=True) -> tuple[list[str], int, int, int]:
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

    print(msg)
    lines, *_ = _display_aux(root)
    for line in lines:
        print(line)


if __name__ == "__main__":
    data = [
        BSTNode(75, "apple"),
        BSTNode(80, "grape"),
        BSTNode(85, "lime"),
        BSTNode(20, "mango"),
        BSTNode(10, "strawberry"),
        BSTNode(50, "banana"),
        BSTNode(30, "cherry"),
        BSTNode(40, "watermelon"),
        BSTNode(70, "melon"),
        BSTNode(90, "plum")
    ]

    tree = None
    for d in data:
        tree = insert(tree, d)
        print_tree(f"added {d.key}", tree)

    tree = delete(tree, 75)
    print_tree("delete 75", tree)

    tree = delete(tree, 85)
    print_tree("delete 85", tree)

    tree = delete(tree, 20)
    print_tree("delete 20", tree)
