"""
Thực hành tạo giao diện GUI với guizero.
Sử dụng TextBox để nhập dữ liệu.
Sử dụng ListBox hoặc Box hiển thị danh sách công việc.
Thực hành đọc/ghi file (tasks.txt).
Thực hành thêm, xóa và đánh dấu hoàn thành công việc.

"""
from guizero import App, Text, ListBox, TextBox, Box, PushButton, info
your_work_now = ""
index_your_work_now = 0
app = App(title = "To - Do app", width = 1000, height = 600)
def save(what_will_I_write, file_type: str, loop: bool):
    if not loop:
        with open("tasks.txt", file_type, encoding = "utf8") as file:
            file.write(f"{what_will_I_write} \n")
    else:
        with open("tasks.txt", file_type, encoding = "utf8") as file:
            for i in range(len(what_will_I_write)):
                file.write(f"{what_will_I_write[i]} \n")
def work_to_do():
    global lst_to_do
    if f"[] {your_choose_work.value}" not in lst_to_do.items:
        lst_to_do.append(f"[] {your_choose_work.value}")
        save(f"[] {your_choose_work.value}", "a", False) # Save chỉ cho phép lưu chứ không đọc được
    else:
        info("Thông báo", "Bạn đã đặt công việc này! Bạn nên hoàn thành trước khi đặt lại!")
    your_choose_work.clear()
def nothing():
    global your_work_now, index_your_work_now
    your_work_now = str(lst_to_do.value)
    index_your_work_now = int(lst_to_do.items.index(your_work_now))
def delete():
    global your_work_now, lst_to_do
    lst_work = lst_to_do.items
    for x in lst_work:
        if x == your_work_now:
            lst_to_do.remove(your_work_now)
    save(lst_to_do.items, "w", True)
def tick():
    global your_work_now, lst_to_do
    lst_work = lst_to_do.items
    for x in lst_work:
        if x == your_work_now and str(x).startswith("[] "):
            lst_to_do.remove(your_work_now)
            lst_to_do.insert(index_your_work_now, f"[x] {your_work_now.removeprefix("[] ")}")
            # break. Ở đây có thể break để tránh trường hợp nhiều nhiệm vụ đã hoàn thành giống nhau bị xóa.
    save(lst_to_do.items, "w", True) # Save chỉ cho phép lưu chứ không đọc được
box_more_work = Box(app, width = 1000, height = 100, align = "top", layout = "grid")
Text(box_more_work, align = "left", text = "Thêm công việc mới: ", size = 20, color = "red", grid = [0,0])
your_choose_work = TextBox(box_more_work, align = "left", width = 800, height = 1, grid = [1,0])
add_work = PushButton(box_more_work, text = "Thêm công việc", grid = [0,1], width = 50, command = work_to_do)
add_work.bg = "lightblue"
box_work = Box(app, width = 1000, height = 400, align = "top")
Text(box_work, text = "Danh sách công việc", size = 20, color = "red")
lst_to_do = ListBox(box_work, scrollbar = True, items = [], width = 500, height = 370, command = nothing)
try:
    with open("tasks.txt", "r", encoding = "utf8") as file:
        unneed = file.readlines()
        for x in unneed:
            lst_to_do.append(x.removesuffix(" \n"))
except FileNotFoundError:
    pass
box_tick = Box(app, width = 1000, height = 100, align = "top")
del_work = PushButton(box_tick, text = "Xóa công việc", height = 5, width = 67, align = "left", command = delete)
del_work.bg = "orange"
tick_work = PushButton(box_tick, text = "Đánh dấu công việc", height = 5, width = 68, align = "left", command = tick)
tick_work.bg = "lightgreen"

app.display()