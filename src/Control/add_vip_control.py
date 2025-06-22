"""
本代码由[Tkinter布局助手]生成
官网:https://www.pytk.net
QQ交流群:905019785
在线反馈:https://support.qq.com/product/618914
"""
import datetime
from tkinter.messagebox import showinfo

import menu_ui
# 示例下载 https://www.pytk.net/blog/1702564569.html
from UI.menu_ui import Win
from Control import menu_control
import pymysql
from UI import vip_menu_ui
from Control import vip_menu_control
class Controller:
    # 导入UI类后，替换以下的 object 类型，将获得 IDE 属性提示功能
    ui: object
    def __init__(self):
        pass
    def y1(self):
        coon = pymysql.connect(host="127.0.0.1", user="root", password="082415", database="y3")
        cursor = coon.cursor()
        sql = f"SELECT * FROM member"
        cursor.execute(sql)
        # 获取查询结果
        results = "20000"+str(len(cursor.fetchall())+1)
        self.ui.tk_input_lxa2ltv6.insert(0,results)
        s=str(datetime.datetime.today()).split()[0]
        self.ui.tk_input_lxa2np4y.insert(0,s)
    def init(self, ui):
        """
        得到UI实例，对组件进行初始化配置
        """
        self.ui = ui
        self.y1()
        # TODO 组件初始化 赋值操作
    def add_vip(self,evt):
        id=int(self.ui.tk_input_lxa2ltv6.get())
        name=self.ui.tk_input_lxa2nm2j.get()
        sex=self.ui.tk_input_lxa2nn7g.get()
        phone=self.ui.tk_input_lxa2nogl.get()
        data=self.ui.tk_input_lxa2np4y.get()
        pwd=self.ui.tk_input_lxgc83sd.get()
        try:
            coon = pymysql.connect(host="127.0.0.1", user="root", password="082415", database="y3")
            cursor = coon.cursor()
            sql = "insert into member(会员卡卡号,会员姓名,性别,电话,注册日期,会员密码) values(%s,%s,%s,%s,%s,%s)"
            data = [id, name, sex, phone, data,pwd]
            cursor.execute(sql, data)
            # 提交事务
            coon.commit()
            # 关闭游标和数据库连接
            cursor.close()
            coon.close()
            showinfo(title="提示", message="添加成功")
            self.ui.destroy()  # 关闭窗口
            win = Win(menu_control.Controller())
            win.mainloop()
        except:
            showinfo(title="提示", message="添加失败")
    def back(self,evt):
        self.ui.destroy()  # 关闭窗口
        win=vip_menu_ui.Win(vip_menu_control.Controller())
        win.mainloop()
