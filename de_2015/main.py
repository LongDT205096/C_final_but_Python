import tree
import function 

root_B = {}
list = []
a = 1
check = 0

while a > 0 and a < 6:
    function.menu()
    a = int(input("\nChon chuc nang: "))

    if a == 1:
        f = open("A.txt","r")
        print("Doc thong tin file A:")
        root_A = tree.read_A(f)
        f.close()
        tree.traversal(root_A)

    elif a == 2:
        f = open("B.txt","r")
        print("Doc thong tin file B:")
        tree.read_B(f, root_B)
        check += 1
        f.close()

        for x, y in root_B.items():
            print(x,y)
        
    elif a == 3:
        if check == 0:
            print("Chua co thong tin file B. Hay kiem tra lai.")
            continue

        function.func_3(root_A, root_B, list)
        print(list)
        for x in list:
            root_A = tree.delete(root_A, x)
        tree.traversal(root_A)

    elif a == 4:
        root_A = function.func_4(root_A, root_B)
        tree.traversal(root_A)
