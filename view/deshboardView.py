import tkinter as tk
from tkinter import messagebox, ttk
from view.addProductView import addProductView
from model.Product import Product

class dashboardView:
    def __init__(self,root):
        # self.attributes('-fullscreen', True)
        self.root = root
        root.title("User Dashboard")
        root.iconbitmap(False, 'image/python.ico')
        root.protocol('WM_DELETE_WINDOW', root.quit)
        sw = root.winfo_screenwidth()
        sh = root.winfo_screenheight()-90
        root.geometry(f'{sw}x{sh}+{-10}+{0}')
        
        menu_bar = tk.Menu(root)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Add Product", command=self.addProduct)
        file_menu.add_command(label="All Products")
        menu_bar.add_cascade(label="Product", menu=file_menu)
        menu_bar.add_command(label="License")
        menu_bar.add_command(label="Help")
        menu_bar.add_command(label="Conduct")
        menu_bar.add_command(label="Exit", command=root.quit)
        root.config(menu=menu_bar)

        # Title Bar
        dashboard_frame = tk.Frame(root)
        dashboard_frame.pack(side='top', expand=True)
        label = tk.Label(dashboard_frame, text="Billing System", font=("Arial", 15))
        label.pack(pady=5, padx=10)


        # Customer Details
        customer_frame = tk.Frame(root, pady=5, padx=20)
        customer_frame.pack(fill=tk.BOTH,side='top', expand=True)
        customer_label_frame = tk.LabelFrame(customer_frame, text="Customer Details", pady=10, padx=10)
        customer_label_frame.pack(fill=tk.BOTH, side='left', expand=True)

        bill_number_label = tk.Label(customer_label_frame, text="Bill Number:", pady=10, padx=30)
        bill_number_label.pack(side='left')
        bill_number_entry = tk.Entry(customer_label_frame, bd=0.5, width=40)
        bill_number_entry.pack(side='left')
        bill_number_search = tk.Button(customer_label_frame, text="Search", padx=20, bg="#ddd", fg="black", font=("Arial", 8))
        bill_number_search.pack(side='left')

        customer_name_label = tk.Label(customer_label_frame, text="Customer Name", pady=10, padx=30)
        customer_name_label.pack(side='left')
        customer_name_entry = tk.Entry(customer_label_frame, bd=0.5, width=40)
        customer_name_entry.pack(side='left')

        mobile_number_label = tk.Label(customer_label_frame, text="Mobile Number:", pady=10, padx=30)
        mobile_number_label.pack(side='left')
        mobile_number_entry = tk.Entry(customer_label_frame, bd=0.5, width=40)
        mobile_number_entry.pack(side='left')


        # Product and billing Frame
        details_frame = tk.Frame(root, pady=5, padx=20)
        details_frame.pack(fill=tk.BOTH, side='top', expand=True)

        # Select by category
        details_label_frame = tk.LabelFrame(details_frame, text="Select product by category", pady=20, padx=20)
        details_label_frame.pack(fill=tk.BOTH, side='left', expand=True)

        category_frame = tk.Frame(details_label_frame)
        category_frame.pack(fill=tk.BOTH, side='top' )
        category_label = tk.Label(category_frame, text="Product Category", padx=20, pady=20)
        category_label.pack(side='left')
        category_entry = ttk.Combobox(category_frame, state="readonly",values=["Python", "C", "C++", "Java"], width=30)
        category_entry.pack(side='left')

        product_frame = tk.Frame(details_label_frame)
        product_frame.pack(fill=tk.BOTH, side='top' )
        product_name_label1 = tk.Label(product_frame, text="Product Name    ", padx=20, pady=20)
        product_name_label1.pack(side='left')
        product_name_entry1 = ttk.Combobox(product_frame, state="readonly",values=["Python", "C", "C++", "Java"], width=30)
        product_name_entry1.pack(side='left')

        quntaty_frame = tk.Frame(details_label_frame)
        quntaty_frame.pack(fill=tk.BOTH, side='top' )
        quntaty_label1 = tk.Label(quntaty_frame, text="Product Quntaty", padx=20, pady=20)
        quntaty_label1.pack(side='left')
        quntaty_entry1 = tk.Entry(quntaty_frame, width=33)
        quntaty_entry1.pack(side='left')


        # Select by nane
        name_label_frame = tk.LabelFrame(details_frame, text="Select product by name", padx=10, pady=10)
        name_label_frame.pack(fill=tk.BOTH, side='left' )

        def on_configure(event):
            canvas.configure ( scrollregion=canvas.bbox ( 'all' ) )
        
        canvas = tk.Canvas ( name_label_frame)
        canvas.pack ( side="left", fill="both", expand=True )

        scrollbar = tk.Scrollbar ( name_label_frame, orient="vertical", command=canvas.yview )
        scrollbar.pack ( side="right", fill="y" )

        canvas.configure ( yscrollcommand=scrollbar.set )
        canvas.bind ( '<Configure>', on_configure )

        frame_inside_canvas = tk.Frame ( canvas )
        canvas.create_window ( (0, 0), window=frame_inside_canvas, anchor='nw' )

        # name_frame = tk.Frame(name_label_frame)
        # name_frame.pack(side='top' )
        # product_checkbutton1 = tk.Checkbutton(name_frame, text="ProductName", onvalue=1, offvalue='off', variable=var1, height=2, width=10)
        # product_checkbutton1.pack(side='left')
        # product_name_entry2 = tk.Entry(name_frame, width=20)
        # product_name_entry2.pack(side=RIGHT)

        products = Product().all()
        if products :
            for product in products:
                name_frame = tk.Frame(frame_inside_canvas)
                name_frame.pack(side='top', fill=tk.BOTH, expand=False)
                product_checkbutton = tk.Checkbutton(name_frame, text=product[1], onvalue=2, offvalue='off', variable=product[0], height=1)
                product_checkbutton.pack(side='left', anchor=tk.NW, expand=True)
                product_name_entry = tk.Entry(name_frame, width=20)
                product_name_entry.pack(side='left')

        canvas.update_idletasks ()
        # Set the canvas scroll region
        canvas.config ( scrollregion=canvas.bbox ( "all" ) )

        # Bill Area
        bill_frame = tk.LabelFrame(details_frame, text="Bill Area", padx=10, pady=5, width=50, height=50)
        bill_frame.pack(fill=tk.BOTH, side='top', expand=True)

        bill_box = tk.Text(bill_frame, fg="black", font=("Arial", 9))
        bill_box.pack(side='left')

        bill_box.delete('1.0', tk.END)
        bill_box.insert(tk.END, "\t\t\tE-SHOP ONLINE MARCATE CENTER\n")
        bill_box.insert(tk.END, "\t\t\t        Web Suraj, Kolkata-700 002\n")
        bill_box.insert(tk.END, "\t\t\t           Mobile : - 01737034338\n")
        bill_box.insert(tk.END, "\n---------------------------------------------  BILL NUMBER :  552441  -----------------------------------------")
        bill_box.insert(tk.END, "\nDate :                       19/07/2023  ( Sunday )                                             Time :  11 : 25: 20 AM")
        bill_box.insert(tk.END, "\nCustomer Name :  MD. SHUMON ISLAM")
        bill_box.insert(tk.END, "\nMobile Number :    01737034338")
        bill_box.insert(tk.END, "\n--------------------------------------------------------------------------------------------------------------------------\n")
        bill_box.insert (tk.END, "DESCRIPTION  \t\t\t RATE \t QUANTITY \t\t AMOUNT")
        bill_box.insert(tk.END, "\n--------------------------------------------------------------------------------------------------------------------------\n")
        bill_box.insert (tk.END, "Coffee Espresso  \t\t\t 60 \t 1 \t\t 60 \n" )
        bill_box.insert (tk.END, "Coffee Cappuccino  \t\t\t 60 \t 1 \t\t 60 \n" )
        bill_box.insert (tk.END, "Coffee Americano(Black)  \t\t\t 60 \t 1 \t\t 60 \n" )
        bill_box.insert (tk.END, "Cold Coffee (Frappe)  \t\t\t 60 \t 1 \t\t 60" )
        bill_box.insert(tk.END, "\n--------------------------------------------------------------------------------------------------------------------------\n")
        bill_box.insert (tk.END, "\t\t\t\tTOTAL PRICE \t  = \t 240\n")
        bill_box.insert (tk.END, "\t\t\t\tDiscount  (-)\t      = \t 24\n" )
        bill_box.insert (tk.END, "\t\t\t\tLess (-)\t           = \t 6\n" )
        bill_box.insert (tk.END,"\t\t------------------------------------------------------------------------------------\n" )
        bill_box.insert (tk.END, "\t\t\t\tNET PAYABLE \t  = \t 210\n" )
        bill_box.insert (tk.END, "\t\t\t\tPaid   (-)\t           = \t 210\n" )
        bill_box.insert (tk.END, "\t\t      ------------------------------------------------------------------------\n" )
        bill_box.insert (tk.END, "\t\t\t\tDUE AMOUNT   \t=\t 00\n" )




        # Option Frame
        option_frame = tk.Frame(root, pady=5, padx=20)
        option_frame.pack(fill=tk.BOTH, expand=True, side='top')

        # Card option
        card_label_frame = tk.LabelFrame(option_frame, text="Card Options", pady=10, padx=50)
        card_label_frame.pack(fill=tk.BOTH, expand=True, side='left')
        add_to_cart_btn = tk.Button(card_label_frame, text="Add", padx=20, bg="#ddd", fg="black", font=("Arial", 8))
        add_to_cart_btn.pack(side='left')

        # Billing option
        bill_label_frame = tk.LabelFrame(option_frame, text="Bill Options", pady=10, padx=50)
        bill_label_frame.pack(fill=tk.BOTH, expand=True, side='left')
        add_to_cart_btn1 = tk.Button(bill_label_frame, text="Submit", padx=20, bg="#ddd", fg="black", font=("Arial", 8))
        add_to_cart_btn1.pack(side='left')

    def addProduct(self):
        self.root.destroy()
        addProductView(tk.Tk())
