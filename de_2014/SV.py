def _1(log_info):
    print("\nChuc nang xem diem cua sinh vien.\n")
    print("Diem cua sinh vien: ", log_info.score)
        
def _2(root, log_info):
    print("\nDa chon chuc nang doi mat khau\n")
    new_pass = input("Nhap mat khau moi: ")

    while True: 
        pass_check = input("Xac nhan lai mat khau: ")
        if pass_check == new_pass: break

    log_info.password = new_pass
    print("Doi mat khau thanh cong.\n")