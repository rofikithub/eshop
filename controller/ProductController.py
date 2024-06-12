from tkinter import messagebox
from model.Product import Product


class ProductController:
    def __init__():
        pass

    def createProduct(values):
        if values[0] == "":
            messagebox.showwarning("Error", "Please enter a product name ! ")
        elif values[1] == "":
            messagebox.showwarning("Error", "Please enter a product category ! ")
        elif values[2] == "":
            messagebox.showwarning("Error", "Please enter a product quantity ! ")
        elif values[3] == "":
            messagebox.showwarning("Error", "Please enter a product selling price ! ")
        elif values[4] == "":
            messagebox.showwarning("Error", "Please enter a product cost price ! ")
        else:
            chack = Product.chack(values[0])
            if chack:
                messagebox.showerror("Error", "Product already exists.")
            else:
                create = Product.create(values)
                if create:
                    messagebox.showinfo("Success", "Product saved successfully.")
                    return "success"