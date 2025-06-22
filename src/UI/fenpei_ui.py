"""
本代码由[Tkinter布局助手]生成
官网:https://www.pytk.net
QQ交流群:905019785
在线反馈:https://support.qq.com/product/618914
"""
import random
from tkinter import *
from tkinter.ttk import *
from ttkbootstrap import *
from pytkUI.widgets import *
import pymysql

class WinGUI(Window):
    def __init__(self):
        super().__init__(themename="cosmo", hdpi=False)
        self.warehouses = None
        self.admins = None
        self.db = pymysql.connect(host="127.0.0.1", user="y2", passwd="082415", database="y3")
        self.db_connect()
        self.__win()
        self.tk_select_box_lxg72jwe = self.__tk_select_box_lxg72jwe(self)
        self.tk_select_box_lxg72wwf = self.__tk_select_box_lxg72wwf(self)
        self.tk_label_lxg73s4v = self.__tk_label_lxg73s4v(self)
        self.tk_label_lxg7462h = self.__tk_label_lxg7462h(self)
        self.tk_button_lxg74ihp = self.__tk_button_lxg74ihp(self)
        self.tk_button_lxg74lhq = self.__tk_button_lxg74lhq(self)
    def db_connect(self):
        self.admins = self.fetch_from_db("SELECT 员工编号 FROM staff")
        self.warehouses = self.fetch_from_db("SELECT 仓库编号 FROM ware")
    def fetch_from_db(self, query):
        cursor = self.db.cursor()
        cursor.execute(query)
        results = [row[0] for row in cursor.fetchall()]
        cursor.close()
        return results
    def __win(self):
        self.title("管理系统")
        # 设置窗口大小、居中
        width = 600
        height = 500
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)
        self.minsize(width=width, height=height)

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

    def v_scrollbar(self, vbar, widget, x, y, w, h, pw, ph):
        widget.configure(yscrollcommand=vbar.set)
        vbar.config(command=widget.yview)
        vbar.place(relx=(w + x) / pw, rely=y / ph, relheight=h / ph, anchor='ne')

    def h_scrollbar(self, hbar, widget, x, y, w, h, pw, ph):
        widget.configure(xscrollcommand=hbar.set)
        hbar.config(command=widget.xview)
        hbar.place(relx=x / pw, rely=(y + h) / ph, relwidth=w / pw, anchor='sw')

    def create_bar(self, master, widget, is_vbar, is_hbar, x, y, w, h, pw, ph):
        vbar, hbar = None, None
        if is_vbar:
            vbar = Scrollbar(master)
            self.v_scrollbar(vbar, widget, x, y, w, h, pw, ph)
        if is_hbar:
            hbar = Scrollbar(master, orient="horizontal")
            self.h_scrollbar(hbar, widget, x, y, w, h, pw, ph)
        self.scrollbar_autohide(vbar, hbar, widget)

    def new_style(self, widget):
        ctl = widget.cget('style')
        ctl = "".join(random.sample('0123456789', 5)) + "." + ctl
        widget.configure(style=ctl)
        return ctl

    def __tk_select_box_lxg72jwe(self, parent):
        cb = Combobox(parent, state="readonly", bootstyle="default")
        cb['values'] = self.admins
        cb.place(relx=0.4783, rely=0.1880, relwidth=0.3483, relheight=0.0800)
        return cb

    def __tk_select_box_lxg72wwf(self, parent):
        cb = Combobox(parent, state="readonly", bootstyle="default")
        cb['values'] = self.warehouses
        cb.place(relx=0.4800, rely=0.3980, relwidth=0.3367, relheight=0.0900)
        return cb

    def __tk_label_lxg73s4v(self, parent):
        label = Label(parent, text="员工编号：", anchor="center", bootstyle="default")
        label.place(relx=0.1917, rely=0.1860, relwidth=0.2333, relheight=0.0800)
        return label

    def __tk_label_lxg7462h(self, parent):
        label = Label(parent, text="仓库编号：", anchor="center", bootstyle="default")
        label.place(relx=0.1950, rely=0.4120, relwidth=0.2333, relheight=0.0800)
        return label

    def __tk_button_lxg74ihp(self, parent):
        btn = Button(parent, text="分配", takefocus=False, bootstyle="default")
        btn.place(relx=0.2000, rely=0.6020, relwidth=0.1717, relheight=0.1140)
        return btn

    def __tk_button_lxg74lhq(self, parent):
        btn = Button(parent, text="取消", takefocus=False, bootstyle="default")
        btn.place(relx=0.6000, rely=0.6060, relwidth=0.1917, relheight=0.1100)
        return btn

class Win(WinGUI):
    def __init__(self, controller):
        self.ctl = controller
        super().__init__()
        self.__event_bind()
        self.__style_config()
        self.ctl.init(self)

    def __event_bind(self):
        self.tk_button_lxg74ihp.bind('<Button-1>', self.ctl.fenpei)
        self.tk_button_lxg74lhq.bind('<Button-1>', self.ctl.back)
        pass

    def __style_config(self):
        sty = Style()
        sty.configure(self.new_style(self.tk_label_lxg73s4v), font=("微软雅黑", -18))
        sty.configure(self.new_style(self.tk_label_lxg7462h), font=("微软雅黑", -18))
        sty.configure(self.new_style(self.tk_button_lxg74ihp), font=("微软雅黑", -12))
        sty.configure(self.new_style(self.tk_button_lxg74lhq), font=("微软雅黑", -12))
        pass


if __name__ == "__main__":
    win = WinGUI()
    win.mainloop()