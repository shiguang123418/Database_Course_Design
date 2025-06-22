from tkinter import *
from tkinter.ttk import *
from ttkbootstrap import *
import random
import pymysql
from UI import vip_menu_ui
from Control import vip_menu_control

#UI和方法一体
class RefundPage(Window):
    def __init__(self, controller):
        super().__init__(themename="cosmo", hdpi=False)
        self.ctl = controller
        self.__win()
        self.__create_widgets()
        self.__style_config()
        self.__populate_data()

    def __win(self):
        self.title("退货信息")
        # 设置窗口大小、居中
        width = 1000
        height = 500
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) // 2, (screenheight - height) // 2)
        self.geometry(geometry)
        self.minsize(width=width, height=height)

    def __create_widgets(self):
        # 标题
        self.tk_label_title = Label(self, text="退货信息", anchor="center", bootstyle="default inverse")
        self.tk_label_title.place(relx=0.5, rely=0.05, anchor='center')

        # 表格
        columns = ('交易流水号', '商品编号', '退货数量', '退款金额', '退货日期')
        self.tree = Treeview(self, columns=columns, show='headings')
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor='center')
        self.tree.place(relx=0.5, rely=0.5, anchor='center', relwidth=0.9, relheight=0.7)

        # 返回按钮
        self.btn_back = Button(self, text="返回", command=self.back, bootstyle="secondary")
        self.btn_back.place(relx=0.5, rely=0.9, anchor='center', relwidth=0.2, relheight=0.08)

    def get_refund_data(self):
        try:
            connection = pymysql.connect(host="127.0.0.1", user="root", password="082415", database="y3")
            query = "SELECT * FROM infer"
            cursor = connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            connection.close()
            return result

        except pymysql.Error as err:
            print(f"Error: {err}")
            return []

    def __populate_data(self):
        data = self.get_refund_data()
        for item in data:
            self.tree.insert('', 'end', values=item)
        try:
            for col in self.tree['columns']:
                self.tree.heading(col, text=col, anchor='center')
                max_width = max([len(str(item[0])) for item in data]) + 20  # Add padding
                self.tree.column(col, width=max_width)
        except:
            pass

    def __style_config(self):
        sty = Style()
        sty.configure(self.new_style(self.tk_label_title), font=("微软雅黑", 24, "bold"))
        sty.configure(self.new_style(self.btn_back), font=("微软雅黑", -12))

    def new_style(self, widget):
        ctl = widget.cget('style')
        ctl = "".join(random.sample('0123456789', 5)) + "." + ctl
        widget.configure(style=ctl)
        return ctl

    def back(self):
        self.destroy()
        main_win = vip_menu_ui.Win(vip_menu_control.Controller())
        main_win.mainloop()

if __name__ == "__main__":
    class Controller:
        def init(self, view):
            pass
        def product_menu(self, event):
            pass
        def vip_menu(self, event):
            pass
        def staff_menu(self, event):
            pass
    refund_page = RefundPage(Controller())
    refund_page.mainloop()
