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
        self.tk_button_lxhnhabn = self.__tk_button_lxhnhabn(self)
        self.tk_label_lxoc4h4j = self.__tk_label_lxoc4h4j(self)
        self.tk_input_lxoc4om6 = self.__tk_input_lxoc4om6(self)
        self.tk_label_lxoc4pzw = self.__tk_label_lxoc4pzw(self)
        self.tk_input_lxoc52as = self.__tk_input_lxoc52as(self)
        self.tk_button_lxoc5a8l = self.__tk_button_lxoc5a8l(self)
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

    def scrollbar_autohide(self,vbar, hbar, widget):
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

    def v_scrollbar(self,vbar, widget, x, y, w, h, pw, ph):
        widget.configure(yscrollcommand=vbar.set)
        vbar.config(command=widget.yview)
        vbar.place(relx=(w + x) / pw, rely=y / ph, relheight=h / ph, anchor='ne')
    def h_scrollbar(self,hbar, widget, x, y, w, h, pw, ph):
        widget.configure(xscrollcommand=hbar.set)
        hbar.config(command=widget.xview)
        hbar.place(relx=x / pw, rely=(y + h) / ph, relwidth=w / pw, anchor='sw')
    def create_bar(self,master, widget,is_vbar,is_hbar, x, y, w, h, pw, ph):
        vbar, hbar = None, None
        if is_vbar:
            vbar = Scrollbar(master)
            self.v_scrollbar(vbar, widget, x, y, w, h, pw, ph)
        if is_hbar:
            hbar = Scrollbar(master, orient="horizontal")
            self.h_scrollbar(hbar, widget, x, y, w, h, pw, ph)
        self.scrollbar_autohide(vbar, hbar, widget)
    def new_style(self,widget):
        ctl = widget.cget('style')
        ctl = "".join(random.sample('0123456789',5)) + "." + ctl
        widget.configure(style=ctl)
        return ctl
    def __tk_button_lxhnhabn(self,parent):
        btn = Button(parent, text="返回", takefocus=False,bootstyle="default")
        btn.place(x=295, y=282, width=125, height=59)
        return btn
    def __tk_label_lxoc4h4j(self,parent):
        label = Label(parent,text="会员卡号",anchor="center", bootstyle="default")
        label.place(x=67, y=46, width=124, height=43)
        return label
    def __tk_input_lxoc4om6(self,parent):
        ipt = Entry(parent, bootstyle="default")
        ipt.place(x=207, y=46, width=216, height=43)
        return ipt
    def __tk_label_lxoc4pzw(self,parent):
        label = Label(parent,text="充值金额",anchor="center", bootstyle="default")
        label.place(x=71, y=154, width=124, height=47)
        return label
    def __tk_input_lxoc52as(self,parent):
        ipt = Entry(parent, bootstyle="default")
        ipt.place(x=206, y=159, width=216, height=43)
        return ipt
    def __tk_button_lxoc5a8l(self,parent):
        btn = Button(parent, text="充值", takefocus=False,bootstyle="default")
        btn.place(x=68, y=282, width=118, height=59)
        return btn
class Win(WinGUI):
    def __init__(self, controller):
        self.ctl = controller
        super().__init__()
        self.__event_bind()
        self.__style_config()
        self.ctl.init(self)
    def __event_bind(self):
        self.tk_button_lxhnhabn.bind('<Button-1>',self.ctl.back)
        self.tk_button_lxoc5a8l.bind('<Button-1>',self.ctl.add)
        pass
    def __style_config(self):
        sty = Style()
        sty.configure(self.new_style(self.tk_button_lxhnhabn),font=("微软雅黑",-12))
        sty.configure(self.new_style(self.tk_label_lxoc4h4j),font=("微软雅黑",-12))
        sty.configure(self.new_style(self.tk_label_lxoc4pzw),font=("微软雅黑",-12))
        sty.configure(self.new_style(self.tk_button_lxoc5a8l),font=("微软雅黑",-12))
        pass
if __name__ == "__main__":
    win = WinGUI()
    win.mainloop()