"""
本代码由[Tkinter布局助手]生成
官网:https://www.pytk.net
QQ交流群:905019785
在线反馈:https://support.qq.com/product/618914
"""
from tkinter.messagebox import showinfo

# 示例下载 https://www.pytk.net/blog/1702564569.html
from UI import vip_menu_ui
from Control import vip_menu_control
import pymysql

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
    def back(self,evt):
        self.ui.destroy()  # 关闭窗口
        win = vip_menu_ui.Win(vip_menu_control.Controller())
        win.mainloop()
    def add(self,evt):
        try:
            id=self.ui.tk_input_lxoc4om6.get()
            money=self.ui.tk_input_lxoc52as.get()
            coon = pymysql.connect(host="127.0.0.1", user="root",password="082415", database="y3")
            cursor = coon.cursor()
            sql = "update member set 余额=余额+%s where 会员卡卡号=%s"
            data = (money,id)
            cursor.execute(sql, data)
            # 提交事务
            coon.commit()
            # 关闭游标和数据库连接
            sql = f"SELECT 余额 FROM member WHERE 会员卡卡号 = {id}"
            cursor.execute(sql)
            product_data = cursor.fetchall()[0][0]
            cursor.close()
            coon.close()
            showinfo(title="提示", message=f"充值成功,余额剩余{product_data}")
        except:
            showinfo(title="提示", message="充值失败")