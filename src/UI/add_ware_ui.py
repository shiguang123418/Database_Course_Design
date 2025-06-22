
from tkinter import messagebox
from tkinter.ttk import *
from ttkbootstrap import *
from pytkUI.widgets import *
import pymysql
from UI import menu_ui
from Control import menu_control
from UI import staff_ware_menu
from Control import staff_ware_control
#UI和方法一体
class EmployeeAddApp:
    def __init__(self):
        self.db = pymysql.connect(host="127.0.0.1", user="root", passwd="082415", database="y3")
        self.root = tk.Tk()
        self.root.title("添加仓库数据")
        # 设置窗口大小和位置
        self.set_window_center(600, 550)
        self.create_widgets()

    def run(self):
        self.root.mainloop()  # 只在这里调用一次 mainloop()
    def set_window_center(self, width, height):
        # 计算屏幕中心位置
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) // 2, (screenheight - height) // 2)
        self.root.geometry(alignstr)
    def create_widgets(self):
        # 设置字体
        label_font = font.Font(family="Arial", size=12)
        entry_font = font.Font(family="Arial", size=12)
        # 设置颜色
        label_color = "#333333"
        entry_bg = "#ffffff"

        center_frame = tk.Frame(self.root)
        center_frame.place(relx=0.5, rely=0.5, anchor='center')

        labels = ['仓库编号','仓库名称','仓库地址']
        self.entries = dict()

        for i, label in enumerate(labels):
            tk.Label(center_frame, text=label, font=label_font, fg=label_color).grid(row=i, column=0, pady=5, sticky='w')
            entry = tk.Entry(center_frame, font=entry_font, bg=entry_bg)
            entry.grid(row=i, column=1, pady=5, sticky='e')
            self.entries[label] = entry

        button_style = {'font': ('Arial', 12, 'bold'), 'bg': '#4c98ae', 'fg': '#ffffff', 'activebackground': '#4c98ae',
                        'activeforeground': '#ffffff', 'relief': 'raised', 'bd': 2}

        # 添加数据按钮
        add_button = tk.Button(center_frame, text="添加数据", command=self.add_employee, **button_style)
        add_button.grid(row=len(labels), column=0, sticky='ew', padx=10, pady=10)

        # 取消按钮
        button_back = tk.Button(center_frame, text="取消", command=self.back, **button_style)
        button_back.grid(row=len(labels), column=1, sticky='ew', padx=10, pady=10)

        # 调整按钮宽度
        center_frame.grid_columnconfigure(0, weight=1)
        center_frame.grid_columnconfigure(1, weight=1)

    def add_employee(self):
        data = list({label: entry.get() for label, entry in self.entries.items()}.values())
        cursor = self.db.cursor()
        insert_stmt = "INSERT INTO ware (仓库编号,仓库名称,仓库地址) VALUES (%s, %s, %s)"
        # 执行SQL语句
        try:
            cursor.execute(insert_stmt, data)
            self.db.commit()
            messagebox.showinfo("成功", "仓库数据已成功添加！")
        except pymysql.Error as err:
            messagebox.showerror("错误", f"数据添加失败: {err}")
        finally:
            cursor.close()

    def back(self):
        self.root.destroy()
        win = staff_ware_menu.Win(staff_ware_control.Controller())
        win.mainloop()
if __name__ == "__main__":
    app = EmployeeAddApp()
    app.run()

