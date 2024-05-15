class BSTNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def preorder(tree):
    if tree is not None:
        print(tree.data)
        preorder(tree.left)
        preorder(tree.right)

def inorder(tree):
    if tree is not None:
        inorder(tree.left)
        print(tree.data)
        inorder(tree.right)

def postorder(tree):
    if tree is not None:
        postorder(tree.left)
        postorder(tree.right)
        print(tree.data)
