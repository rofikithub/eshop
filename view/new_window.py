import tkinter as tk


def newWindowView(self):
    root = tk.Toplevel(self)
    root.title("New Window")
    ww = 400
    wh = 300
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    c_x = int(sw / 2 - ww / 2)
    c_y = int(100)
    root.geometry(f'{ww}x{wh}+{c_x}+{c_y}')
    root.resizable(False, False)
    new_label = tk.Label(root, text="This is a new window!", font=("Arial", 18))
    new_label.pack(pady=50)
