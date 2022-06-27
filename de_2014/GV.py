from tree import Tree, add_node, delete, search

def _1(root):
    print("\nChon chuc nang them sinh vien\n")
    print("Username: ")
    username = input()
    print("Password: ")
    password = input()
    print("Score: ")
    score = int(input())
    new = Tree(username, password, score)
    root = add_node(root, new)

def _2(root):
    print("\nChon chuc nang in danh sach\n")
    if root is not None:
        _2(root.left)
        if root.username != "Admin":
            print(root.username, root.password, root.score)
        _2(root.right)

def _3(root):
    print("\nChon chuc nang xoa\n")
    user_del = str
    while True:
        user_del = input()
        if user_del != "Admin": break

    del_node = search(root, user_del)

    if del_node is not None:
        print(del_node.username, del_node.password, del_node.score)
        root = delete(root, user_del)
        print("Xoa thanh cong\n")
    else:
        print("User khong ton tai\n")
