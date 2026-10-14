class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


def add(node, x):
    if node is None:
        return Node(x)
    if x == node.key:
        return node
    if x < node.key:
        node.left = add(node.left, x)
    else:
        node.right = add(node.right, x)

    update_height(node)
    bal = height(node.right) - height(node.left)

    if bal == 2:
        right_kid = node.right
        if height(right_kid.right) - height(right_kid.left) >= 0:
            return turn_left(node)
        else:
            node.right = turn_right(right_kid)
            return turn_left(node)

    if bal == -2:
        left_kid = node.left
        if height(left_kid.right) - height(left_kid.left) <= 0:
            return turn_right(node)
        else:
            node.left = turn_left(left_kid)
            return turn_right(node)
            
    return node


def turn_left(node):
    right_kid = node.right
    node.right = right_kid.left
    right_kid.left = node
    update_height(node)
    update_height(right_kid)
    return right_kid


def turn_right(node):
    left_kid = node.left
    node.left = left_kid.right
    left_kid.right = node
    update_height(node)
    update_height(left_kid)
    return left_kid


def exists(node, x):
    while node is not None:
        if x < node.key:
            node = node.left
        elif x > node.key:
            node = node.right
        else:
            return True
    return False


def height(node):
    return node.height if node is not None else 0


def update_height(node):
    node.height = 1 + max(height(node.left), height(node.right))


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
    elif cmd == 'exists':
        print('YES' if exists(node, int(text[1])) else 'NO')
    elif cmd == 'root':
        print('Empty' if node is None else node.key)
    elif cmd == 'height':
        print(height(node))
    elif cmd == 'print':
        if node is None:
            print('Empty')
        else:
            res = []
            preorder(node, res)
            print(' '.join(res))