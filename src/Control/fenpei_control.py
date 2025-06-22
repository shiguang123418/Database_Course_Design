"""
本代码由[Tkinter布局助手]生成
官网:https://www.pytk.net
QQ交流群:905019785
在线反馈:https://support.qq.com/product/618914
"""
from tkinter.messagebox import showinfo

import pymysql
from UI import staff_ware_menu
from Control import staff_ware_control
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
    def fenpei(self,evt):
        id1=self.ui.tk_select_box_lxg72jwe.get()
        id2=self.ui.tk_select_box_lxg72wwf.get()

        db=pymysql.connect(host='127.0.0.1',user='y2',password='082415',database='y3')
        cursor=db.cursor()
        try:
            sql2="Update ware SET 仓库管理员编号=%s WHERE 仓库编号=%s"
            data2=(id1,id2)
            cursor.execute(sql2,data2)
            db.commit()
            sql1= 'UPDATE staff SET 仓库管理员编号=%s,仓库编号=%s WHERE 员工编号=%s'
            data1=(id1,id2,id1)
            cursor.execute(sql1, data1)
            db.commit()
            showinfo(title="提示", message=f"分配成功,已将仓库编号为{id2}的仓库管理员编号更改为{id1}")
        except:
            showinfo(title="提示", message="分配失败")

    def back(self,evt):
        self.ui.destroy()
        self.ui=staff_ware_menu.Win(staff_ware_control.Controller())
        self.ui.mainloop()


