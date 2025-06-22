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
        self.tk_label_lx06b9ro = self.__tk_label_lx06b9ro(self)
        self.tk_frame_lxa2lhyp = self.__tk_frame_lxa2lhyp(self)
        self.tk_label_lxa2lnn7 = self.__tk_label_lxa2lnn7( self.tk_frame_lxa2lhyp)
        self.tk_input_lxa2ltv6 = self.__tk_input_lxa2ltv6( self.tk_frame_lxa2lhyp)
        self.tk_frame_lxa2nm2h = self.__tk_frame_lxa2nm2h(self)
        self.tk_label_lxa2nm2i = self.__tk_label_lxa2nm2i( self.tk_frame_lxa2nm2h)
        self.tk_input_lxa2nm2j = self.__tk_input_lxa2nm2j( self.tk_frame_lxa2nm2h)
        self.tk_frame_lxa2nn7e = self.__tk_frame_lxa2nn7e(self)
        self.tk_label_lxa2nn7f = self.__tk_label_lxa2nn7f( self.tk_frame_lxa2nn7e)
        self.tk_input_lxa2nn7g = self.__tk_input_lxa2nn7g( self.tk_frame_lxa2nn7e)
        self.tk_frame_lxa2nogj = self.__tk_frame_lxa2nogj(self)
        self.tk_label_lxa2nogk = self.__tk_label_lxa2nogk( self.tk_frame_lxa2nogj)
        self.tk_input_lxa2nogl = self.__tk_input_lxa2nogl( self.tk_frame_lxa2nogj)
        self.tk_frame_lxa2np4w = self.__tk_frame_lxa2np4w(self)
        self.tk_label_lxa2np4x = self.__tk_label_lxa2np4x( self.tk_frame_lxa2np4w)
        self.tk_input_lxa2np4y = self.__tk_input_lxa2np4y( self.tk_frame_lxa2np4w)
        self.tk_button_lxa2vxyp = self.__tk_button_lxa2vxyp(self)
        self.tk_button_lxa2vyvl = self.__tk_button_lxa2vyvl(self)
        self.tk_frame_lxgc83sb = self.__tk_frame_lxgc83sb(self)
        self.tk_label_lxgc83sc = self.__tk_label_lxgc83sc( self.tk_frame_lxgc83sb)
        self.tk_input_lxgc83sd = self.__tk_input_lxgc83sd( self.tk_frame_lxgc83sb)
    def __win(self):
        self.title("Tkinter布局助手")
        # 设置窗口大小、居中
        width = 600
        height = 550
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
    def __tk_label_lx06b9ro(self,parent):
        label = Label(parent,text="添加商品信息",anchor="center", bootstyle="default")
        label.place(x=0, y=0, width=599, height=40)
        return label
    def __tk_frame_lxa2lhyp(self,parent):
        frame = Frame(parent,bootstyle="default")
        frame.place(x=40, y=75, width=549, height=42)
        return frame
    def __tk_label_lxa2lnn7(self,parent):
        label = Label(parent,text="请确定会员号：",anchor="center", bootstyle="default")
        label.place(x=20, y=7, width=146, height=30)
        return label
    def __tk_input_lxa2ltv6(self,parent):
        ipt = Entry(parent, bootstyle="default")
        ipt.place(x=177, y=7, width=357, height=30)
        return ipt
    def __tk_frame_lxa2nm2h(self,parent):
        frame = Frame(parent,bootstyle="default")
        frame.place(x=40, y=138, width=549, height=42)
        return frame
    def __tk_label_lxa2nm2i(self,parent):
        label = Label(parent,text="请输入名称：",anchor="center", bootstyle="default")
        label.place(x=20, y=5, width=146, height=30)
        return label
    def __tk_input_lxa2nm2j(self,parent):
        ipt = Entry(parent, bootstyle="default")
        ipt.place(x=177, y=7, width=357, height=30)
        return ipt
    def __tk_frame_lxa2nn7e(self,parent):
        frame = Frame(parent,bootstyle="default")
        frame.place(x=40, y=199, width=549, height=42)
        return frame
    def __tk_label_lxa2nn7f(self,parent):
        label = Label(parent,text="请输入性别：",anchor="center", bootstyle="default")
        label.place(x=20, y=7, width=146, height=30)
        return label
    def __tk_input_lxa2nn7g(self,parent):
        ipt = Entry(parent, bootstyle="default")
        ipt.place(x=177, y=7, width=357, height=30)
        return ipt
    def __tk_frame_lxa2nogj(self,parent):
        frame = Frame(parent,bootstyle="default")
        frame.place(x=40, y=260, width=549, height=42)
        return frame
    def __tk_label_lxa2nogk(self,parent):
        label = Label(parent,text="请输入电话：",anchor="center", bootstyle="default")
        label.place(x=20, y=7, width=146, height=30)
        return label
    def __tk_input_lxa2nogl(self,parent):
        ipt = Entry(parent, bootstyle="default")
        ipt.place(x=177, y=7, width=357, height=30)
        return ipt
    def __tk_frame_lxa2np4w(self,parent):
        frame = Frame(parent,bootstyle="default")
        frame.place(x=40, y=326, width=549, height=42)
        return frame
    def __tk_label_lxa2np4x(self,parent):
        label = Label(parent,text="请输入注册日期：",anchor="center", bootstyle="default")
        label.place(x=20, y=7, width=146, height=30)
        return label
    def __tk_input_lxa2np4y(self,parent):
        ipt = Entry(parent, bootstyle="default")
        ipt.place(x=177, y=7, width=357, height=30)
        return ipt
    def __tk_button_lxa2vxyp(self,parent):
        btn = Button(parent, text="添加", takefocus=False,bootstyle="default")
        btn.place(x=103, y=461, width=100, height=50)
        return btn
    def __tk_button_lxa2vyvl(self,parent):
        btn = Button(parent, text="取消", takefocus=False,bootstyle="default")
        btn.place(x=424, y=460, width=100, height=50)
        return btn
    def __tk_frame_lxgc83sb(self,parent):
        frame = Frame(parent,bootstyle="default")
        frame.place(x=40, y=393, width=549, height=42)
        return frame
    def __tk_label_lxgc83sc(self,parent):
        label = Label(parent,text="请输入密码：",anchor="center", bootstyle="default")
        label.place(x=20, y=7, width=146, height=30)
        return label
    def __tk_input_lxgc83sd(self,parent):
        ipt = Entry(parent, bootstyle="default",show="*")
        ipt.place(x=177, y=7, width=357, height=30)
        return ipt
class Win(WinGUI):
    def __init__(self, controller):
        self.ctl = controller
        super().__init__()
        self.__event_bind()
        self.__style_config()
        self.ctl.init(self)
    def __event_bind(self):
        self.tk_button_lxa2vxyp.bind('<Button-1>',self.ctl.add_vip)
        self.tk_button_lxa2vyvl.bind('<Button-1>',self.ctl.back)
        pass
    def __style_config(self):
        sty = Style()
        sty.configure(self.new_style(self.tk_label_lx06b9ro),font=("宋体",-19))
        sty.configure(self.new_style(self.tk_label_lxa2lnn7),font=("微软雅黑",-12))
        sty.configure(self.new_style(self.tk_label_lxa2nm2i),font=("微软雅黑",-12))
        sty.configure(self.new_style(self.tk_label_lxa2nn7f),font=("微软雅黑",-12))
        sty.configure(self.new_style(self.tk_label_lxa2nogk),font=("微软雅黑",-12))
        sty.configure(self.new_style(self.tk_label_lxa2np4x),font=("微软雅黑",-12))
        sty.configure(self.new_style(self.tk_button_lxa2vxyp),font=("微软雅黑",-12))
        sty.configure(self.new_style(self.tk_button_lxa2vyvl),font=("微软雅黑",-12))
        sty.configure(self.new_style(self.tk_label_lxgc83sc),font=("微软雅黑",-12))
        pass
if __name__ == "__main__":
    win = WinGUI()
    win.mainloop()