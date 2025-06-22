"""
本代码由[Tkinter布局助手]生成
官网:https://www.pytk.net
QQ交流群:905019785
在线反馈:https://support.qq.com/product/618914
"""
# 示例下载 https://www.pytk.net/blog/1702564569.html
from UI import menu_ui
from Control import menu_control
from UI import add_vip_ui
from Control import add_vip_control
from UI import add_money_ui
from UI import login_vip_ui
from Control import add_money_control
from UI import check_money_ui
from UI import infer_ui
from UI import check_trade_ui
from UI import check_infer_ui
from Control import check_money_control
from Control import login_vip_control
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
    def add_vip(self,evt):
        self.ui.destroy()
        win=add_vip_ui.Win(add_vip_control.Controller())
        win.mainloop()
    def back(self,evt):
        self.ui.destroy()
        win=menu_ui.Win(menu_control.Controller())
        win.mainloop()
    def add_money(self,evt):
        self.ui.destroy()
        win=add_money_ui.Win(add_money_control.Controller())
        win.mainloop()
    def check_money(self,evt):
        self.ui.destroy()
        win=check_money_ui.Win(check_money_control.Controller())
        win.mainloop()
    def shopping(self, evt):
        self.ui.destroy()
        win = login_vip_ui.Win(login_vip_control.Controller())
        win.mainloop()
    def infer(self, evt):
        self.ui.destroy()
        app = infer_ui.RefundApp()
        app.mainloop()
    def check_infer(self, evt):
        self.ui.destroy()
        class Controller1:
            def init(self, view):
                pass

            def product_menu(self, event):
                pass

            def vip_menu(self, event):
                pass

            def staff_menu(self, event):
                pass
        refund_page = check_infer_ui.RefundPage(Controller1())
        refund_page.mainloop()
    def check_trade(self, evt):
        self.ui.destroy()
        class Controller1:
            def init(self, view):
                pass

            def product_menu(self, event):
                pass

            def vip_menu(self, event):
                pass

            def staff_menu(self, event):
                pass
        refund_page = check_trade_ui.RefundPage(Controller1())
        refund_page.mainloop()



