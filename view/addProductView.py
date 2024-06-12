import tkinter as tk
from tkinter import * # type: ignore
from PIL import ImageTk,Image
from view import deshboardView
from controller.ProductController import ProductController

class addProductView:
    def __init__(self, root):
        self.root = root
        root.title("Add Product")
        ww = 400
        wh = 440
        sw = root.winfo_screenwidth()
        sh = root.winfo_screenheight()
        c_x = int(sw / 2 - ww / 2)
        c_y = int(100)
        root.geometry(f'{ww}x{wh}+{c_x}+{c_y}')
        root.resizable(False, False)



        def backDeshboard(event):
            self.root.destroy()
            deshboardView.dashboardView(tk.Tk())


        add_frame = tk.Frame(root, padx=20, pady=20, relief=tk.RAISED)
        add_frame.pack(fill=tk.BOTH, expand=True, side=TOP)

        add_label_frame = tk.LabelFrame(add_frame, text="Add New Product", padx=5, pady=5)
        add_label_frame.pack(fill=tk.BOTH, expand=True, side=TOP)

        photo = Image.open("image/product.webp")
        image = photo.resize((70,70))
        img = ImageTk.PhotoImage(image)

        image_label = tk.Label(add_label_frame, image = img) # type: ignore
        image_label.image = img # type: ignore
        image_label.pack(side=TOP)

        name_frame = tk.Frame(add_label_frame, padx=10, pady=10)
        name_frame.pack(side=TOP)
        product_name_label = tk.Label(name_frame, text="Name     ")
        product_name_label.pack(side=LEFT)
        self.product_name_entry = tk.Entry(name_frame)
        self.product_name_entry.pack(side=LEFT)

        category_frame = tk.Frame(add_label_frame, padx=10, pady=10)
        category_frame.pack(side=TOP)
        category_label = tk.Label(category_frame, text="Category")
        category_label.pack(side=LEFT)
        self.category_entry = tk.Entry(category_frame)
        self.category_entry.pack(side=LEFT)

        quantity_frame = tk.Frame(add_label_frame, padx=10, pady=10)
        quantity_frame.pack(side=TOP)
        quantity_label = tk.Label(quantity_frame, text="Quantity")
        quantity_label.pack(side=LEFT)
        self.quantity_entry = tk.Entry(quantity_frame)
        self.quantity_entry.pack(side=LEFT)

        sell_frame = tk.Frame(add_label_frame, padx=10, pady=10)
        sell_frame.pack(side=TOP)
        sell_price_label = tk.Label(sell_frame, text="Sell Price")
        sell_price_label.pack(side=LEFT)
        self.sell_price_entry = tk.Entry(sell_frame)
        self.sell_price_entry.pack(side=LEFT)

        cost_frame = tk.Frame(add_label_frame, padx=10, pady=10)
        cost_frame.pack(side=TOP)
        cost_price_label = tk.Label(cost_frame, text="Cost Price")
        cost_price_label.pack(side=LEFT)
        self.cost_price_entry = tk.Entry(cost_frame)
        self.cost_price_entry.pack(side=LEFT)

        btn_frame = tk.Frame(add_label_frame, padx=40, pady=20)
        btn_frame.pack(fill=tk.BOTH, side=TOP)
        new_product_save_btn = tk.Button(btn_frame, command=lambda:self.getValue(), padx=20, text="Save", bg="#ddd",fg="black", font=("Arial", 10))
        new_product_save_btn.pack(side=TOP)

        go_back_label = tk.Label(add_label_frame, text='Go back', cursor='hand2')
        go_back_label.pack(side='top',  fill='both')
        go_back_label.bind("<Button-1>", backDeshboard)

    def getValue(self):
        values = [
            self.product_name_entry.get(),
            self.category_entry.get(),
            self.quantity_entry.get(),
            self.sell_price_entry.get(),
            self.cost_price_entry.get()
        ]

        sms = ProductController.createProduct(values) # type: ignore
        if sms == "success":
            self.product_name_entry.delete(0, tk.END)
            self.category_entry.delete(0, tk.END)
            self.quantity_entry.delete(0, tk.END)
            self.sell_price_entry.delete(0, tk.END)
            self.cost_price_entry.delete(0, tk.END)








