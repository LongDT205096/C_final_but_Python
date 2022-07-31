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
-	Chương trình sử dụng cấu trúc cây nhị phân tìm kiếm, các thao tác với cây và các câu lệnh đệ quy để thực hiện việc tìm kiếm, duyệt danh sách…

   ![image](https://user-images.githubusercontent.com/91714440/177144144-7169b3da-74bb-4f0f-8ca1-b07fe5cdf061.png)
 
-	File dữ liệu chia làm 3 trường: username, password, score. Người dùng với username là Admin sẽ là người phụ trách.
 
   ![image](https://user-images.githubusercontent.com/91714440/177144355-5a5034af-8d43-4029-94f5-7ad458b3a050.png)

-	Mỗi dòng tương ứng với thông tin của 1 người dùng. Vì vậy, em thực hiện việc đọc từng dòng trong file bằng lệnh read_line(), lưu thông tin vào 1 list, tạo node với các tham số vào là các phần tử trong list và thực hiện thêm node vào cây. Việc sắp xếp các phần tử trong cây theo thứ tự bảng chữ cái của username.
 
   ![image](https://user-images.githubusercontent.com/91714440/177144400-3e29853f-e3ac-4315-bc5b-c001756c7ea7.png)
 
-	Khi người dùng đăng nhập, chương trình sẽ thực hiện đệ quy để trả về node chứa thông tin tài khoản dựa trên username. Chương trình cho phép nhập tên tài khoản nhiều lần nếu nhập sai bằng vòng lặp while.
-  Sau khi tìm được node khớp với username đã nhập, chương trình thực hiện kiếm tra với password người dùng nhập. Nếu nhập sai quá 3 lần, chương trình sẽ dừng ngay lập tức.
 
   ![image](https://user-images.githubusercontent.com/91714440/177144440-2fa0d534-0bd0-40a1-b5f7-f8f4d0dd0bc9.png)
   ![image](https://user-images.githubusercontent.com/91714440/182027969-0c8b32a2-5cd4-49a9-8706-f535e3563ddd.png)
   

- Tùy vào chức vụ, chương trình sẽ hiển thị 2 loại menu khác nhau và cho phép người thực hiện các chức năng tương ứng. Việc chọn chức năng tương ứng với số thứ tự trên menu.

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

\
\
\
→  chuyển tiếng nhật

I.　情報
-  プロジェクトは2014のCベーシックの最終試験。
-  言語：Python
-  目標：Python言語でプログラムを書くこととデータ構造を復習します

II.　内容
-  この演習では、ログインおよびログアウトする機能を備えた学生スコア管理プログラムを書きます。
-  ログイン情報は、ユーザー名、パスワード、スコアの3つのフィールドを持つテキストファイルに保存されます。その中で、クラスの担任のユーザー名はAdminで、残りのユーザーは学生です。
-  学生ユーザーは、成績を表示し、パスワードを変更し、ファイルへの情報の保存の機能を使用できます。
-  クラスの担任（Admin）は、ユーザーの追加、リストの印刷、ユーザーの削除、情報の保存の機能を利用できます。

III.  扱う
-  プログラムは、バイナリ検索ツリー構造と再帰ステートメントを使用して、検索やリストトラバーサルなどを実行します。

               \image

-  データファイルは、ユーザー名、パスワード、スコアの3つのフィールドに分かれています。 ユーザー名がAdminのユーザーが担当者です。

               \image

-  各行は1人のユーザーの情報に対応します。それで、read_line（）コマンドを使用してファイルの各行を読み取って、情報をリストに保存して、入力パラメーターをリストの要素として使用してノードを作成して、ツリーにノードを追加します。ツリーの要素は、ユーザー名のアルファベット順にソートされています。

               \image

-  ユーザーがログインすると、プログラムはユーザー名に基づいてアカウント情報を含むノードを再帰的に返します。プログラムは、アカウント名が間違って入力された場合、whileループを使うため、何度もアカウント名を入力することができます