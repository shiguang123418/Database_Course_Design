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
        self.tk_button_lxa2vyvl = self.__tk_button_lxa2vyvl(self)
        self.tk_button_lxhlyqpp = self.__tk_button_lxhlyqpp(self)
        self.tk_button_lxhlys8s = self.__tk_button_lxhlys8s(self)
        self.tk_button_lxhm3nf7 = self.__tk_button_lxhm3nf7(self)
        self.tk_button_lxhm3o8d = self.__tk_button_lxhm3o8d(self)
        self.tk_button_lxhm48lq = self.__tk_button_lxhm48lq(self)
        self.tk_button_lxohgu8j = self.__tk_button_lxohgu8j(self)
    def __win(self):
        self.title("Tkinter布局助手")
        # 设置窗口大小、居中
        width = 600
        height = 400
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
    def __tk_button_lxa2vyvl(self,parent):
        btn = Button(parent, text="取消", takefocus=False,bootstyle="default")
        btn.place(x=200, y=307, width=184, height=50)
        return btn
    def __tk_button_lxhlyqpp(self,parent):
        btn = Button(parent, text="添加商品", takefocus=False,bootstyle="default")
        btn.place(x=0, y=22, width=184, height=60)
        return btn
    def __tk_button_lxhlys8s(self,parent):
        btn = Button(parent, text="添加入库单", takefocus=False,bootstyle="default")
        btn.place(x=222, y=19, width=186, height=60)
        return btn
    def __tk_button_lxhm3nf7(self,parent):
        btn = Button(parent, text="修改商品", takefocus=False,bootstyle="default")
        btn.place(x=0, y=117, width=184, height=60)
        return btn
    def __tk_button_lxhm3o8d(self,parent):
        btn = Button(parent, text="删除商品", takefocus=False,bootstyle="default")
        btn.place(x=0, y=223, width=186, height=60)
        return btn
    def __tk_button_lxhm48lq(self,parent):
        btn = Button(parent, text="查询供应商", takefocus=False,bootstyle="default")
        btn.place(x=226, y=118, width=181, height=59)
        return btn
    def __tk_button_lxohgu8j(self,parent):
        btn = Button(parent, text="添加供应商", takefocus=False,bootstyle="default")
        btn.place(x=226, y=220, width=181, height=59)
        return btn
class Win(WinGUI):
    def __init__(self, controller):
        self.ctl = controller
        super().__init__()
        self.__event_bind()
        self.__style_config()
        self.ctl.init(self)
    def __event_bind(self):
        self.tk_button_lxa2vyvl.bind('<Button-1>',self.ctl.back)
        self.tk_button_lxhlyqpp.bind('<Button-1>',self.ctl.add_product)
        self.tk_button_lxhlys8s.bind('<Button-1>',self.ctl.add_entry)
        self.tk_button_lxhm3nf7.bind('<Button-1>',self.ctl.update_product)
        self.tk_button_lxhm3o8d.bind('<Button-1>',self.ctl.del_product)
        self.tk_button_lxhm48lq.bind('<Button-1>',self.ctl.check_vender)
        self.tk_button_lxohgu8j.bind('<Button-1>',self.ctl.add_vendor)
        pass
    def __style_config(self):
        sty = Style()
        sty.configure(self.new_style(self.tk_button_lxa2vyvl),font=("微软雅黑",-12))
        sty.configure(self.new_style(self.tk_button_lxhlyqpp),font=("微软雅黑",-12))
        sty.configure(self.new_style(self.tk_button_lxhlys8s),font=("微软雅黑",-12))
        sty.configure(self.new_style(self.tk_button_lxhm3nf7),font=("微软雅黑",-12))
        sty.configure(self.new_style(self.tk_button_lxhm3o8d),font=("微软雅黑",-12))
        sty.configure(self.new_style(self.tk_button_lxhm48lq),font=("微软雅黑",-12))
        sty.configure(self.new_style(self.tk_button_lxohgu8j),font=("微软雅黑",-12))
        pass
if __name__ == "__main__":
    win = WinGUI()
    win.mainloop()