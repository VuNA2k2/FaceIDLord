import tkinter
from tkinter import *
from tkinter import messagebox

import RecognitionData
from DatabaseConnection import DatabaseConnection
from getData2 import GetData

# Tạo một cửa sổ
window = Tk()

# Đặt tiêu đề cho cửa sổ
window.title("Nhập thông tin sinh viên")

# Đặt kích thước cho cửa sổ
window.geometry('350x200')

# Tạo các đối tượng Label và Entry để nhập thông tin
name_label = Label(window, text="Họ tên")
name_label.grid(column=0, row=0)
name_entry = Entry(window, width=30)
name_entry.grid(column=1, row=0)

age_label = Label(window, text="Tuổi")
age_label.grid(column=0, row=1)
age_entry = Entry(window, width=30)
age_entry.grid(column=1, row=1)

class_label = Label(window, text="Lớp")
class_label.grid(column=0, row=2)
class_entry = Entry(window, width=30)
class_entry.grid(column=1, row=2)

id_label = Label(window, text="Mã sinh viên")
id_label.grid(column=0, row=3)
id_entry = Entry(window, width=30)
id_entry.grid(column=1, row=3)
connection = DatabaseConnection().__enter__()
# Tạo một hàm xử lý sự kiện cho nút Submit
def submit_info():
    name = name_entry.get()
    age = age_entry.get()
    class_name = class_entry.get()
    id_number = id_entry.get()
    cursor = connection.cursor()
    sql = "SELECT id FROM users WHERE student_code =%s";
    cursor.execute(sql, id_number)
    result = cursor.fetchone()
    print(result[0])
    if(result[0]):
        print("Mã sinh viên đã tồn tại")
    else:
        sql = "INSERT INTO users (name, age, class, student_code) VALUES (%s, %s, %s, %s) RETURNING id"
        val = (name, age, class_name, id_number)
        cursor.execute(sql, val)
        connection.commit()
        lastId = cursor.fetchone()[0]
        print(lastId)
        GetData().getDataForStudentCode(str(lastId))
        window.destroy()
        print(cursor.rowcount, "record inserted.")
        print("Đã thêm sinh viên thành công")

def recognition():
    name = name_entry.get()
    age = age_entry.get()
    class_name = class_entry.get()
    id_number = id_entry.get()
    try:
        cursor = connection.cursor()
        sql = "SELECT id FROM users WHERE student_code =%s AND name = %s AND age = %s AND class = %s";
        cursor.execute(sql, (id_number, name, age, class_name))
        connection.commit()
        result = cursor.fetchone()
        print(result[0])
        print(sql)
        if(result[0]):
            id = result[0]
            RecognitionData.Recognition().recognition(id, name, id_number, class_name, age)
        else:
            messagebox.showerror("Error", "Không tìm thấy sinh viên")
    except:
        messagebox.showerror("Error", "Không tìm thấy sinh viên")

# Tạo một nút Submit
submit_button = Button(window, text="Submit", command=submit_info)
recognizer_button = Button(window, text="Recognizer", command=recognition)
submit_button.grid(column=1, row=4)
recognizer_button.grid(column=1, row=5)

# Hiển thị cửa sổ
window.mainloop()
