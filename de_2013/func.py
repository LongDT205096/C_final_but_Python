import tree

def menu():
    print("1. Lay du lieu file")
    print("2. Danh sach cac doi")
    print("3. Tim kiem doi bong")
    print("4. Cac doi bong xuong hang")
    print("5. Luu danh sach")
    print("6. Thoat\n")

def _3(root):
    find = input("Ten doi bong: ")
    p = tree.search(root, find)
    if p is not None:
        print(p.team, p.score, "\n")
    else: 
        print("Khong co doi bong nay!\n")

def _4(root, rank, list):
    if root is not None:
        _4(root.left, rank, list)
        if root.score < rank: 
            list.append(root.team)
        _4(root.right, rank, list)

    
