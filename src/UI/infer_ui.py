import tkinter as tk
from tkinter import messagebox
import pymysql
from  UI import vip_menu_ui
from Control import vip_menu_control

class RefundApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.__win()
        self.create_widgets()

    def __win(self):
        self.title("会员退款界面")
        width = 500
        height = 400
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) // 2, (screenheight - height) // 2)
        self.geometry(geometry)
        self.resizable(width=False, height=False)

    def create_widgets(self):
        tk.Label(self, text="交易流水号:").grid(row=0, column=0, padx=10, pady=10)
        self.entry_transaction_id = tk.Entry(self)
        self.entry_transaction_id.grid(row=0, column=1, padx=10, pady=10)

        self.btn_query = tk.Button(self, text="查询订单", command=self.query_order)
        self.btn_query.grid(row=1, columnspan=2, pady=10)

        self.info_text = tk.Text(self, height=10, width=60)
        self.info_text.grid(row=2, columnspan=2, padx=10, pady=10)
        self.info_text.config(state=tk.DISABLED)

        self.btn_frame = tk.Frame(self)
        self.btn_frame.grid(row=3, columnspan=2, pady=10)

        self.btn_refund = tk.Button(self.btn_frame, text="处理退款", command=self.process_refund, state=tk.DISABLED,
                                    bg="#4CAF50", fg="white", padx=10, pady=5)
        self.btn_refund.grid(row=0, column=0, padx=10)

        self.btn_back = tk.Button(self.btn_frame, text="取消", command=self.back, bg="#f44336", fg="white", padx=10,
                                  pady=5)
        self.btn_back.grid(row=0, column=1, padx=10)

    def query_order(self):
        transaction_id = self.entry_transaction_id.get()
        if not transaction_id:
            messagebox.showwarning("输入错误", "请输入交易流水号")
            return

        try:
            conn =pymysql.connect(host="127.0.0.1", user="root",password="082415", database="y3")
            cursor = conn.cursor()

            cursor.execute(
                "SELECT 商品编号, 交易数量, 交易金额, 会员卡卡号 FROM trade WHERE 交易流水号 = %s AND 类型 = 'purchase'",
                (transaction_id,))
            result = cursor.fetchone()

            if not result:
                messagebox.showerror("错误", "没有找到符合条件的购买交易记录")
                self.info_text.config(state=tk.NORMAL)
                self.info_text.delete('1.0', tk.END)
                self.info_text.config(state=tk.DISABLED)
                self.btn_refund.config(state=tk.DISABLED)
                return

            商品编号, 交易数量, 交易金额, 会员卡卡号 = result
            self.info_text.config(state=tk.NORMAL)
            self.info_text.delete('1.0', tk.END)
            self.info_text.insert(tk.END, f"商品编号: {商品编号}\n", 'bold')
            self.info_text.insert(tk.END, f"交易数量: {交易数量}\n", 'bold')
            self.info_text.insert(tk.END, f"交易金额: {交易金额}\n", 'bold')
            self.info_text.insert(tk.END, f"会员卡卡号: {会员卡卡号}\n", 'bold')
            self.info_text.config(state=tk.DISABLED)

            self.btn_refund.config(state=tk.NORMAL)

        except pymysql.Error as err:
            messagebox.showerror("数据库错误", f"数据库错误: {err}")
        finally:
            cursor.close()
            conn.close()

    def process_refund(self):
        transaction_id = self.entry_transaction_id.get()

        try:
            conn = pymysql.connect(host="127.0.0.1", user="root",password="082415", database="y3")
            cursor = conn.cursor()

            cursor.execute(
                "SELECT 商品编号, 交易数量, 交易金额, 会员卡卡号 FROM trade WHERE 交易流水号 = %s AND 类型 = 'purchase'",
                (transaction_id,))
            result = cursor.fetchone()

            if not result:
                messagebox.showerror("错误", "没有找到符合条件的购买交易记录")
                return

            商品编号, 交易数量, 交易金额, 会员卡卡号 = result

            cursor.execute("""
                UPDATE goods 
                SET 销量 = 销量 - %s, 库存量 = 库存量 + %s 
                WHERE 商品编号 = %s
            """, (交易数量, 交易数量, 商品编号))

            cursor.execute("""
                UPDATE member 
                SET 累计金额 = 累计金额 - %s, 余额 = 余额 + %s 
                WHERE 会员卡卡号 = %s
            """, (交易金额, 交易金额, 会员卡卡号))

            cursor.execute("""
                INSERT INTO infer (交易流水号, 商品编号, 退货数量, 退款金额, 退货日期) 
                VALUES (%s, %s, %s, %s, CURDATE())
            """, (transaction_id, 商品编号, 交易数量, 交易金额))

            cursor.execute("""
                UPDATE trade 
                SET 类型 = 'infer' 
                WHERE 交易流水号 = %s
            """, (transaction_id,))

            conn.commit()
            messagebox.showinfo("成功", "退款处理成功")
            self.info_text.config(state=tk.NORMAL)
            self.info_text.delete('1.0', tk.END)
            self.info_text.config(state=tk.DISABLED)
            self.btn_refund.config(state=tk.DISABLED)

        except pymysql.Error as err:
            messagebox.showerror("数据库错误", f"数据库错误: {err}")
            conn.rollback()
        finally:
            cursor.close()
            conn.close()

    def back(self):
        self.destroy()  # 关闭窗口
        # 这里需要导入并创建新的界面类
        win = vip_menu_ui.Win(vip_menu_control.Controller())
        win.mainloop()

if __name__ == "__main__":
    app = RefundApp()
    app.mainloop()
