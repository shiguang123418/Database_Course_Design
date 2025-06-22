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
        self.tk_button_lxhn6298 = self.__tk_button_lxhn6298(self)
        self.tk_button_lxhn7h5p = self.__tk_button_lxhn7h5p(self)
        self.tk_button_lxoe198x = self.__tk_button_lxoe198x(self)
        self.tk_button_lxoe1azh = self.__tk_button_lxoe1azh(self)
        self.tk_button_lxoe1cl4 = self.__tk_button_lxoe1cl4(self)
        self.tk_button_lxoe1gj0 = self.__tk_button_lxoe1gj0(self)
        self.tk_button_lxoe2p58 = self.__tk_button_lxoe2p58(self)
        self.tk_button_lxoe3dee = self.__tk_button_lxoe3dee(self)
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
    def __tk_button_lxhn6298(self,parent):
        btn = Button(parent, text="添加会员", takefocus=False,bootstyle="default")
        btn.place(x=0, y=41, width=153, height=51)
        return btn
    def __tk_button_lxhn7h5p(self,parent):
        btn = Button(parent, text="返回", takefocus=False,bootstyle="default")
        btn.place(x=208, y=340, width=153, height=51)
        return btn
    def __tk_button_lxoe198x(self,parent):
        btn = Button(parent, text="余额充值", takefocus=False,bootstyle="default")
        btn.place(x=0, y=142, width=153, height=51)
        return btn
    def __tk_button_lxoe1azh(self,parent):
        btn = Button(parent, text="余额查询", takefocus=False,bootstyle="default")
        btn.place(x=0, y=239, width=153, height=51)
        return btn
    def __tk_button_lxoe1cl4(self,parent):
        btn = Button(parent, text="购物", takefocus=False,bootstyle="default")
        btn.place(x=182, y=42, width=153, height=51)
        return btn
    def __tk_button_lxoe1gj0(self,parent):
        btn = Button(parent, text="申请退款", takefocus=False,bootstyle="default")
        btn.place(x=181, y=143, width=157, height=53)
        return btn
    def __tk_button_lxoe2p58(self,parent):
        btn = Button(parent, text="查看退货信息", takefocus=False,bootstyle="default")
        btn.place(x=181, y=242, width=154, height=51)
        return btn
    def __tk_button_lxoe3dee(self,parent):
        btn = Button(parent, text="查看交易记录", takefocus=False,bootstyle="default")
        btn.place(x=378, y=46, width=153, height=51)
        return btn
class Win(WinGUI):
    def __init__(self, controller):
        self.ctl = controller
        super().__init__()
        self.__event_bind()
        self.__style_config()
        self.ctl.init(self)
    def __event_bind(self):
        self.tk_button_lxhn6298.bind('<Button-1>',self.ctl.add_vip)
        self.tk_button_lxhn7h5p.bind('<Button-1>',self.ctl.back)
        self.tk_button_lxoe198x.bind('<Button-1>',self.ctl.add_money)
        self.tk_button_lxoe1azh.bind('<Button-1>',self.ctl.check_money)
        self.tk_button_lxoe1cl4.bind('<Button-1>',self.ctl.shopping)
        self.tk_button_lxoe1gj0.bind('<Button-1>',self.ctl.infer)
        self.tk_button_lxoe2p58.bind('<Button-1>',self.ctl.check_infer)
        self.tk_button_lxoe3dee.bind('<Button-1>',self.ctl.check_trade)
        pass
    def __style_config(self):
        sty = Style()
        sty.configure(self.new_style(self.tk_button_lxhn6298),font=("微软雅黑",-12))
        sty.configure(self.new_style(self.tk_button_lxhn7h5p),font=("微软雅黑",-12))
        sty.configure(self.new_style(self.tk_button_lxoe198x),font=("微软雅黑",-12))
        sty.configure(self.new_style(self.tk_button_lxoe1azh),font=("微软雅黑",-12))
        sty.configure(self.new_style(self.tk_button_lxoe1cl4),font=("微软雅黑",-12))
        sty.configure(self.new_style(self.tk_button_lxoe1gj0),font=("微软雅黑",-12))
        sty.configure(self.new_style(self.tk_button_lxoe2p58),font=("微软雅黑",-12))
        sty.configure(self.new_style(self.tk_button_lxoe3dee),font=("微软雅黑",-12))
        pass
if __name__ == "__main__":
    win = WinGUI()
    win.mainloop()