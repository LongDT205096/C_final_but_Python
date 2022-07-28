I.	Giới thiệu
-	Sản phẩm là bài thi cuối kì 2014 môn C basic 
-	Ngôn ngữ sử dụng: Python
-	Mục đích: luyện tập lập trình với ngôn ngữ Python và ôn lại các cấu trúc dữ liệu

II.	Nội dung 
-	Bài tập yêu cầu viết chương trình quản lí điểm sinh viên với các chức năng đăng nhập và thoát chương trình. 
-	Thông tin đăng nhập được lưu trong 1 file text với 3 trường: username, password, score. Trong đó chia ra 2 loại người dùng phụ trách lớp với tên đăng nhập là Admin và sinh viên là những người dùng còn lại.
-	Người dùng là sinh viên có thể sử dụng các chức năng xem điểm, đổi mật khẩu, lưu thông tin vào file
-	Người dùng là phụ trách lớp (Admin) có thể sử dụng chức năng thêm người dùng, in danh sách, xóa người dùng và lưu thông tin

III.	Giải quyết 
-	Chương trình sử dụng cấu trúc cây nhị phân tìm kiếm, các thao tác với cây và các cấu trúc đệ quy để thực hiện việc tìm kiếm, duyệt danh sách…

   ![image](https://user-images.githubusercontent.com/91714440/177144144-7169b3da-74bb-4f0f-8ca1-b07fe5cdf061.png)
 
-	File dữ liệu chia làm 3 trường: username, password, score. Đặc biệt, người dùng với username là Admin sẽ là người phụ trách.
 
 ![image](https://user-images.githubusercontent.com/91714440/177144355-5a5034af-8d43-4029-94f5-7ad458b3a050.png)

-	Mỗi dòng tương ứng với thông tin của 1 người dùng. Vì vậy, em thực hiện việc đọc từng dòng trong file bằng lệnh read_line(), lưu thông tin vào 1 list, tạo node với các tham số vào là các phần tử trong list và thực hiện thêm node vào cây. Việc sắp xếp các phần tử trong cây theo thứ tự bảng chữ cái của username.
 
 ![image](https://user-images.githubusercontent.com/91714440/177144400-3e29853f-e3ac-4315-bc5b-c001756c7ea7.png)
 
-	Khi người dùng đăng nhập, chương trình sẽ thực hiện đệ quy để tìm kiếm thông tin tài khoản dựa trên username. Tùy vào chức vụ, chương trình sẽ hiển thị 2 loại menu khác nhau và cho phép người thực hiện các chức năng tương ứng
 
![image](https://user-images.githubusercontent.com/91714440/177144440-2fa0d534-0bd0-40a1-b5f7-f8f4d0dd0bc9.png)

 ![image](https://user-images.githubusercontent.com/91714440/177144467-0feb13c5-1228-44e5-9f5c-c52db09a1a04.png)

IV.	Điểm nổi bật
-	Sử dụng cấu trúc cây nhị phân giúp thuận tiện trong việc tìm kiếm (đăng nhập tài khoản)
-	Hướng tối ưu: sử dụng cây AVL (hoặc cây Red-Black đối với file dữ liệu lớn) để tạo sự cân bằng cho cấu trúc cây

V. File nguồn
-  main.py: thực hiện chạy toàn bộ giao diện, chức năng chương trình
-  menu.py: giao diện menu của chương trình, gồm menu chính, menu giáo viên, menu sinh viên
-  GV.py: gồm các lệnh chức năng của người dùng là giáo viên
-  SV.py: gồm các lệnh chức năng của người dùng là sinh viên
-  tree.py: hoạt động của chương trình, gồm các chức năng tìm kiếm, thêm node, xóa node,... trên cấu trúc dữ liệu cây
-  sinhvien.txt: file text chứa thông tin đăng nhập gồm tên đăng nhập, mật khẩu, điểm số của các người dùng
