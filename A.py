class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def add(node, x):
    if node is None:
        return Node(x)
    if x == node.key:
        return node
    if x < node.key:
        node.left = add(node.left, x)
    else:
        node.right = add(node.right, x)
    return node


def exists(node, x):
    while node is not None:
        if x < node.key:
            node = node.left
        elif x > node.key:
            node = node.right
        else:
            return True
    return False


def find_min(node):
    while node.left is not None:
        node = node.left
    return node


def delete(node, x):
    if node is None:
        return None
    if x < node.key:
        node.left = delete(node.left, x)
    elif x > node.key:
        node.right = delete(node.right, x)
    else:
        if node.left is None:
            return node.right
        if node.right is None:
            return node.left
        m = find_min(node.right)
        node.key = m.key
        node.right = delete(node.right, m.key)
    return node


def height(node):
    if node is None:
        return 0
    return 1 + max(height(node.left), height(node.right))


def preorder(node, out):
    if node is None:
        return
    out.append(str(node.key))
    preorder(node.left, out)
    preorder(node.right, out)


q = int(input())
node = None

for _ in range(q):
    text = input().split()
    cmd = text[0]
    if cmd == 'add':
        node = add(node, int(text[1]))
    elif cmd == 'del':
        node = delete(node, int(text[1]))
    elif cmd == 'exists':
        print('YES' if exists(node, int(text[1])) else 'NO')
    elif cmd == 'height':
        print(str(height(node)))
    elif cmd == 'print':
        if node is None:
            print('Empty')
        else:
            res = []
            preorder(node, res)
            print(' '.join(res))
