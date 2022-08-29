import tree
import func

check = 0
option = 0
while option < 6 and option > -1:
    func.menu()
    option = int(input("Chon chuc nang: "))

    if (option != 1 and check == 0) and (option != 6):
        print("Vui long chon chuc nang 1 de doc file\n")
    else:
        if option == 1: 
            f = open("bongda.txt","r")
            root = tree.read_file(f)
            f.close()
            check += 1
            print("Lay du lieu thanh cong\n")

        elif option == 2:
            tree.traversal(root)
            print("\n")

        elif option == 3:
            func._3(root)

        elif option == 4:
            list = []
            rank = int(input("Nhap diem xuong hang: "))
            func._4(root, rank, list)
            print(list,"\n")
            for i in range(len(list)):
                root = tree.delete(root, list[i])

        elif option == 5:
            f = open("ketqua.txt","w")
            tree.output(f, root)
            f.close()
            print("Luu thanh cong\n")

        else:
            print("Thoat chuong trinh\n")
            quit()







