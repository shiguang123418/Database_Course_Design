"""
本代码由[Tkinter布局助手]生成
官网:https://www.pytk.net
QQ交流群:905019785
在线反馈:https://support.qq.com/product/618914
"""
from Control import update_staff_control
import update_product_ui1
from tkinter import messagebox
import pymysql
import tkinter as tk
from tkinter.messagebox import showinfo
from Control import menu_control
from Control import update_product_control
from UI import update_product_ui
from UI.menu_ui import Win as MainWin
from UI import update_staff_ui
from Control import staff_ware_control
from UI import staff_ware_menu


class Controller:
    # 导入UI类后，替换以下的 object 类型，将获得 IDE 属性提示功能
    ui: object
    def __init__(self):
        self.id = None
    def init(self, ui):
        """
        得到UI实例，对组件进行初始化配置
        """
        self.ui = ui
        # TODO 组件初始化 赋值操作
    def y1(self,evt):
        id = self.ui.tk_input_lxa2ltv6.get()
        try:
            coon = pymysql.connect(host="127.0.0.1", user="root",password="082415", database="y3")
            cursor = coon.cursor()
            sql = f"SELECT * FROM staff WHERE 员工编号 = {id}"
            cursor.execute(sql)
            # 获取查询结果
            results = cursor.fetchall()
            if results:
                self.ui.destroy()
                update_staff_control.Controller.y1(self,id)
                cursor.close()
                coon.close()
            else:
                messagebox.showinfo(title="提示", message="没有该员工")
            # 关闭游标和数据库连接
        except Exception as e:
            pass
    def back(self,evt):
        self.ui.destroy()  # 关闭窗口
        win = staff_ware_menu.Win(staff_ware_control.Controller())
        win.mainloop()