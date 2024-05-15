class BSTNode:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return BSTNode(key, key)

    if root.key == key:
        return root
    elif root.key < key:
        # return insert(root.right, key)    # TODO: 틀림
        root.right = insert(root.right, key)
    else:
        # return insert(root.left, key)     # TODO: 틀림
        root.left = insert(root.left, key)

    return root

def delete(root, key):
    if root is None:
        return None

    if root.key < key:
        root.right = delete(root.right, key)
    elif root.key > key:
        root.left = delete(root.left, key)
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

    return root

if __name__ == '__main__':
    ...