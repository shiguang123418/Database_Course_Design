import tkinter as tk
from tkinter import ttk, messagebox
import pymysql
from datetime import date
import random
from ttkbootstrap import Window
from UI import product_munu_ui
from Control import product_munu_control
#UI和方法一体
class WinGUI(Window):
    def __init__(self):
        super().__init__(themename="cosmo", hdpi=False)
        self.__win()
        self.create_widgets()

    def __win(self):
        self.title("Tkinter布局助手")
        width = 600
        height = 500
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)
        self.resizable(width=False, height=False)

    def scrollbar_autohide(self, vbar, hbar, widget):
        def show():
            if vbar: vbar.lift(widget)
            if hbar: hbar.lift(widget)

        def hide():
            if vbar: vbar.lower(widget)
            if hbar: hbar.lower(widget)

        hide()
        widget.bind("<Enter>", lambda e: show())
        if vbar: vbar.bind("<Enter>", lambda e: show())
        if vbar: vbar.bind("<Leave>", lambda e: hide())
        if hbar: hbar.bind("<Enter>", lambda e: show())
        if hbar: hbar.bind("<Leave>", lambda e: hide())
        widget.bind("<Leave>", lambda e: hide())

    def create_widgets(self):
        frame_entry = ttk.Frame(self)
        frame_entry.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

        ttk.Label(frame_entry, text='供应商编号:').grid(row=0, column=0, padx=10, pady=10, sticky='e')
        self.entry_product_id = ttk.Entry(frame_entry)
        self.entry_product_id.grid(row=0, column=1, padx=10, pady=10)
        self.entry_product_id.insert(0, str(self.get_next_entry_id()))

        ttk.Label(frame_entry, text='供应名称:').grid(row=1, column=0, padx=10, pady=10, sticky='e')
        self.entry_manager_id = ttk.Entry(frame_entry)
        self.entry_manager_id.grid(row=1, column=1, padx=10, pady=10)

        ttk.Label(frame_entry, text='联系电话:').grid(row=2, column=0, padx=10, pady=10, sticky='e')
        self.entry_quantity = ttk.Entry(frame_entry)
        self.entry_quantity.grid(row=2, column=1, padx=10, pady=10)

        ttk.Label(frame_entry, text='地址:').grid(row=3, column=0, padx=10, pady=10, sticky='e')
        self.entry_total_amount = ttk.Entry(frame_entry)
        self.entry_total_amount.grid(row=3, column=1, padx=10, pady=10)

        ttk.Label(frame_entry, text='开户银行:').grid(row=4, column=0, padx=10, pady=10, sticky='e')
        self.entry_supplier_id = ttk.Entry(frame_entry)
        self.entry_supplier_id.grid(row=4, column=1, padx=10, pady=10)

        ttk.Label(frame_entry, text='银行账户:').grid(row=5, column=0, padx=10, pady=10, sticky='e')
        self.entry_entry_date = ttk.Entry(frame_entry)
        self.entry_entry_date.grid(row=5, column=1, padx=10, pady=10)

        ttk.Button(self, text='添加', command=self.add_entry, width=10).grid(row=7, column=0, padx=10, pady=10, sticky='we')

        ttk.Button(self, text='取消', command=self.back, width=10).grid(row=7, column=1, padx=10, pady=10, sticky='we')

    def get_next_entry_id(self):
        connection = pymysql.connect(host="127.0.0.1", user="root", password="082415", database="y3")
        cursor = connection.cursor()
        sql = f"SELECT * FROM vendor"
        cursor.execute(sql)
        results = len(cursor.fetchall()) + 1
        return results

    def add_entry(self):
        product_id = self.entry_product_id.get()
        manager_id = self.entry_manager_id.get()
        quantity = self.entry_quantity.get()
        total_amount = self.entry_total_amount.get()
        supplier_id = self.entry_supplier_id.get()
        entry_date = self.entry_entry_date.get()
        print(product_id, manager_id, quantity, total_amount, supplier_id, entry_date)
        if not (product_id and quantity and total_amount and supplier_id and entry_date  and manager_id):
            messagebox.showerror('错误', '所有字段都必须填写')
            return

        connection = pymysql.connect(host="127.0.0.1", user="root", password="082415", database="y3")
        cursor = connection.cursor()

        try:
            insert_query = "INSERT INTO vendor (供应商编号, 供应商名称, 联系电话, 地址, 开户银行, 银行账户) " \
                           "VALUES (%s, %s, %s, %s, %s, %s)"
            entry_data = (product_id,manager_id, quantity, total_amount, supplier_id, entry_date)
            cursor.execute(insert_query, entry_data)
            connection.commit()
            messagebox.showinfo('成功', '供应商信息已成功添加')

        except pymysql.Error as err:
            messagebox.showerror('数据库错误', f'添加供应商时发生错误: {err}')

    def back(self):
        self.destroy()
        main_win = product_munu_ui.Win(product_munu_control.Controller())
        main_win.mainloop()
class Win(WinGUI):
    def __init__(self, controller):
        self.ctl = controller
        super().__init__()
        self.ctl.init(self)
if __name__ == "__main__":
    add_entry_page = WinGUI()
    add_entry_page.mainloop()
