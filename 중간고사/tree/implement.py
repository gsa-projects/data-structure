from collections import deque
from typing import TypeVar, Generic, Callable
import operator

BinaryOperator = Callable[[float, float], float]

T = TypeVar('T')
class BTNode(Generic[T]):
    def __init__(self, data: T, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def is_leaf(self):
        return self.left is None and self.right is None

def preorder(node: BTNode):
    if node is not None:
        print(node.data, end=' ')
        preorder(node.left)
        preorder(node.right)

def inorder(node: BTNode):
    if node is not None:
        inorder(node.left)
        print(node.data, end=' ')
        inorder(node.right)

def postorder(node: BTNode):
    if node is not None:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=' ')

def levelorder(node: BTNode):
    if node is not None:
        q: deque[BTNode] = deque([node])

        while q:
            n = q.popleft()
            print(n.data, end=' ')

            if not n.is_leaf():
                q.append(n.left)
                q.append(n.right)

def count(node: BTNode) -> int:
    if node is None:
        return 0
    else:
        return count(node.left) + count(node.right) + 1

def level(node: BTNode) -> int:
    if node is None:
        return 0
    else:
        return max(level(node.left), level(node.right)) + 1

def evaluate(node: BTNode):
    if node is None:
        return 0
    elif node.is_leaf():    # 피연산자
        return node.data
    else:   # 연산자
        op = node.data
        return op(evaluate(node.left), evaluate(node.right))

def prefix_to_tree(expr: deque[str]):
    # TODO: 조금 복잡할 듯 DFS-BFS 차이처럼
    ...

def postfix_to_tree(expr: deque[str]):
    if not expr:
        return None

    tok = expr.pop()
    if tok in mapping.keys():   # 연산자
        node = BTNode(mapping[tok])
        # -1 이 연산자면 후위표기식의 경우 -2, -3이 무조건 피연산자
        # 후위표기식은 스택을 사용하는데, 함수 호출도 스택으로 이루어져서 재귀로 구현하기 쉬움
        node.right = postfix_to_tree(expr)  # 여기서 pop 한 번 더 일어남
        node.left = postfix_to_tree(expr)   # pop
        return node
    else:
        return BTNode(float(tok))

mapping = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '%': operator.mod
}

if __name__ == '__main__':
    query = input("수식: ")
    expr = query.split()

    print('수식:', expr)

    tree = postfix_to_tree(deque(expr))
    # tree = prefix_to_tree(deque(expr))

    print('전위 순회:', end=' ')
    preorder(tree)
    print()
    print('중위 순회:', end=' ')
    inorder(tree)
    print()
    print('후위 순회:', end=' ')
    postorder(tree)
    print()
    print('레벨 순회:', end=' ')
    levelorder(tree)
    print()

    print('계산 결과:', evaluate(tree))
    print('노드 수:', count(tree))
    print('트리 높이:', level(tree))
