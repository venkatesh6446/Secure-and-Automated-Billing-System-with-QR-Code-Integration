from tkinter import *
import math,random,os
from tkinter import  messagebox

class Bill_App:
    def __init__(self, root):
        self.root = root
        # Set the window size to 1350x700 and position it at top-left (0,0)
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        bg_color="#074463"  # ---------------color to change IMPORTANT if u chage here total navi bule color will be replaced with given color i.e the colour u given or required --------------
        tilte=Label(self.root,text="BILLING SOFTWARE",bd=12,relief=GROOVE,bg=bg_color,fg="gold",font=("times new roman",30,"bold"),pady=2).pack(fill=X)
    #=================================variables#===============================================
        #=======Cosmetics#===========================
        self.samsung=IntVar()
        self.apple=IntVar()
        self.oneplus=IntVar()
        self.xiaomi=IntVar()
        self.realme=IntVar()
        self.vivo=IntVar()
        #=========grocery#=================
        self.dell=IntVar()
        self.hp=IntVar()
        self.lenovo=IntVar()
        self.macbook=IntVar()
        self.asus=IntVar()
        self.acer=IntVar()
        #=======cold Drinks#==============
        self.powerbank=IntVar()
        self.earbuds=IntVar()
        self.mobilecases=IntVar()
        self.harddrive=IntVar()
        self.coolingpad=IntVar()
        self.wirelessmouse=IntVar()
        #=======Total Product price & Tax varibale===============
        self.cosmetic_price=StringVar()
        self.grocery_price=StringVar()
        self.cold_drink_price=StringVar()
        self.cosmetic_tax=StringVar()
        self.grocery_tax=StringVar()
        self.cold_drink_tax=StringVar()
        #===========customer#===========
        self.c_name=StringVar()
        self.c_phon=StringVar()
        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
       
        self.Search_bill=StringVar()
        #=========customer details Frame==============
        F1=LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer Details",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)
        cname_lb1=Label(F1,text="Customer Name",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_text=Entry(F1,width=15,textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)
        
        cphn_lb1=Label(F1,text="Phone No",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=2,padx=20,pady=5)
        cphn_text=Entry(F1,width=15,textvariable=self.c_phon,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)
        
        c_bill_lb1=Label(F1,text="Bill Number",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=4,padx=20,pady=5)
        c_bill_text=Entry(F1,width=15,textvariable=self.Search_bill,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)

        bill_btn=Button(F1,text="Search",command=self.find_bill,width=10,bd=7,font="arial 12 bold").grid(row=0,column=6,padx=10,pady=10)
       
        #===============MObile Brands Frame==============
        F2=LabelFrame(self.root,bd=10,relief=GROOVE,text="MobileBrands",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F2.place(x=5,y=180,width=325,height=380)
       
        bath_lbl=Label(F2,text="samsung",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        bath_txt=Entry(F2,width=10,textvariable=self.samsung,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        Face_cream_lbl=Label(F2,text="Apple",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        Face_cream_txt=Entry(F2,width=10,textvariable=self.apple,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        Face_w_lbl=Label(F2,text="OnePlus",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        Face_w_txt=Entry(F2,width=10,textvariable=self.oneplus,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        Hair_s_lbl=Label(F2,text="Xiaomi",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        Hair_s_txt=Entry(F2,width=10,textvariable=self.xiaomi,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        Hair_g_lbl=Label(F2,text="Realme",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        Hair_g_txt=Entry(F2,width=10,textvariable=self.realme,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        body_lbl=Label(F2,text="vivo",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        body_txt=Entry(F2,width=10,textvariable=self.vivo,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

         
         #===============Grocery Frame==============
        F3=LabelFrame(self.root,bd=10,relief=GROOVE,text="LaptopBrands",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F3.place(x=340,y=180,width=325,height=380)
      
        g1_lbl=Label(F3,text="Dell",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        g1_txt=Entry(F3,width=10,textvariable=self.dell,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        g2_lbl=Label(F3,text="HP",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        g2_txt=Entry(F3,width=10,textvariable=self.hp,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        g3_lbl=Label(F3,text="Lenovo",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        g3_txt=Entry(F3,width=10,textvariable=self.lenovo,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        g4_lbl=Label(F3,text="MacBook",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        g4_txt=Entry(F3,width=10,textvariable=self.macbook,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        g5_lbl=Label(F3,text="Asus",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        g5_g_txt=Entry(F3,width=10,textvariable=self.asus,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        g6_lbl=Label(F3,text="Acer",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        g6_txt=Entry(F3,width=10,textvariable=self.acer,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)



        #===============Cooldrinks Frame==============
        F4=LabelFrame(self.root,bd=10,relief=GROOVE,text="Accessories",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F4.place(x=670,y=180,width=325,height=380)
       
        c1_lbl=Label(F4,text="PowerBank",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        c1_txt=Entry(F4,width=10,textvariable=self.powerbank,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        c2_lbl=Label(F4,text="EarBuds",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        c2_txt=Entry(F4,width=10,textvariable=self.earbuds,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        c3_lbl=Label(F4,text="MobileCases",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        c3_txt=Entry(F4,width=10,textvariable=self.mobilecases,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        c4_lbl=Label(F4,text="Ssd",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        c4_txt=Entry(F4,width=10,textvariable=self.harddrive,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        c5_lbl=Label(F4,text="CoolingPad",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        c5_txt=Entry(F4,width=10,textvariable=self.coolingpad,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        c6_lbl=Label(F4,text="Wireless Mouse",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        c6_txt=Entry(F4,width=10,textvariable=self.wirelessmouse,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)


        #======================Bill Area=================
        F5=Frame(self.root,bd=10,relief=GROOVE)
        F5.place(x=1010,y=180,width=350,height=380)
        bill_title=Label(F5,text="BILL AREA",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.textarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)
        
        #==========Button Frame============
        F6=LabelFrame(self.root,bd=10,relief=GROOVE,text="Bill Menu",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F6.place(x=0,y=560,relwidth=1,height=140)
        m1=Label(F6,text="Total Mobiles Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky=W)
        m1=Entry(F6,width=18,textvariable=self.cosmetic_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

        m2=Label(F6,text="Total Laptop Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky=W)
        m2=Entry(F6,width=18,textvariable=self.grocery_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)

        m3=Label(F6,text="Total Accessories Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky=W)
        m3=Entry(F6,width=18,textvariable=self.cold_drink_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)


        c1=Label(F6,text="Mobiles Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=2,padx=20,pady=1,sticky=W)
        c1=Entry(F6,width=18,font="arial 10 bold",textvariable=self.cosmetic_tax,bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)

        c2=Label(F6,text="Laptops Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=2,padx=20,pady=1,sticky=W)
        c2=Entry(F6,width=18,font="arial 10 bold",textvariable=self.grocery_tax,bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)

        c3=Label(F6,text="Accessories Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=2,padx=20,pady=1,sticky=W)
        c3=Entry(F6,width=18,font="arial 10 bold",textvariable=self.cold_drink_tax,bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)

        btn_F=Frame(F6,bd=7,relief=GROOVE)
        btn_F.place(x=750,width=580,height=105)
        total_btn=Button(btn_F,command=self.total,text="Total",bg="Cadetblue",fg="white",bd=2,pady=15,width=10,font="arial 15 bold").grid(row=0,column=0,padx=5,pady=5)
        GBill_btn=Button(btn_F,text="Genrate Bill",command=self.bill_area,bg="Cadetblue",fg="white",bd=2,pady=15,width=10,font="arial 15 bold").grid(row=0,column=1,padx=5,pady=5)
        clear_btn=Button(btn_F,text="Clear",command=self.clear_data,bg="Cadetblue",fg="white",bd=2,pady=15,width=10,font="arial 15 bold").grid(row=0,column=2,padx=5,pady=5)
        Exit_btn=Button(btn_F,text="Exit",bg="Cadetblue",command=self.Exit_app,fg="white",bd=2,pady=15,width=10,font="arial 15 bold").grid(row=0,column=3,padx=5,pady=5)
        self.welcome_bill()
        ##=================total button function========================[[[[[[[[[[[cost setting]]]]]]]##
    def total(self):
        self.c_s_p=  self.samsung.get() * 10000 
        self.c_fc_p= self.apple.get() * 50000
        self.c_fw_p= self.oneplus.get() * 20000
        self.c_hs_p= self.xiaomi.get() * 10000
        self.c_hg_p= self.realme.get() * 15000
        self.c_bl_p= self.vivo.get() * 20000
       
    # Calculate cosmetics total
        self.total_cosmetic_price = float(
        self.c_s_p+  
        self.c_fc_p+
        self.c_fw_p+
        self.c_hs_p+
        self.c_hg_p+
        self.c_bl_p

    )
        self.cosmetic_price.set("Rs. " + str(self.total_cosmetic_price))
        self.c_tax=round((self.total_cosmetic_price * 0.05), 2)
        self.cosmetic_tax.set("Rs. "+str(self.c_tax))  # 5% cosmetic tax

    # Calculate grocery total

        self.g_r_p=self.dell.get()*40000
        self.g_f_p=self.hp.get()*75000
        self.g_d_p=self.lenovo.get()*60000
        self.g_w_p=self.macbook.get()*160000
        self.g_s_p=self.asus.get()*80000
        self.g_t_p=self.acer.get()*50000
        self.total_grocery_price = float(
        self.g_r_p +
        self.g_f_p +
        self.g_d_p +
        self.g_w_p +
        self.g_s_p +
        self.g_t_p
)

        self.grocery_price.set("Rs. " + str(self.total_grocery_price))
        self.g_tax=(round(self.total_grocery_price * 0.1, 2))
        self.grocery_tax.set("Rs. " + str(self.g_tax)) # 10% grocery tax

    # Calculate cold drinks total

        self.d_m_p = self.powerbank.get() * 2000
        self.d_c_p = self.earbuds.get() * 1600
        self.d_f_p = self.mobilecases.get() * 500
        self.d_t_p = self.harddrive.get() * 5000
        self.d_l_p = self.coolingpad.get() * 4000
        self.d_s_p = self.wirelessmouse.get() * 500

        self.total_cold_drink_price = float(
    self.d_m_p +
    self.d_c_p +
    self.d_f_p +
    self.d_t_p +
    self.d_l_p +
    self.d_s_p
)

        self.cold_drink_price.set("Rs. " + str(self.total_cold_drink_price))
        self.d_tax=(round(self.total_cold_drink_price * 0.05, 2))
        self.cold_drink_tax.set("Rs. " + str(self.d_tax))  # 5% cold drink tax
        self.Total_bill=float(self.total_cosmetic_price+self.total_grocery_price+self.total_cold_drink_price+self.c_tax+self.g_tax+self.d_tax)
    
    def welcome_bill(self):
        self.textarea.delete('1.0',END)
        self.textarea.insert(END,"\tWelcome Reliance Retail\n")
        self.textarea.insert(END,f"\nBill Number: {self.bill_no.get()}")  
        self.textarea.insert(END,f"\nCustomer Name: {self.c_name.get()}")
        self.textarea.insert(END,f"\nPhone Number: {self.c_phon.get()}")
        self.textarea.insert(END,f"\n======================================")
        self.textarea.insert(END,f"\n Products\t\tQTY\t\tPrice")
        self.textarea.insert(END,f"\n======================================")



    def bill_area(self):
        if self.c_name.get()=="" or self.c_phon.get()=="":
            messagebox.showerror("Error ","Customer details are must");
        else:
            
            self.welcome_bill()

            #======cosmetics#=====billing side display===============[[[[[[[[[bill area dispaly ]]]]]]]]]
            if self.samsung.get() != 0:
                self.textarea.insert(END, f"\n samsung \t\t{self.samsung.get()}\t\t{self.c_s_p}")
            if self.apple.get() != 0: 
                self.textarea.insert(END, f"\n apple \t\t{self.apple.get()}\t\t{self.c_fc_p}")
            if self.oneplus.get() != 0:
                self.textarea.insert(END, f"\n oneplus\t\t{self.oneplus.get()}\t\t{self.c_fw_p}")
            if self.xiaomi.get() != 0:
                self.textarea.insert(END, f"\n xiaomi \t\t{self.xiaomi.get()}\t\t{self.c_hs_p}")  
            if self.realme.get() != 0:
                self.textarea.insert(END, f"\n Realme \t\t{self.realme.get()}\t\t{self.c_hg_p}")  
            if self.vivo.get() != 0:
                self.textarea.insert(END, f"\n vivo \t\t{self.vivo.get()}\t\t{self.c_bl_p}")  

            #===========grocery#==============
            if self.dell.get() != 0:
                self.textarea.insert(END, f"\n DELL \t\t{self.dell.get()}\t\t{self.g_r_p}")  # Corrected alignment for "Rice"
            if self.hp.get() != 0:
                self.textarea.insert(END, f"\n HP \t\t{self.hp.get()}\t\t{self.g_f_p}")  # Consistent tab spacing
            if self.lenovo.get() != 0:
                self.textarea.insert(END, f"\n LENOVO \t\t{self.lenovo.get()}\t\t{self.g_w_p}")
            if self.macbook.get() != 0:
                self.textarea.insert(END, f"\n MACBOOK \t\t{self.macbook.get()}\t\t{self.g_d_p}")  # Removed extra space after "Daal"
            if self.asus.get() != 0:  # Corrected spelling: 'suger' -> 'sugar'
               self.textarea.insert(END, f"\n ASUS \t\t{self.asus.get()}\t\t{self.g_s_p}")  # Updated variable and label to "Sugar"

            if self.acer.get() != 0:
               self.textarea.insert(END, f"\n ACER \t\t{self.acer.get()}\t\t{self.g_t_p}")  # Fixed spacing and alignment
    


            #===========cooldrinks#==============
            if self.powerbank.get() != 0:
                self.textarea.insert(END, f"\n POWER BANK \t\t{self.powerbank.get()}\t\t{self.d_m_p}")  # Corrected: 'rice.get()' -> 'maza.get()'
            if self.earbuds.get() != 0:
                self.textarea.insert(END, f"\n EARBUDS\t\t{self.earbuds.get()}\t\t{self.d_c_p}")  # Capitalized "Cock"
            if self.mobilecases.get() != 0:
                self.textarea.insert(END, f"\n MOBILE CASE \t\t{self.mobilecases.get()}\t\t{self.d_f_p}")  # Capitalized "Frooti"
            if self.harddrive.get() != 0:
                self.textarea.insert(END, f"\n SSD \t\t{self.harddrive.get()}\t\t{self.d_t_p}")  # Corrected name: "Daal" -> "Thumbs Up"
            if self.coolingpad.get() != 0:
               self.textarea.insert(END, f"\n COOLING PAD \t\t{self.coolingpad.get()}\t\t{self.d_l_p}")  # Corrected name: "Suger" -> "Limca"
            if self.wirelessmouse.get() != 0:
                self.textarea.insert(END, f"\n WIRELESS MOUSE \t\t{self.wirelessmouse.get()}\t\t{self.d_s_p}")  # Corrected name: "Tea" -> "Sprite"
    
            self.textarea.insert(END,f"\n--------------------------------------")
            if self.cosmetic_tax.get()!="Rs. 0.0":
                self.textarea.insert(END,f"\n MobilePhone tax\t\t\t{self.cosmetic_tax.get()}")
            if self.grocery_tax.get()!="Rs. 0.0":
                self.textarea.insert(END,f"\n Laptop Tax\t\t\t{self.grocery_tax.get()}")
            if self.cold_drink_tax.get()!="Rs. 0.0":
                self.textarea.insert(END,f"\n Accessories Tax\t\t\t{self.cold_drink_tax.get()}")
                self.textarea.insert(END,f"\n Total Bill \t\t\t Rs. {str(self.Total_bill)}")

            self.textarea.insert(END,f"\n--------------------------------------")
            self.save_bill()
    def save_bill(self):
        op = messagebox.askyesno("Save Bill", "Do you want to save the bill?")
        if op:  # No need for `op > 0` since `askyesno` already returns True/False
            try:
                # Ensure folder exists
                if not os.path.exists("bills"):
                    os.makedirs("bills")
                    
                self.bill_data = self.textarea.get('1.0', END).strip()  # Strip extra spaces or newlines
                file_path = f"bills/{self.bill_no.get()}.txt"
                with open(file_path, "w") as f1:
                    f1.write(self.bill_data)
                
                messagebox.showinfo("Saved", f"Bill no: {self.bill_no.get()} saved successfully!")
            except Exception as e:
                # Handle unexpected errors
                messagebox.showerror("Error", f"An error occurred while saving the bill: {str(e)}")
        else:
            return


    def find_bill(self):
        present="no"
        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.Search_bill.get():
                f1=open(f"bills/{i}","r")
                self.textarea.delete('1.0',END)
                for d in f1:
                            self.textarea.insert(END,d)
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("Clear","Invalid Bill No.")
    def clear_data(self):
        op=messagebox.askyesno("Exit","Do you really want to Clear?")
        if op>0:
            
            self.samsung.set(0)
            self.apple.set(0)
            self.oneplus.set(0)
            self.xiaomi.set(0)
            self.realme.set(0)
            self.vivo.set(0)
            #=========grocery#=================
            self.dell.set(0)
            self.hp.set(0)
            self.lenovo.set(0)
            self.macbook.set(0)
            self.asus.set(0)
            self.acer.set(0)
            #=======cold Drinks#==============
            self.powerbank.set(0)
            self.earbuds.set(0)
            self.mobilecases.set(0)
            self.harddrive.set(0)
            self.coolingpad.set(0)
            self.wirelessmouse.set(0)
            #=======Total Product price & Tax varibale===============
            self.cosmetic_price.set("")
            self.grocery_price.set("")
            self.cold_drink_price.set("")
            self.cosmetic_tax.set("")
            self.grocery_tax.set("")
            self.cold_drink_tax.set("")
            #===========customer#===========
            self.c_name.set("")
            self.c_phon.set("")
            self.bill_no.set("")
            x=random.randint(1000,9999)
            self.bill_no.set(str(x))
            self.welcome_bill()
       
    def Exit_app(self):
        op=messagebox.askyesno("Exit","Do you really want to exit?")
        if op>0:
            self.root.destory()
        

















#--------------------------------------qr genration ---------------------------
import qrcode
import os
import time
import traceback

# Function to generate QR code for the most recently generated bill
def generate_qr_code_for_latest_bill():
    try:
        # Define the path for the bills and QR codes
        bills_directory = r"C:\Users\lakka\OneDrive\Desktop\TECH PRODUCTS\bills"
        
        # Get the list of all files in the directory
        files = os.listdir(bills_directory)
        print("Files in bills directory:", files)  # Debug: Check if the files are listed correctly
        
        # Filter out files that are not .txt (assuming bills are saved in .txt format)
        bill_files = [f for f in files if f.endswith('.txt')]
        print("Bill files found:", bill_files)  # Debug: Check which files are selected as bills
        
        # Check if there are any bill files
        if not bill_files:
            print("No bill files found in the directory.")
            return
        
        # Find the most recently modified bill file
        latest_bill_file = max(bill_files, key=lambda f: os.path.getmtime(os.path.join(bills_directory, f)))
        print(f"Latest bill file: {latest_bill_file}")  # Debug: Check if correct file is selected
        
        # Full path of the most recently modified bill file
        bill_file_path = os.path.join(bills_directory, latest_bill_file)
        
        # Read the bill details from the text file
        with open(bill_file_path, 'r') as bill_file:
            bill_details = bill_file.read()
        
        # Print the bill details for debugging
        print(f"Bill Details:\n{bill_details}")
        
        # Create a QR code from the bill details
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(bill_details)
        qr.make(fit=True)

        # Generate the QR code image
        img = qr.make_image(fill='black', back_color='white')

        # Save the QR code image in the same directory as the bill
        qr_code_file_name = f"{os.path.splitext(latest_bill_file)[0]}_qr.png"  # QR code will have the same name as the bill file
        qr_code_path = os.path.join(bills_directory, qr_code_file_name)
        
        # Save the image
        img.save(qr_code_path)
        print(f"QR Code generated and saved to {qr_code_path}")
    
    except Exception as e:
        print(f"Error generating QR Code: {e}")
        traceback.print_exc()  # Print the detailed traceback for error diagnostics

# Call the function to automatically find the latest bill and generate QR code
generate_qr_code_for_latest_bill()






#--------------------------pdf genration------------------------
import os
import qrcode
from fpdf import FPDF
from PIL import Image

# Define the path for the bills
bills_directory = r"C:\Users\lakka\OneDrive\Desktop\TECH PRODUCTS\bills"

# Get the latest bill file
def get_latest_file(directory, extension):
    try:
        files = [f for f in os.listdir(directory) if f.endswith(extension)]
        if not files:
            print(f"No {extension} files found in {directory}.")
            return None
        return max(files, key=lambda f: os.path.getmtime(os.path.join(directory, f)))
    except FileNotFoundError:
        print(f"Directory not found: {directory}")
        return None

# Generate QR Code
def generate_qr_code(data, qr_path):
    qr = qrcode.QRCode(box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill="black", back_color="white")
    img.save(qr_path)
    return qr_path

# Generate the PDF with enhanced formatting
def generate_pdf():
    latest_bill = get_latest_file(bills_directory, ".txt")
    if not latest_bill:
        return
    
    bill_path = os.path.join(bills_directory, latest_bill)
    try:
        with open(bill_path, "r", encoding="utf-8") as file:
            bill_content = file.read()
    except FileNotFoundError:
        print(f"Bill file not found: {bill_path}")
        return

    # Define paths
    pdf_path = os.path.join(bills_directory, f"{os.path.splitext(latest_bill)[0]}_bill.pdf")
    qr_path = os.path.join(bills_directory, f"{os.path.splitext(latest_bill)[0]}_qr.png")
    
    # Generate QR Code
    generate_qr_code(bill_content, qr_path)

    # Create PDF
    pdf = FPDF()
    pdf.add_page()
    
    # Set background color
    pdf.set_fill_color(240, 240, 240)  # Light Gray
    pdf.rect(0, 0, 210, 297, 'F')  # Fill entire page

    # Draw a border
    pdf.set_line_width(1)
    pdf.set_draw_color(0, 0, 0)  # Black border
    pdf.rect(10, 10, 190, 277)

    # Set font for bill heading
    pdf.set_font("Arial", "B", 16)
    pdf.set_text_color(0, 0, 128)  # Navy Blue
    pdf.cell(190, 10, "Customer Bill", ln=True, align="C")
    pdf.ln(10)

    # Set font for bill content
    pdf.set_font("Arial", size=12)
    pdf.set_text_color(0, 0, 0)  # Black

    # Add bill content, properly aligned
    pdf.set_x(10)
    pdf.multi_cell(190, 8, bill_content, align="L")  # Left aligned
    pdf.ln(10)

    # Draw QR Code Box
    pdf.set_line_width(1)
    pdf.set_draw_color(50, 50, 50)  # Dark Gray
    pdf.rect(75, 190, 60, 60)  # Box for QR code

    # Add QR Code if it exists
    if os.path.exists(qr_path):
        pdf.image(qr_path, x=80, y=195, w=50, h=50)  # QR inside the box

    # Display message below QR Code
    pdf.set_font("Arial", "B", 12)
    pdf.set_text_color(255, 0, 0)  # Red
    pdf.set_xy(10, 260)
    pdf.cell(190, 10, "SCAN QR TO SEE BILL DETAILS", ln=True, align="C")

    # Save PDF
    pdf.output(pdf_path)
    print(f"PDF generated at: {pdf_path}")

# Call the function to generate the formatted PDF
generate_pdf()




#-------------------------------sending eamil---------------------------------
import smtplib
import ssl
import os
from email.message import EmailMessage
from dotenv import load_dotenv

# Load environment variables with override
load_dotenv(override=True)

# Get credentials securely from .env file
EMAIL_SENDER = os.getenv("EMAIL_SENDER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_RECEIVER = "giridharchindam@gmail.com"  # Customer email-----------------------

# Check if credentials are loaded
if not EMAIL_SENDER or not EMAIL_PASSWORD:
    print("❌ ERROR: Missing EMAIL_SENDER or EMAIL_PASSWORD. Check your .env file.")
    exit()

# Directory where PDFs are stored
BILLS_DIR = r"C:\Users\lakka\OneDrive\Desktop\TECH PRODUCTS\bills"

# Function to get the latest PDF file
def get_latest_pdf(directory):
    pdf_files = [f for f in os.listdir(directory) if f.endswith(".pdf")]
    if not pdf_files:
        print("❌ No PDF files found!")
        return None
    latest_file = max(pdf_files, key=lambda f: os.path.getctime(os.path.join(directory, f)))
    return os.path.join(directory, latest_file)

# Get the latest PDF file
PDF_PATH = get_latest_pdf(BILLS_DIR)

if PDF_PATH is None:
    print("❌ No latest PDF found. Exiting.")
    exit()

# Email content
subject = "Your Bill - TECH PRODUCTS"
body = "Dear Customer,\n\nPlease find your bill attached.\n\nThank you!"

# Create EmailMessage object
msg = EmailMessage()
msg["From"] = EMAIL_SENDER
msg["To"] = EMAIL_RECEIVER
msg["Subject"] = subject
msg.set_content(body)

# Attach the latest PDF
with open(PDF_PATH, "rb") as f:
    msg.add_attachment(f.read(), maintype="application", subtype="pdf", filename=os.path.basename(PDF_PATH))

# Connect to SMTP server and send email
try:
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        print("✅ Connecting to SMTP server...")
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        print("✅ Logged in successfully!")
        server.send_message(msg)
    print(f"✅ Email sent successfully with attachment: {PDF_PATH}")
except smtplib.SMTPAuthenticationError:
    print("❌ ERROR: Authentication failed. Check your email & app password.")
except Exception as e:
    print(f"❌ Error sending email: {e}")

root = Tk()
obj = Bill_App(root)
root.mainloop()













#---------------End of the code -------------------------------------




#zkht xskx fysl olbl







