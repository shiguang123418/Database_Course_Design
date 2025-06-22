"""
本代码由[Tkinter布局助手]生成
官网:https://www.pytk.net
QQ交流群:905019785
在线反馈:https://support.qq.com/product/618914
"""
# 示例下载 https://www.pytk.net/blog/1702564569.html
from UI import add_staff_ui
from UI import update_staff_ui1
from UI import add_ware_ui
from UI import menu_ui
from UI import fenpei_ui
from Control import add_staff_control
from Control import update_staff_control1
from Control import menu_control
from Control import fenpei_control
class Controller:
    # 导入UI类后，替换以下的 object 类型，将获得 IDE 属性提示功能
    ui: object
    def __init__(self):
        pass
    def init(self, ui):
        """
        得到UI实例，对组件进行初始化配置
        """
        self.ui = ui
        # TODO 组件初始化 赋值操作
    def add_staff(self,evt):
        self.ui.destroy()
        win=add_staff_ui.EmployeeAddApp()
    def update_staff(self,evt):
        self.ui.destroy()
        win=update_staff_ui1.Win(update_staff_control1.Controller())
        win.mainloop()
    def add_ware(self,evt):
        self.ui.destroy()
        win = add_ware_ui.EmployeeAddApp()
    def fenpei(self,evt):
        self.ui.destroy()
        win=fenpei_ui.Win(fenpei_control.Controller())
        win.mainloop()
    def back(self,evt):
        self.ui.destroy()
        win=menu_ui.Win(menu_control.Controller())
        win.mainloop()

