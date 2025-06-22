import tkinter as tk
from datetime import datetime
from tkinter import messagebox
import pymysql
from UI import menu_ui
from Control import menu_control

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
        win = menu_ui.Win(menu_control.Controller())
        win.mainloop()


class ShoppingApp:
    def __init__(self, root, member_id):
        super().__init__(themename="cosmo", hdpi=False)
        self.cart = []
        self.products = {}
        self.member_id = member_id  # 接收会员卡卡号
        self.create_widgets()
        self.load_products()


    def create_widgets(self):
        self.title("Tkinter布局助手")
        # 设置窗口大小、居中
        width = 600
        height = 550
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)
        self.resizable(width=False, height=False)

        product_listbox = tk.Listbox(self.root)
        product_listbox.pack(fill=tk.BOTH, expand=1)

        quantity_label = tk.Label(self.root, text="购买数量:")
        quantity_label.pack()
        quantity_entry = tk.Entry(self.root)
        quantity_entry.pack()

        add_to_cart_button = tk.Button(self.root, text="加入购物车", command=self.add_to_cart)
        add_to_cart_button.pack()

        view_cart_button = tk.Button(self.root, text="查看购物车", command=self.view_cart)
        view_cart_button.pack()

        checkout_button = tk.Button(self.root, text="结账", command=self.checkout)
        checkout_button.pack()

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

    def add_to_cart(self):
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

        self.cart.append((product_id, quantity))
        messagebox.showinfo("提示", f"商品已加入购物车: {product['name']} (数量: {quantity})")

    def view_cart(self):
        if not self.cart:
            messagebox.showinfo("购物车", "购物车为空")
        else:
            cart_contents = "\n".join(
                [f"{self.products[pid]['name']} - ¥{self.products[pid]['price']} x {qty}" for pid, qty in self.cart]
            )
            messagebox.showinfo("购物车", cart_contents)

    def checkout(self):
        if not self.cart:
            messagebox.showinfo("结账", "购物车为空")
            return

        total_amount = sum(self.products[pid]['price'] * qty for pid, qty in self.cart)
        conn = pymysql.connect(host='127.0.0.1', user='y2', password='082415', database='y3')
        cursor = conn.cursor()
        cursor.execute("SELECT 余额 FROM member WHERE 会员卡卡号 = %s", (self.member_id,))
        member_balance = cursor.fetchone()
        if not member_balance or member_balance[0] < total_amount:
            messagebox.showerror("错误", "余额不足")
            cursor.close()
            conn.close()
            return

        for product_id, quantity in self.cart:
            cursor.execute("UPDATE goods SET 库存量 = 库存量 - %s WHERE 商品编号 = %s", (quantity, product_id))

        cursor.execute("UPDATE member SET 余额 = 余额 - %s WHERE 会员卡卡号 = %s", (total_amount, self.member_id))
        for product_id, quantity in self.cart:
            transaction_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            cursor.execute("""
                INSERT INTO trade (交易日期, 员工编号, 商品编号, 交易数量, 交易金额, 会员卡卡号, 类型)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (
            transaction_date, 'some_employee_id', product_id, quantity, self.products[product_id]['price'] * quantity,
            self.member_id, 'purchase'))

        conn.commit()
        cursor.close()
        conn.close()

        self.cart.clear()
        messagebox.showinfo("结账", "结账成功，谢谢惠顾！")
        self.product_listbox.delete(0, tk.END)
        self.load_products()


if __name__ == "__main__":
    root = tk.Tk()
    app = ShoppingApp(root, "some_member_id")
    root.mainloop()
