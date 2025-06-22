import tkinter as tk
from tkinter import messagebox

import fenpei_control
from UI import menu_ui
from Control import menu_control
from UI import fenpei_ui
if __name__ == "__main__":
    win=menu_ui.Win(menu_control.Controller())
    fenpei_ui.Win(fenpei_control.Controller()).destroy()
    win.mainloop()
