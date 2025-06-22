"""
本代码由[Tkinter布局助手]生成
官网:https://www.pytk.net
QQ交流群:905019785
在线反馈:https://support.qq.com/product/618914
"""
from tkinter import messagebox
import pymysql
import tkinter as tk
from tkinter.messagebox import showinfo
from Control import menu_control
from UI.menu_ui import Win
from Control import product_munu_control
from UI import product_munu_ui
# 示例下载 https://www.pytk.net/blog/1702564569.html
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
    def y1(self,evt):
        id = self.ui.tk_input_lxa2ltv6.get()
        try:
            coon = pymysql.connect(host="127.0.0.1", user="root",password="082415", database="y3")
            cursor = coon.cursor()
            sql = f"SELECT * FROM goods WHERE 商品编号 = {id}"
            cursor.execute(sql)
            # 获取查询结果
            results = cursor.fetchall()[0][8]

            messagebox.showinfo(title="提示", message=f"该商品的供应商编号为:{results}")
            # 关闭游标和数据库连接
            cursor.close()
            coon.close()
        except:
            showinfo(title="提示", message="没有该商品")
    def back(self,evt):
        self.ui.destroy()  # 关闭窗口
        win = product_munu_ui.Win(product_munu_control.Controller())
        win.mainloop()