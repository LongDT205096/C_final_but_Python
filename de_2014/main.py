import tree 
import SV
import GV
import menu

f = open("sinhvien.txt","r")
root = tree.read_file(f)
f.close()

option = 1
while option > 0 and option < 2:
    menu.main_menu()
    option = int(input("Chon chuc nang: "))
    
    if option == 1:
        log_info = None
        while log_info is None:
            username = input("Username: ")
            log_info = tree.search(root, username)
        
        tree.login(log_info)

        if username != "Admin":
            menu.menu_SV()
            opt = 0
            while opt != 3:
                opt = int(input("\nChon chuc nang: "))

                if opt == 1: SV._1(log_info)
                elif opt == 2: SV._2(root, log_info)
                elif opt == 3:
                    print("\nChon chuc nang luu thong tin\n")
                    f = open("sinhvien.txt","w")
                    tree.rewrite(f, root)
                    f.close()
                    print("Luu thanh cong\n")
        else:
            menu.menu_GV()
            opt = 0
            while opt != 4:
                opt = int(input("\nChon chuc nang: "))

                if opt == 1: GV._1(root)
                elif opt == 2: 
                    print("\nChon chuc nang in danh sach\n")
                    GV._2(root)
                elif opt == 3: GV._3(root)
                elif opt == 4:
                    print("\nChon chuc nang luu thong tin\n")
                    f = open("sinhvien.txt","w")
                    tree.rewrite(f, root)
                    f.close()
                    print("Luu thanh cong\n")

    elif option == 2:
        print("\nThoat chuong trinh thanh cong\n")
        quit()

