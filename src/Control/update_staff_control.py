"""
本代码由[Tkinter布局助手]生成
官网:https://www.pytk.net
QQ交流群:905019785
在线反馈:https://support.qq.com/product/618914
"""
from decimal import Decimal

import pymysql

from UI import update_staff_ui
import update_product_ui
from UI.menu_ui import Win
from UI.update_product_ui import Win as win
from Control import menu_control
from tkinter.messagebox import showinfo
from Control import staff_ware_control
from UI import staff_ware_menu
global id
class Controller:
    # 导入UI类后，替换以下的 object 类型，将获得 IDE 属性提示功能
    ui: win
    def __init__(self):
        pass
    def init(self, ui):
        self.ui = ui
        # TODO 组件初始化 赋值操作
        coon = pymysql.connect(host="127.0.0.1", user="root", password="082415", database="y3")
        cursor = coon.cursor()
        sql = f"SELECT * FROM staff WHERE 员工编号 = {id}"
        cursor.execute(sql)
        product_data = cursor.fetchall()[0]
        self.ui.tk_input_lxa2ltv6.insert(0, product_data[0])
        self.ui.tk_input_lxa2mi9s.insert(0, product_data[1])
        self.ui.tk_input_lxa2nm2j.insert(0, product_data[2])
        self.ui.tk_input_lxa2nn7g.insert(0, product_data[3])
        self.ui.tk_input_lxa2nogl.insert(0, product_data[4])
        self.ui.tk_input_lxa2np4y.insert(0, product_data[5])
        self.ui.tk_input_lxa2ntnd.insert(0, product_data[6])
        self.ui.tk_input_lxa2nuik.insert(0, product_data[7])
        self.ui.tk_input_lxa2nv8j.insert(0, product_data[8])
    def y1(self,evt):
        global id
        id = evt
        self.ui = update_staff_ui.Win(Controller())
        self.ui.mainloop()
    def update_product(self,evt):
        # 创建数据库连接
        try:
            id = self.ui.tk_input_lxa2ltv6.get()
            name = self.ui.tk_input_lxa2mi9s.get()
            type = self.ui.tk_input_lxa2nm2j.get()
            price = self.ui.tk_input_lxa2nn7g.get()
            cost = self.ui.tk_input_lxa2nogl.get()
            number = self.ui.tk_input_lxa2np4y.get()
            Sales = self.ui.tk_input_lxa2ntnd.get()
            plan = self.ui.tk_input_lxa2nuik.get()
            supplierid = self.ui.tk_input_lxa2nv8j.get()
            print(id,name,type,price,cost,number,Sales,plan,supplierid)
            coon = pymysql.connect(host="127.0.0.1", user="root",password="082415", database="y3")
            cursor = coon.cursor()
            sql="update staff set 员工姓名=%s,员工性别=%s,员工年龄=%s,员工工龄=%s,身份证号码=%s,联系电话=%s,入职日期=%s,工资=%s where 员工编号=%s"
            data=(name,type,price,cost,number,Sales,plan,supplierid,id)
            cursor.execute(sql, data)
            # 提交事务
            coon.commit()
            # 关闭游标和数据库连接
            cursor.close()
            coon.close()
            showinfo(title="提示", message="修改成功")
            self.ui.destroy()  # 关闭窗口
            win = Win(menu_control.Controller())
            win.mainloop()
        except:
            showinfo(title="提示", message="修改失败")
            pass
    def back(self,evt):
        self.ui.destroy()  # 关闭窗口
        win = staff_ware_menu.Win(staff_ware_control.Controller())
        win.mainloop()
