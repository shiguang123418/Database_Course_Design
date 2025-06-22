"""
本代码由[Tkinter布局助手]生成
官网:https://www.pytk.net
QQ交流群:905019785
在线反馈:https://support.qq.com/product/618914
"""
import product_munu_control
# 示例下载 https://www.pytk.net/blog/1702564569.html
from UI import product_munu_ui
from UI import menu_ui
from tkinter import *
from tkinter.ttk import *
from ttkbootstrap import *
from pytkUI.widgets import *
from UI import vip_menu_ui
from UI import staff_ware_menu
from UI import login_vip_ui
from Control import vip_menu_control
from Control import staff_ware_control
from Control import login_vip_control
class Controller:
    # 导入UI类后，替换以下的 object 类型，将获得 IDE 属性提示功能
    ui: menu_ui
    def __init__(self):
        pass
    def init(self, ui):
        self.ui = ui
        # TODO 组件初始化 赋值操作
    def product_menu(self,evt):
        self.ui.destroy()

        win=product_munu_ui.Win(product_munu_control.Controller())
        win.mainloop()
    def vip_menu(self,evt):
        self.ui.destroy()
        win=vip_menu_ui.Win(vip_menu_control.Controller())
        win.mainloop()
    def staff_menu(self,evt):
        self.ui.destroy()
        win=staff_ware_menu.Win(staff_ware_control.Controller())
        win.mainloop()


