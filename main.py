import tkinter as tk
from view.deshboardView import dashboardView


class App:
    def __init__(self,root):
        
        dashboardView(root)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
