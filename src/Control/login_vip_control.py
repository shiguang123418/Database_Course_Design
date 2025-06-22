import tkinter as tk
from datetime import datetime
from tkinter import messagebox
import pymysql
from UI import menu_ui
from UI import vip_menu_ui
from Control import menu_control
from Control import vip_menu_control
class Controller:
    ui: object
    def __init__(self):
        pass

    def init(self, ui):
        self.ui = ui

    def login(self, evt):
        username = self.ui.tk_input_lxa2nn7g.get()
        password = self.ui.tk_input_lxa2nogl.get()
        if self.validate_credentials(username, password):
            messagebox.showinfo("登录成功", "欢迎回来！")
            self.ui.destroy()  # 关闭窗口
            root = tk.Tk()
            app = ShoppingApp(root, username)  # 传递会员卡卡号
            root.mainloop()
        else:
            messagebox.showerror("错误", "用户名不存在或密码错误！")

    def validate_credentials(self, username, password):
        conn = pymysql.connect(host='127.0.0.1', user='y2', password='082415', database='y3')
        cursor = conn.cursor()
        query = "SELECT * FROM member WHERE 会员卡卡号=%s AND 会员密码=%s"
        cursor.execute(query, (username, password))
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return bool(result)

    def back(self, evt):
        self.ui.destroy()
        win = vip_menu_ui.Win(vip_menu_control.Controller())
        win.mainloop()


class ShoppingApp:
    def __init__(self, root, member_id):
        self.root = root
        self.root.title("购物页面")
        self.products = {}
        self.member_id = member_id  # 接收会员卡卡号
        self.create_widgets()
        self.load_products()

    def create_widgets(self):
        # # 设置窗口的大小和背景颜色
        width = 600
        height = 500
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        # self.geometry(geometry)
        self.root.geometry(geometry)
        self.root.config(bg="white")
        # self.minsize(width=width, height=height)

        # 产品列表框架
        self.product_frame = tk.Frame(self.root, bg="white")
        self.product_frame.pack(fill=tk.BOTH, expand=1, padx=20, pady=20)

        self.product_listbox = tk.Listbox(self.product_frame, font=("Arial", 12), bg="lightgrey")
        self.product_listbox.pack(fill=tk.BOTH, expand=1)

        # 底部框架
        self.bottom_frame = tk.Frame(self.root, bg="white")
        self.bottom_frame.pack(fill=tk.X, padx=20, pady=20)

        self.quantity_label = tk.Label(self.bottom_frame, text="购买数量:", font=("Arial", 12), bg="white")
        self.quantity_label.pack(side=tk.LEFT)

        self.quantity_entry = tk.Entry(self.bottom_frame, font=("Arial", 12), bg="lightyellow", width=5)  # Smaller width
        self.quantity_entry.pack(side=tk.LEFT, padx=5)

        self.purchase_button = tk.Button(self.bottom_frame, text="购买", command=self.purchase)
        self.purchase_button.pack(side=tk.LEFT, padx=10)
        self.purchase_button.config(bg="lightblue", font=("Arial", 12, "bold"))

        self.return_button = tk.Button(self.bottom_frame, text="返回", command=self.return_to_menu)  # Return button
        self.return_button.pack(side=tk.LEFT, padx=10)
        self.return_button.config(bg="lightgrey", font=("Arial", 12, "bold"))

    def load_products(self):
        conn = pymysql.connect(host='127.0.0.1', user='y2', password='082415', database='y3')
        cursor = conn.cursor()
        cursor.execute("SELECT 商品编号, 商品名称, 销售价格, 库存量 FROM goods")
        products = cursor.fetchall()
        for product in products:
            product_id, name, price, stock = product
            self.products[str(product_id)] = {
                'name': name,
                'price': price,
                'stock': stock
            }
            self.product_listbox.insert(tk.END, f"{product_id}: {name} - ¥{price} (库存: {stock})")
        cursor.close()
        conn.close()

    def purchase(self):
        selected_product = self.product_listbox.get(tk.ACTIVE)
        if not selected_product:
            messagebox.showerror("错误", "请先选择一个商品")
            return

        product_id = selected_product.split(":")[0].strip()
        quantity_str = self.quantity_entry.get()
        if not quantity_str.isdigit():
            messagebox.showerror("错误", "请输入有效的购买数量")
            return

        quantity = int(quantity_str)
        if product_id not in self.products:
            messagebox.showerror("错误", "商品不存在")
            return

        product = self.products[product_id]
        if quantity > int(product['stock']):
            messagebox.showerror("错误", "库存不足")
            return

        total_amount = product['price'] * quantity
        conn = pymysql.connect(host='127.0.0.1', user='y2', password='082415', database='y3')
        cursor = conn.cursor()
        cursor.execute("SELECT 余额 FROM member WHERE 会员卡卡号 = %s", (self.member_id,))
        member_balance = cursor.fetchone()
        if not member_balance or member_balance[0] < total_amount:
            messagebox.showerror("错误", "余额不足")
            cursor.close()
            conn.close()
            return
        # 更新商品库存
        # 更新会员余额
        # cursor.execute("UPDATE member SET 余额 = 余额 - %s WHERE 会员卡卡号 = %s", (total_amount, self.member_id))
        #
        # cursor.execute("UPDATE member SET 累计金额 = 累计金额 + %s WHERE 会员卡卡号 = %s", (total_amount, self.member_id))
        # 添加交易记录
        transaction_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute("SELECT COUNT(*) FROM trade")
        trade_count = cursor.fetchone()[0]
        transaction_id = f"10000{trade_count + 1}"
        cursor.execute(f"SELECT 仓库管理员编号 FROM entry WHERE  商品编号 = {product_id}")
        # 获取查询结果
        results = cursor.fetchall()
        print(results)
        cursor.execute(
            "INSERT INTO trade (交易流水号, 交易日期, 员工编号, 商品编号, 交易数量, 交易金额, 会员卡卡号, 类型) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            (transaction_id, transaction_date,results, product_id, quantity, total_amount, self.member_id, 'purchase')
        )

        conn.commit()
        cursor.close()
        conn.close()

        messagebox.showinfo("提示", f"购买成功: {product['name']} (数量: {quantity})")
        self.product_listbox.delete(0, tk.END)
        self.load_products()

    def return_to_menu(self):
        self.root.destroy()
        win = vip_menu_ui.Win(vip_menu_control.Controller())
        win.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = ShoppingApp(root, "some_member_id")
    root.mainloop()
