class BSTNode:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

def delete(root, key):
    if root is None:
        return None

    if key < root.key:
        root.left = delete(root.left, key)
    elif key > root.key:
        root.right = delete(root.right, key)
    else:
        if root.left is None:   # TODO: is not None 이라고 해서 틀림
            return root.right
        if root.right is None:
            return root.left

        succ = root.right
        while succ.left is not None:
            succ = succ.left

        root.key = succ.key
        root.right = delete(root.right, root.key)

    return root

if __name__ == '__main__':
    ...