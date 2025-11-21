"""
Luyện tập sử dụng ListBox trong guizero để hiển thị danh sách dữ liệu.
Thực hành đọc và ghi file (users.txt).
Thực hành thao tác thêm, xóa, chọn dữ liệu từ GUI.

* Yêu cầu nâng cao (tùy chọn)
Thêm xác nhận trước khi xóa (Yes/No).
Hiển thị thông tin chi tiết khi chọn username (ví dụ: password bị ẩn bằng dấu *).
Sắp xếp danh sách người dùng theo tên.

"""
from guizero import App, Text, PushButton, TextBox, info, Box, ListBox
name_and_password = {}
name_and_password_add = {}
try:
    with open("control_users.txt", "r", encoding = "utf8") as file:
        lst_file = file.readlines()
        for i in range(0, len(lst_file), 2):
            key = lst_file[i].strip()
            value = lst_file[i + 1].strip()
            name_and_password[key] = value
except FileNotFoundError:
    name_and_password = {}
def show_users():
    user_name_choose = users.value
    name.value = user_name_choose
    password.value = name_and_password[user_name_choose]
    password.hide_text = True
def save(func_choose: str, valuable):
    global name_and_password_add
    if func_choose == "add":
        for key, value in name_and_password_add.items():
            name_and_password[key] = value
            users.append(key)
            with open("control_users.txt", "a", encoding = "utf8") as file:
                file.write(f"{key}\n")
                file.write(f"{value}\n")
        name_and_password_add.clear()
    elif func_choose == "del":
        with open("control_users.txt", "r", encoding = "utf8") as file:
            lst_file = file.readlines()
            lst_copy = lst_file.copy()
            for x in lst_copy:
                if valuable == x.removesuffix("\n"):
                    lst_file.remove(f"{valuable}\n")
                    lst_file.remove(f"{name_and_password[valuable]}\n")
        with open("control_users.txt", "w", encoding = "utf8") as file:
            for x in lst_file:
                file.write(x)
def del_user():
        global name, password, name_and_password
        for key in list(name_and_password.keys()):
            if name.value == key and password.value == name_and_password[key]:
                info("Thông báo", "Xóa người dùng thành công!")
                save("del", name.value)
                name_and_password.pop(name.value)
                users.remove(name.value)
                name.clear()
                password.clear()
                break
        else:
            info("Thông báo", "Xóa người dùng thất bại!!!")
            name.clear()
            password.clear()
def new_user():
    global name_and_password_add, name, password
    if (name.value not in name_and_password_add.keys() and name.value not in name_and_password.keys()) and name.value.strip() != "" and password.value.strip() != "":
        name_and_password_add[name.value] = password.value
        info("Thông báo", "Thêm người dùng thành công!!!")
        name.clear()
        password.clear()
        save("add", "")
    else:
        info("Thông báo", "Người dùng đã có, bạn nên thêm người dùng khác!!!")
        name.clear()
        password.clear()
app = App(title = "Hệ thống quản lí người dùng", width = 400, height = 400)
Text(app, align = "top", text = "Danh sách người dùng:", size = 15, color = "red")
users = ListBox(app, align = "top", scrollbar = True, items = name_and_password, command = show_users)
box_input = Box(app, height = 80, width = 350, align = "top", layout = "grid")
Text(box_input, size = 20, align = "left", color = "red", text = "Tên: ", grid = [0,0])
name = TextBox(box_input, width = 250, grid = [1,0])
Text(box_input, size = 20, align = "left", color = "red", text = "Mật khẩu: ", grid = [0,1])
password = TextBox(box_input, width = 250, grid = [1,1], hide_text = True)
add_user = PushButton(app, align = "left", text = "Thêm người dùng", width = 25, height = 6, command = new_user)
add_user.bg = "lightgreen"
remove_user = PushButton(app, align = "left", text = "Xóa người dùng", width = 25, height = 6, command = del_user)
remove_user.bg = "orange"

app.display()