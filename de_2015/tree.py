class tree:
    def __init__(root, maso, toy_name):
        root.left = None
        root.right = None
        root.maso = int(maso)
        root.name = toy_name

def add(root, new):
    if root is None:
        root = new
    elif root.maso < new.maso:
        root.right = add(root.right, new)
    elif root.maso > new.maso:
        root.left = add(root.left, new)
    return root

def search(root, maso):
    if root is None:
        return None
    elif root.maso > maso:
        return search(root.right, maso)
    elif root.maso < maso:
        return search(root.left, maso)
    else:
        return root

def traversal(root):
    if root is not None:
        traversal(root.left)
        print(root.maso, root.name)
        traversal(root.right)

def LeftMost(root):
    while root.left is not None:
        root = root.left
    return root

def delete(root, maso):
    if root is None:
        return root
    if root.maso < maso:
        root.left = delete(root.left, maso)
    elif root.maso > maso:
        root.right = delete(root.right, maso)
    else:
        if root.left is None:
            new = root.right
            root = None
            return new
        if root.right is None:
            new = root.left
            root = None
            return new

        new = LeftMost(root.right)
        root.maso = new.maso
        root.name = new.name
        root.right = delete(root.right, new.maso)
    return root

def read_A(f):
    root = None
    new = None

    for x in f: 
        x = x.split(" ")
        x[-1] = x[-1].strip()
        if len(x) == 1:
            print("Thieu thong tin:",x[0])
            print("Nhap ten do choi cua", x[0])
            a = input()
            x.append(a)
        new = tree(x[0], x[1])
        root = add(root, new)
    return root

def read_B(f):
    root = None
    new = None

    for x in f: 
        x = x.split(" ")
        x[-1] = x[-1].strip()
            
        new = tree(x[0], x[1])
        root = add(root, new)
    return root

#f = open("A.txt","r")
#root = read_A(f)
#traversal(root)


