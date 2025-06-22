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

class WinGUI(Window):
    def __init__(self):
        super().__init__(themename="cosmo", hdpi=False)
        self.__win()
        self.tk_label_title = self.__tk_label_title(self)
        self.tk_button_product = self.__tk_button_product(self)
        self.tk_button_member = self.__tk_button_member(self)
        self.tk_button_staff = self.__tk_button_staff(self)

    def __win(self):
        self.title("管理系统")
        # 设置窗口大小、居中
        width = 600
        height = 400
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) // 2, (screenheight - height) // 2)
        self.geometry(geometry)
        self.minsize(width=width, height=height)

    def new_style(self, widget):
        ctl = widget.cget('style')
        ctl = "".join(random.sample('0123456789', 5)) + "." + ctl
        widget.configure(style=ctl)
        return ctl

    def __tk_label_title(self, parent):
        # 使用LabelFrame来增加边框和标题栏
        frame = LabelFrame(parent, text="无人店销售商品管理系统", bootstyle="primary")
        frame.place(relx=0.5, rely=0.2, anchor='center', relwidth=0.8, relheight=0.2)

        label = Label(frame, text="无人店销售商品管理系统", anchor="center", font=("微软雅黑", 18), bootstyle="primary")
        label.place(relx=0.5, rely=0.5, anchor='center')
        return frame

    def __tk_button_product(self, parent):
        btn = Button(parent, text="商品及供应商管理", takefocus=False, bootstyle="primary")
        btn.place(relx=0.5, rely=0.5, anchor='center', relwidth=0.4, relheight=0.1)
        return btn

    def __tk_button_member(self, parent):
        btn = Button(parent, text="会员管理", takefocus=False, bootstyle="primary")
        btn.place(relx=0.5, rely=0.65, anchor='center', relwidth=0.4, relheight=0.1)
        return btn

    def __tk_button_staff(self, parent):
        btn = Button(parent, text="员工及仓库管理", takefocus=False, bootstyle="primary")
        btn.place(relx=0.5, rely=0.8, anchor='center', relwidth=0.4, relheight=0.1)
        return btn

class Win(WinGUI):
    def __init__(self, controller):
        self.ctl = controller
        super().__init__()
        self.__event_bind()
        self.__style_config()
        self.ctl.init(self)

    def __event_bind(self):
        self.tk_button_product.bind('<Button-1>', self.ctl.product_menu)
        self.tk_button_member.bind('<Button-1>', self.ctl.vip_menu)
        self.tk_button_staff.bind('<Button-1>', self.ctl.staff_menu)

    def __style_config(self):
        sty = Style()
        sty.configure(self.new_style(self.tk_label_title), font=("微软雅黑", 18))
        sty.configure(self.new_style(self.tk_button_product), font=("微软雅黑", -12))
        sty.configure(self.new_style(self.tk_button_member), font=("微软雅黑", -12))
        sty.configure(self.new_style(self.tk_button_staff), font=("微软雅黑", -12))

if __name__ == "__main__":
    win = WinGUI()
    win.mainloop()
