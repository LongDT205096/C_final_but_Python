def _1(log_info):
    print("\nChuc nang xem diem cua sinh vien.\n")
    print("Diem cua sinh vien: ", log_info.score)
        
def _2(root, log_info):
    print("\nDa chon chuc nang doi mat khau\n")
    print("Nhap mat khau moi: ")
    new_pass = input()
    while True: 
        print("Xac nhan lai mat khau: ")
        pass_check = input()
        if pass_check == new_pass: break

    log_info.password = new_pass
    print("Doi mat khau thanh cong.\n")