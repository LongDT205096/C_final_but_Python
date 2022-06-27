import tree 
import SV
import GV
import menu

f = open("d:\Github\C_final_but_Python\de_2014\sinhvien.txt","r")
root = tree.read_file(f)
f.close()

option = 1
while option > 0 and option < 2:
    menu.main_menu()
    print("Chon chuc nang: ")
    option = int(input())
    
    if option == 1:
        log_info = None
        while log_info is None:
            print("Username:") 
            username = input()
            log_info = tree.search(root, username)
        
        tree.login(log_info)

        if username != "Admin":
            menu.menu_SV()
            opt = 0
            while opt != 3:
                print("\nChon chuc nang: ")
                opt = int(input())

                if opt == 1: SV._1(log_info)
                elif opt == 2: SV._2(root, log_info)
                elif opt == 3:
                    print("\nChon chuc nang luu thong tin\n")
                    f = open("d:\Github\C_final_but_Python\de_2014\sinhvien.txt","w")
                    tree.rewrite(f, root)
                    f.close()
        else:
            menu.menu_GV()
            opt = 0
            while opt != 4:
                print("\nChon chuc nang: ")
                opt = int(input())

                if opt == 1: GV._1(root)
                elif opt == 2: GV._2(root)
                elif opt == 3: GV._3(root)
                elif opt == 4:
                    print("\nChon chuc nang luu thong tin\n")
                    f = open("d:\Github\C_final_but_Python\de_2014\sinhvien.txt","w")
                    tree.rewrite(f, root)
                    f.close()

    elif option == 2:
        print("\nThoat chuong trinh thanh cong\n")
        quit()

