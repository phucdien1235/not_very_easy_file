"""
Thực hành tạo giao diện GUI với guizero.
Sử dụng TextBox để nhập dữ liệu.
Thực hành đọc và ghi dữ liệu vào file (users.txt).
Xử lý logic đăng ký và đăng nhập cơ bản.

* Yêu cầu nâng cao (tùy chọn)
Thêm khả năng xóa tài khoản đã đăng ký.
Thêm thông báo chi tiết nếu người dùng nhập thiếu thông tin.

"""
from guizero import App, Text, PushButton, TextBox, info, Box, ListBox, yesno
name_and_password = {}
name_and_password_add = {}
try:
    with open("users.txt", "r", encoding = "utf8") as file:
        lst_file = file.readlines()
        for i in range(0, len(lst_file), 2):
            key = lst_file[i].strip()
            value = lst_file[i + 1].strip()
            name_and_password[key] = value
except FileNotFoundError:
    name_and_password = {}
def save(func_choose: str, valuable):
    global name_and_password_add
    if func_choose == "add":
        for key, value in name_and_password_add.items():
            name_and_password[key] = value
            with open("users.txt", "a", encoding = "utf8") as file:
                file.write(f"{key}\n")
                file.write(f"{value}\n")
        name_and_password_add.clear()
    elif func_choose == "del":
        with open("users.txt", "r", encoding = "utf8") as file:
            lst_file = file.readlines()
            lst_copy = lst_file.copy()
            for x in lst_copy:
                if valuable == x.removesuffix("\n"):
                    lst_file.remove(f"{valuable}\n")
                    lst_file.remove(f"{name_and_password[valuable]}\n")
        with open("users.txt", "w", encoding = "utf8") as file:
            for x in lst_file:
                file.write(x)
def __dang_nhap__():
    global name, password
    for key in name_and_password.keys():
        if name.value == key and password.value == name_and_password[key]:
            info("Thông báo", "Đăng nhập thành công!")
            save("del", name.value)
            name_and_password.pop(name.value)
            name.clear()
            password.clear()
            break
    else:
        info("Thông báo", "Đăng nhập thất bại!!!")
        name.clear()
        password.clear()
def __dang_ki__():
    global name_and_password_add, name, password
    if (name.value not in name_and_password_add.keys() and name.value not in name_and_password.keys()) and name.value.strip() != "" and password.value.strip() != "":
        name_and_password_add[name.value] = password.value
        info("Thông báo", "Đăng kí thành công!!!")
        name.clear()
        password.clear()
        save("add", "")
    else:
        info("Thông báo", "Tên này đã có, bạn có thể đăng nhập!!!")
        name.clear()
        password.clear()
app = App(title = "Hệ thống điều khiển mật khẩu", width = 400, height = 200)
box_input = Box(app, height = 80, width = 350, align = "top", layout = "grid")
Text(box_input, size = 20, align = "left", color = "red", text = "Tên: ", grid = [0,0])
name = TextBox(box_input, width = 250, grid = [1,0])
Text(box_input, size = 20, align = "left", color = "red", text = "Mật khẩu: ", grid = [0,1])
password = TextBox(box_input, width = 250, grid = [1,1], hide_text = True)
dang_nhap = PushButton(app, align = "left", text = "Đăng nhập", width = 25, height = 6, command = __dang_nhap__)
dang_nhap.bg = "lightgreen"
dang_ki = PushButton(app, align = "left", text = "Đăng kí", width = 25, height = 6, command = __dang_ki__)
dang_ki.bg = "orange"

app.display()