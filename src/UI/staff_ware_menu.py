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
        self.tk_button_lxhnghg6 = self.__tk_button_lxhnghg6(self)
        self.tk_button_lxhngntl = self.__tk_button_lxhngntl(self)
        self.tk_button_lxhngsww = self.__tk_button_lxhngsww(self)
        self.tk_button_lxhngyvd = self.__tk_button_lxhngyvd(self)
        self.tk_button_lxhnhabn = self.__tk_button_lxhnhabn(self)

    def __win(self):
        self.title("Tkinter布局助手")
        # 设置窗口大小、居中
        width = 600
        height = 500
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)

        self.resizable(width=False, height=False)

    def scrollbar_autohide(self, vbar, hbar, widget):
        """自动隐藏滚动条"""

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

    def __tk_button_lxhnghg6(self, parent):
        btn = Button(parent, text="添加员工", takefocus=False, bootstyle="default")
        btn.place(x=0, y=29, width=143, height=50)
        return btn

    def __tk_button_lxhngntl(self, parent):
        btn = Button(parent, text="修改员工", takefocus=False, bootstyle="default")
        btn.place(x=0, y=120, width=143, height=50)
        return btn

    def __tk_button_lxhngsww(self, parent):
        btn = Button(parent, text="添加仓库", takefocus=False, bootstyle="default")
        btn.place(x=0, y=210, width=143, height=50)
        return btn

    def __tk_button_lxhngyvd(self, parent):
        btn = Button(parent, text="仓库管理员分配", takefocus=False, bootstyle="default")
        btn.place(x=188, y=32, width=143, height=48)
        return btn

    def __tk_button_lxhnhabn(self, parent):
        btn = Button(parent, text="返回", takefocus=False, bootstyle="default")
        btn.place(x=187, y=328, width=152, height=54)
        return btn


class Win(WinGUI):
    def __init__(self, controller):
        self.ctl = controller
        super().__init__()
        self.__event_bind()
        self.__style_config()
        self.ctl.init(self)

    def __event_bind(self):
        self.tk_button_lxhnghg6.bind('<Button-1>', self.ctl.add_staff)
        self.tk_button_lxhngntl.bind('<Button-1>', self.ctl.update_staff)
        self.tk_button_lxhngsww.bind('<Button-1>', self.ctl.add_ware)
        self.tk_button_lxhngyvd.bind('<Button-1>', self.ctl.fenpei)
        self.tk_button_lxhnhabn.bind('<Button-1>', self.ctl.back)
        pass

    def __style_config(self):
        sty = Style()
        sty.configure(self.new_style(self.tk_button_lxhnghg6), font=("微软雅黑", -12))
        sty.configure(self.new_style(self.tk_button_lxhngntl), font=("微软雅黑", -12))
        sty.configure(self.new_style(self.tk_button_lxhngsww), font=("微软雅黑", -12))
        sty.configure(self.new_style(self.tk_button_lxhngyvd), font=("微软雅黑", -12))
        sty.configure(self.new_style(self.tk_button_lxhnhabn), font=("微软雅黑", -12))
        pass


if __name__ == "__main__":
    win = WinGUI()
    win.mainloop()