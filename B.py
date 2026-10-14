class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def tree(node, x):
    if node is None:
        return Node(x)
    if x == node.key:
        return node
    if x < node.key:
        node.left = tree(node.left, x)
    else:
        node.right = tree(node.right, x)
    return node


def turn_left(node, x):
    if node is None:
        return None
    if x < node.key:
        node.left = turn_left(node.left, x)
    elif x > node.key:
        node.right = turn_left(node.right, x)
    else:
        right_kid = node.right
        node.right = right_kid.left
        right_kid.left = node
        return right_kid
    return node


def turn_right(node, x):
    if node is None:
        return None
    if x < node.key:
        node.left = turn_right(node.left, x)
    elif x > node.key:
        node.right = turn_right(node.right, x)
    else:
        left_kid = node.left
        node.left = left_kid.right
        left_kid.right = node
        return left_kid
    return node


def preorder(node, out):
    if node is None:
        return
    out.append(str(node.key))
    preorder(node.left, out)
    preorder(node.right, out)


n = int(input())
nums = [int(i) for i in input().split()]
m = int(input())
node = None

for i in nums:
    node = tree(node, i)

for _ in range(m):
    text = input().split()
    cmd = text[0]
    x = int(text[1])
    if cmd == 'left':
        node = turn_left(node, x)
    elif cmd == 'right':
        node = turn_right(node, x)

    res = []
    preorder(node, res)
    print(' '.join(res))