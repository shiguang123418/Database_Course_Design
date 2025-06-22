"""
本代码由[Tkinter布局助手]生成
官网:https://www.pytk.net
QQ交流群:905019785
在线反馈:https://support.qq.com/product/618914
"""
import pymysql
from UI.product_munu_ui import Win
from Control import product_munu_control
from tkinter.messagebox import showinfo
class Controller:
    # 导入UI类后，替换以下的 object 类型，将获得 IDE 属性提示功能
    ui: object
    def __init__(self):
        pass
    def init(self, ui):
        self.ui = ui
        # TODO 组件初始化 赋值操作
    def add_product(self,evt):
        id=self.ui.tk_input_lxa2ltv6.get()
        name=self.ui.tk_input_lxa2nm2j.get()
        type=self.ui.tk_input_lxa2nn7g.get()
        price=self.ui.tk_input_lxa2nogl.get()
        cost=self.ui.tk_input_lxa2np4y.get()
        number=self.ui.tk_input_lxa2ntnd.get()
        Sales=self.ui.tk_input_lxa2mi9s.get()
        plan=self.ui.tk_input_lxa2nuik.get()
        try:
            coon = pymysql.connect(host="127.0.0.1", user="root",password="082415", database="y3")
            cursor = coon.cursor()

            sql="insert into goods(商品编号,商品名称,规格型号,销售价格,进货价格,库存量,销量,计划库存量) values(%s,%s,%s,%s,%s,%s,%s,%s)"
            data=[id,name,type,price,cost,number,Sales,plan]
            cursor.execute(sql, data)
            # 提交事务
            coon.commit()
            # 关闭游标和数据库连接
            cursor.close()
            coon.close()
            showinfo(title="提示", message="添加成功")
            self.ui.destroy()  # 关闭窗口
            win = Win(product_munu_control.Controller())
            win.mainloop()
        except:
            showinfo(title="提示", message="添加失败")

    def back(self,evt):
        self.ui.destroy()  # 关闭窗口
        win = Win(product_munu_control.Controller())
        win.mainloop()
