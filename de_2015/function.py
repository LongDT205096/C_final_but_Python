import tree

def func_3(root_A, root_B, list):
    if root_A is not None:
        func_3(root_A.left, root_B, list)
        if root_A.maso in root_B.keys():
            list.append(root_A.maso)
        func_3(root_A.right, root_B, list)

def func_4(root_A, root_B):
    for x, y in root_B.items():
        new = tree.tree(x, y)
        root_A = tree.add(root_A, new)
    return root_A

def func_5(root, root_A):
    pass

def menu():
    print("\n1. Doc file A")
    print("2. Doc file B")
    print("3. Tim kiem")
    print("4. Tong hop")
    print("5. Thong ke")