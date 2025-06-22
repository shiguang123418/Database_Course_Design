"""
本代码由[Tkinter布局助手]生成
官网:https://www.pytk.net
QQ交流群:905019785
在线反馈:https://support.qq.com/product/618914
"""
from Control import update_product_control1
# 示例下载 https://www.pytk.net/blog/1702564569.html
from Control import menu_control
from Control import update_product_control
from UI import update_product_ui
from UI.menu_ui import Win as MainWin
from UI import add_product_ui
from UI import menu_ui
from UI import update_product_ui1
from UI import del_product_ui
from UI import check_supplier_ui
from UI import add_entry
from UI import add_vendor
from Control import add_product_control
from Control import check_supplier_control
from Control import del_product_control
from Control import update_staff_control1
class Controller:
    # 导入UI类后，替换以下的 object 类型，将获得 IDE 属性提示功能
    ui: object
    def __init__(self):
        pass
    def init(self, ui):
        self.ui = ui
    def back(self,evt):
        self.ui.destroy()  # 关闭窗口
        win = menu_ui.Win(menu_control.Controller())
        win.mainloop()
    def add_product(self,evt):
        self.ui.destroy()  # 关闭窗口
        win = add_product_ui.Win(add_product_control.Controller())
        win.mainloop()
    def add_entry(self,evt):
        self.ui.destroy()  # 关闭窗口
        win = add_entry.Win(Controller())
        win.mainloop()
    def update_product(self,evt):
        self.ui.destroy()  # 关闭窗口
        self.ui=update_product_ui1.Win(update_product_control1.Controller())
        self.ui.mainloop()
    def del_product(self,evt):
        self.ui.destroy()  # 关闭窗口
        self.ui=del_product_ui.Win(del_product_control.Controller())
        self.ui.mainloop()
    def check_vender(self,evt):
        self.ui.destroy()  # 关闭窗口
        self.ui=check_supplier_ui.Win(check_supplier_control.Controller())
        self.ui.mainloop()
    def add_vendor(self,evt):
        self.ui.destroy()
        win = add_vendor.Win(Controller())
        win.mainloop()
