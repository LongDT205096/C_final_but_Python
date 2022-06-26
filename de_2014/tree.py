class Tree:
    def __init__(root, username, password, score): 
        root.left = None
        root.right = None
        root.username = username
        root.password = password
        root.score = score

def add_node(root, new):
    if root is None:
        root = new
    elif root.username < new.username:
        root.right = add_node(root.right, new)
    elif root.username > new.username:
        root.left = add_node(root.left, new)

def traversal(root):
    traversal(root.left)
    print(root.username)
    traversal(root.right)

def LeftMost(root):
    while root.left is not None:
        root = root.left
    return root

def delete(root, user_del):
    if root is None:
        return root
    if root.username > user_del:
        root.left = delete(root.left, user_del)
    elif root.user < user_del:
        root.right = delete(root.right, user_del)
    else:
        if root.left is None:
            new = root.right
            root = None
            return new
        
        elif root.right is None:
            pass