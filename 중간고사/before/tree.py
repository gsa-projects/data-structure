class BSTNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

"""
    V
   / \
  L   R
"""

def preorder(tree):     # VLR
    if tree is not None:
        print(tree.data, end=' ')
        preorder(tree.left)
        preorder(tree.right)

def inorder(tree):      # LVR
    if tree is not None:
        inorder(tree.left)
        print(tree.data, end=' ')
        inorder(tree.right)

def postorder(tree):    # LRV
    if tree is not None:
        postorder(tree.left)
        postorder(tree.right)
        print(tree.data, end=' ')
