class BSTNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left: BSTNode | None = None
        self.right: BSTNode | None = None

    def __str__(self):
        return f"{self.key}:{self.value}"

    def __len__(self):
        return int(self.left is not None) + int(self.right is not None)

def search_bst(root: BSTNode, key) -> BSTNode | None:
    if root is None:
        return None
    elif key < root.key:  # 왼쪽 서브 트리로 가기
        return search_bst(root.left, key)
    elif key > root.key:  # 오른쪽 서브 트리로 가기
        return search_bst(root.right, key)
    else:
        return root

def search_value_bst(root: BSTNode, value) -> BSTNode | None:
    if root is None:
        return None
    elif value == root.value:
        return root

    res = search_value_bst(root.left, value)
    if res is not None:
        return res
    else:
        return search_value_bst(root.right, value)

def insert_bst(root: BSTNode, node: BSTNode) -> BSTNode | None:
    if root is None:  # 삽입 위치까지 도달한 경우
        return node
    elif node.key < root.key:
        root.left = insert_bst(root.left, node)
    elif node.key > root.key:
        root.right = insert_bst(root.right, node)
    else:  # 동일한 키는 허용하지 않아 변화 없음
        return root

    return root

def insert_bst_(root: BSTNode, key, value=None) -> BSTNode | None:
    if root is None:  # 삽입 위치까지 도달한 경우
        return BSTNode(key, value)
    elif key < root.key:
        root.left = insert_bst_(root.left, key)
    elif key > root.key:
        root.right = insert_bst_(root.right, key)
    else:  # 동일한 키는 허용하지 않아 변화 없음
        return root

    return root

def delete_bst(root: BSTNode, key, use_succ_to_right=True) -> BSTNode | None:
    if root is None:
        return None
    elif key < root.key:
        root.left = delete_bst(root.left, key, use_succ_to_right)
    elif key > root.key:
        root.right = delete_bst(root.right, key, use_succ_to_right)
    else:
        # case 1: 단말 노드의 삭제
        # case 2: 자식이 하나인 노드의 삭제
        # case 3: 자식이 2개인 노드의 삭제

        # match len(root):
        #     case 0:
        #         return None
        #     case 1:
        #         return root.left if root.left else root.right
        #     case 2:
        #         if use_succ_to_right:   # 후계자는 오른쪽 서브 트리의 최소 키로 정함
        #             # 후계자 찾기
        #             succ = root.right
        #             while succ.left is not None:
        #                 succ = succ.left
        #
        #             # 데이터 복사
        #             root.key = succ.key
        #             root.value = succ.value
        #
        #             # 후계자 삭제
        #             root.right = delete_bst(root.right, root.key, use_succ_to_right)   # 당연히 succ.key도 됨
        #         else:   # 후계자는 왼쪽 서브 트리의 최대 키로 정함
        #             # 후계자 찾기
        #             succ = root.left
        #             while succ.right is not None:
        #                 succ = succ.right
        #
        #             # 데이터 복사
        #             root.key = succ.key
        #             root.value = succ.value
        #
        #             # 후계자 삭제
        #             root.left = delete_bst(root.left, root.key, use_succ_to_right)

        # case 1과 2를 한 번에
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        # case 3
        if use_succ_to_right:
            succ = root.right
            while succ.left is not None:
                succ = succ.left

            root.key = succ.key
            root.value = succ.value
            root.right = delete_bst(root.right, succ.key, use_succ_to_right)
        else:
            succ = root.left
            while succ.right is not None:
                succ = succ.right

            root.key = succ.key
            root.value = succ.value
            root.left = delete_bst(root.left, succ.key, use_succ_to_right)

    return root

def _display_aux(root: BSTNode, use_key_only) -> tuple[list[str], int, int, int]:
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

def print_tree(msg: str, root: BSTNode, use_key_only=True):
    print(msg)
    lines, *_ = _display_aux(root, use_key_only)
    for line in lines:
        print(line)

if __name__ == "__main__":
    # data_list = [(6, "여섯"), (8, "여덟"), (2, "둘"), (4, "넷"), (7, "일곱"),
    #              (5, "다섯"), (1, "하나"), (9, "아홉"), (3, "셋"), (0, "영")]
    #
    # tree = None
    # for data in data_list:
    #     tree = insert_bst(tree, BSTNode(data[0], data[1]))
    #
    # print_tree("최초 트리:", tree)
    # print()
    #
    # print("search 3:", search_bst(tree, 3))
    # print("search 8:", search_bst(tree, 8))
    # print("search 0:", search_bst(tree, 0))
    # print("search 10:", search_bst(tree, 10))
    # print("search 둘:", search_value_bst(tree, '둘'))
    # print("search 열:", search_value_bst(tree, '열'))
    # print()
    #
    # use_succ_to_right = False
    #
    # tree = delete_bst(tree, 7, use_succ_to_right)
    # print_tree("delete 7:", tree)
    # print()
    #
    # tree = delete_bst(tree, 8, use_succ_to_right)
    # print_tree("delete 8:", tree)
    # print()
    #
    # tree = delete_bst(tree, 2, use_succ_to_right)
    # print_tree("delete 2:", tree)
    # print()
    #
    # tree = delete_bst(tree, 6, use_succ_to_right)
    # print_tree("delete 6:", tree)

    # avl과 비교하는 테스트
    tree = None
    tree = insert_bst(tree, BSTNode(75, "apple"))
    tree = insert_bst(tree, BSTNode(80, "grape"))
    tree = insert_bst(tree, BSTNode(85, "lime"))
    tree = insert_bst(tree, BSTNode(20, "mango"))
    tree = insert_bst(tree, BSTNode(10, "strawberry"))
    tree = insert_bst(tree, BSTNode(50, "banana"))
    tree = insert_bst(tree, BSTNode(30, "cherry"))
    tree = insert_bst(tree, BSTNode(40, "watermelon"))
    tree = insert_bst(tree, BSTNode(70, "melon"))
    tree = insert_bst(tree, BSTNode(90, "plum"))
    print_tree('', tree)

    delete_bst(tree, 75)
    delete_bst(tree, 85)
    print_tree("75와 85 삭제", tree)
