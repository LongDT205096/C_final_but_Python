class Tree:
    def __init__(root, username, password, score): 
        root.left = None
        root.right = None
        root.username = username
        root.password = password
        root.score = float(score)

def add_node(root, new):
    if root is None:
        root = new
    elif root.username < new.username:
        root.right = add_node(root.right, new)
    elif root.username > new.username:
        root.left = add_node(root.left, new)
    return root

def traversal(root):
    if root is not None:
        traversal(root.left)
        print(root.username, root.password, root.score)
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
    elif root.username < user_del:
        root.right = delete(root.right, user_del)
    else:
        if root.left is None:
            new = root.right
            root = None
            return new
        
        elif root.right is None:
            new = root.left
            root = None
            return new

        new = LeftMost(root.right)
        root.username = new.username
        root.right = delete(root.right, new.username)
    return root

def search(root, username):
    if root is None:
        return None
    elif root.username == username:
        return root
    elif root.username < username:
        return search(root.right, username)
    elif root.username > username:
        return search(root.left, username)

def read_file(f):
    root = None
    new = None

    for x in f:
        x = x.split(" ")
        x[-1] = x[-1].strip()
        new = Tree(x[0], x[1], x[2])
        root = add_node(root, new)
    return root

def rewrite(f, root):
    if root is not None:
        rewrite(f, root.left)
        f.write("%s %s %.1f\n" % (root.username, root.password, root.score))
        rewrite(f, root.right)

def login(log_info):
    check = 0
    while True:
        password = input("Password: ")

        if log_info.password == password: 
            print("Dang nhap thanh cong\n")
            break
        check += 1
        if check == 3:
            print("Sai qua 3 lan. Thoat\n")
            quit()


