import tkinter as tk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from account import *
from pathlib import Path
from tkinter import messagebox as msg

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\USER\Desktop\BookstoreTKinter\src\img")

root = tk.Tk()
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

w = tk


class MainShop:

    def __init__(self, master):
        self.showname = "Guest"
        self.TKshowname = tk.StringVar()
        self.TKshowname.set(self.showname)
        self.id_login = False
        self.master = master
        self.master.geometry("1440x924")
        self.master.configure(bg="#FFFFFF")
        self.master.title("Main Shop")
        self.canvas = Canvas(root, bg = "#1895F5", height = 924, width = 1440, bd = 0, highlightthickness = 0, relief = "ridge")
        self.canvas.place(x = 0, y = 0)
        self.canvas.create_rectangle(0.0,114.0,1440.0,924.0,fill="#FFFFFF",outline="")
        self.shownamelabel = self.canvas.create_text(1331.0,50.0,anchor="nw",text=self.TKshowname.get(),fill="#FFFFFF",font=("Inter", 16 * -1))
        
        
        
        self.button_main_image = PhotoImage(file=relative_to_assets("button_3.png"))
        self.button_main = Button(image=self.button_main_image,borderwidth=0,highlightthickness=0,command=lambda: print("button_3 clicked"),relief="flat")
        self.button_main.place(x=22.0,y=30.0,width=218.0,height=54.0)
        
        
        self.button_account_image = PhotoImage(
        file=relative_to_assets("button_14.png"))
        self.button_account = Button(image=self.button_account_image,borderwidth=0,highlightthickness=0,command=self.select_loginAndregister,relief="flat")
        self.button_account.place(x=1207.0,y=30.0,width=56.0,height=56.0)
        
        
        self.button_cart_image = PhotoImage(
        file=relative_to_assets("button_15.png"))
        self.button_cart = Button(image=self.button_cart_image,borderwidth=0,highlightthickness=0,command=lambda: print("button_15 clicked"),relief="flat")
        self.button_cart.place(x=1083.0, y=30.0, width=56.0, height=56.0)
        
        self.button_manga_image = PhotoImage(
        file=relative_to_assets("button_manga.png"))
        self.button_manga = Button(image=self.button_manga_image,borderwidth=0 , highlightthickness=0 )
        self.button_manga.place(x=274, y=43)
        
        self.button_novel_image = PhotoImage(
        file=relative_to_assets("button_novel.png"))
        self.button_novel = Button(image=self.button_novel_image, borderwidth=0, highlightthickness=0 )
        self.button_novel.place(x=408, y=43)
        

        
    def select_loginAndregister(self):
        if self.id_login == False:
            self.bglr = self.canvas.create_rectangle(1030.0,113.0,1440.0,924.0,fill="#82C9FF",outline="")
            self.button_image_Signinlr = PhotoImage(file=relative_to_assets("button_signin.png"))
            self.button_Signinlr = Button(image=self.button_image_Signinlr,borderwidth=0,highlightthickness=0,command=self.show_login,relief="flat")
            self.button_Signinlr.place(x=1107.0,y=211.0,width=97.0,height=33.0)
            
            self.button_image_Signuplr = PhotoImage(file=relative_to_assets("button_signup.png"))
            self.button_Signuplr = Button(image=self.button_image_Signuplr,borderwidth=0,highlightthickness=0,command=self.show_register,relief="flat")
            self.button_Signuplr.place(x=1268.0,y=211.0,width=97.0,height=33.0)
        if self.id_login:
            self.bgaccount = self.canvas.create_rectangle(1030.0,113.0,1440.0,924.0,fill="#82C9FF",outline="")
            self.bgwhite = self.canvas.create_rectangle(1043.0,208.0,1422.0,582.0,fill="#FFFFFF",outline="")
            self.canvas.create_text(1047.0,153.0,anchor="nw",text="Account Info",fill="#FFFFFF",font=("Inter", 16 * -1))
            self.TKidaccount  = tk.StringVar()
            self.TKnameaccount = tk.StringVar()
            self.TKemailaccount = tk.StringVar()
            self.TKphoneaccount = tk.StringVar()
            self.TKaddraccount = tk.StringVar()
            self.TKidaccount.set("ID: "+self.infologin[0])
            self.TKnameaccount.set("NAME: "+self.infologin[1])
            self.TKemailaccount.set("EMAIL: "+self.infologin[2])
            self.TKphoneaccount.set("PHONE: "+self.infologin[3])
            self.TKaddraccount.set("ADDRESS: "+self.infologin[4])
            self.textIdaccount = self.canvas.create_text(1049.0,220.0,anchor="nw",text=self.TKidaccount.get(),fill="#000000",font=("Inter", 15 * -1))
            self.textnameaccount = self.canvas.create_text(1047.0,300.0,anchor="nw",text=self.TKnameaccount.get(),fill="#000000",font=("Inter", 15 * -1))
            self.textemailaccount = self.canvas.create_text(1047.0,380.0,anchor="nw",text=self.TKemailaccount.get(),fill="#000000",font=("Inter", 15 * -1))
            self.textphoneaccount = self.canvas.create_text(1047.0,460.0,anchor="nw",text=self.TKphoneaccount.get(),fill="#000000",font=("Inter", 15 * -1))
            self.textaddraccount = self.canvas.create_text(1047.0,540.0,anchor="nw",text=self.TKaddraccount.get(),fill="#000000",font=("Inter", 15 * -1))
            
            self.button_image_back = PhotoImage(file=relative_to_assets("button_back.png"))
            self.button_back = Button(image=self.button_image_back,borderwidth=0,highlightthickness=0,command=self.destroy_widgets_account,relief="flat")
            self.button_back.place(x=1048.0,y=623.0,width=97.0,height=33.0)

    def show_login(self):
        self.destroy_wigets_regisorlogin()
        self.bgl = self.canvas.create_rectangle(1030.0,113.0,1440.0,924.0,fill="#82C9FF",outline="")
        self.canvas.place(x = 0, y = 0)
        self.textIdlogin = self.canvas.create_text(1049.0,199.0,anchor="nw",text="id",fill="#000000",font=("Inter", 15 * -1))
        self.textpasslogin = self.canvas.create_text(1047.0,266.0,anchor="nw",text="password",fill="#000000",font=("Inter", 15 * -1))
        self.textlabelsignin =self.canvas.create_text(1047.0,153.0,anchor="nw",text="Sign in Bookstore",fill="#FFFFFF",font=("Inter", 16 * -1))
        

        
        self.entry_image_textfill = PhotoImage(file=relative_to_assets("entry_textfill.png"))
        self.entry_bg_textfill_1 = self.canvas.create_image(1237.0,241.5,image=self.entry_image_textfill)
        self.entry_ID = Entry(bd=0,bg="#FFFFFF",fg="#000716",highlightthickness=0)
        self.entry_ID.place(x=1064.0,y=223.0,width=346.0,height=35.0)

        self.entry_bg_textfill_2 = self.canvas.create_image(1236.0,308.5,image=self.entry_image_textfill)
        self.entry_Password = Entry(bd=0,bg="#FFFFFF",fg="#000716",highlightthickness=0, show="*")
        self.entry_Password.place(x=1063.0,y=290.0,width=346.0,height=35.0 )
        
        
        self.button_image_Signin = PhotoImage(file=relative_to_assets("button_signin.png"))
        self.button_Signin = Button(image=self.button_image_Signin,borderwidth=0,highlightthickness=0,command=self.check_login,relief="flat")
        self.button_Signin.place(x=1327.0,y=357.0,width=97.0,height=33.0)

        self.button_image_back = PhotoImage(file=relative_to_assets("button_back.png"))
        self.button_back = Button(image=self.button_image_back,borderwidth=0,highlightthickness=0,command=self.destroy_widgets_login,relief="flat")
        self.button_back.place(x=1049.0,y=353.0,width=97.0,height=33.0)
    
    
        
    
    def destroy_widgets_login(self):                                                                                                                            #ลบหน้าล็อกอิน
        self.canvas.delete(self.entry_bg_textfill_1, self.entry_bg_textfill_2, self.textIdlogin, self.textpasslogin, self.textlabelsignin ,self.bgl)
        self.entry_ID.destroy()
        self.entry_Password.destroy()
        self.button_Signin.destroy()
        self.button_back.destroy()
        if self.id_login == False:
            self.select_loginAndregister()
        
    
        
    def destroy_widgets_register(self):                                                                                                             #ลบหน้าสมัครสมาชิก
        self.canvas.delete(self.textIdregis, self.textpassregis, self.textnameregis, self.textemailregis, self.textphoneregis, self.textaddrregis, self.bgr)
        self.entry_ID.destroy()
        self.entry_Password.destroy()
        self.entry_Name.destroy()
        self.entry_Email.destroy()
        self.entry_Phone.destroy()
        self.entry_Address.destroy()
        self.button_Signup.destroy()
        self.button_back.destroy()
        self.select_loginAndregister()
    
    def destroy_wigets_regisorlogin(self):                                                                                                              #ลบหน้าสมัครสมาชิกและหน้าล็อกอิน
        self.button_Signinlr.destroy()
        self.button_Signuplr.destroy()
        self.canvas.delete(self.bglr ,self.button_image_Signinlr ,self.button_image_Signuplr)    
        
    def show_register(self):                                                                                                                            #เปิดหน้าสมัครสมาชิก
        self.destroy_wigets_regisorlogin()
        self.bgr = self.canvas.create_rectangle(1030.0,113.0,1440.0,924.0,fill="#82C9FF",outline="")
        self.textIdregis = self.canvas.create_text(1049.0,199.0,anchor="nw",text="id",fill="#000000",font=("Inter", 15 * -1))
        self.textpassregis = self.canvas.create_text(1047.0,266.0,anchor="nw",text="password",fill="#000000",font=("Inter", 15 * -1))
        self.textnameregis = self.canvas.create_text(1047.0,333.0,anchor="nw",text="name",fill="#000000",font=("Inter", 15 * -1))
        self.textemailregis = self.canvas.create_text(1047.0,400.0,anchor="nw",text="email",fill="#000000",font=("Inter", 15 * -1))
        self.textphoneregis = self.canvas.create_text(1047.0,467.0,anchor="nw",text="phone",fill="#000000",font=("Inter", 15 * -1))
        self.textaddrregis = self.canvas.create_text(1047.0,534.0,anchor="nw",text="address",fill="#000000",font=("Inter", 15 * -1))
        
        self.canvas.create_text(1047.0,153.0,anchor="nw",text="Sign up Bookstore",fill="#FFFFFF",font=("Inter", 16 * -1))
        
        self.entry_image_textfill = PhotoImage(file=relative_to_assets("entry_textfill.png"))
        self.entry_bg_textfill_1 = self.canvas.create_image(1237.0,241.5,image=self.entry_image_textfill)
        self.entry_ID = Entry(bd=0,bg="#FFFFFF",fg="#000716",highlightthickness=0)
        self.entry_ID.place(x=1064.0,y=223.0,width=346.0,height=35.0)

        self.entry_bg_textfill_2 = self.canvas.create_image(1236.0,308.5,image=self.entry_image_textfill)
        self.entry_Password = Entry(bd=0,bg="#FFFFFF",fg="#000716",highlightthickness=0, show="*")
        self.entry_Password.place(x=1063.0,y=290.0,width=346.0,height=35.0 )
        
        self.entry_bg_textfill_3 = self.canvas.create_image(1236.0,375.5,image=self.entry_image_textfill)
        self.entry_Name = Entry(bd=0,bg="#FFFFFF",fg="#000716",highlightthickness=0)
        self.entry_Name.place(x=1063.0,y=357.0,width=346.0,height=35.0)
        
        self.entry_bg_textfill_4 = self.canvas.create_image(1236.0,442.5,image=self.entry_image_textfill)
        self.entry_Email = Entry(bd=0,bg="#FFFFFF",fg="#000716",highlightthickness=0)
        self.entry_Email.place(x=1063.0,y=424.0,width=346.0,height=35.0)
        
        self.entry_bg_textfill_5 = self.canvas.create_image(1236.0,509.5,image=self.entry_image_textfill)
        self.entry_Phone = Entry(bd=0,bg="#FFFFFF",fg="#000716",highlightthickness=0)
        self.entry_Phone.place(x=1063.0,y=491.0,width=346.0,height=35.0)
        
        self.entry_bg_textfill_6 = self.canvas.create_image(1236.0,576.5,image=self.entry_image_textfill)
        self.entry_Address = Entry(bd=0,bg="#FFFFFF",fg="#000716",highlightthickness=0)
        self.entry_Address.place(x=1063.0,y=558.0,width=346.0,height=35.0)
        
        
        self.button_image_Signup = PhotoImage(file=relative_to_assets("button_signup.png"))
        self.button_Signup = Button(image=self.button_image_Signup,borderwidth=0,highlightthickness=0,command=self.register_button_clicked,relief="flat")
        self.button_Signup.place(x=1327.0,y=623.0,width=97.0,height=33.0)

        self.button_image_back = PhotoImage(file=relative_to_assets("button_back.png"))
        self.button_back = Button(image=self.button_image_back,borderwidth=0,highlightthickness=0,command=self.destroy_widgets_register,relief="flat")
        self.button_back.place(x=1048.0,y=623.0,width=97.0,height=33.0)
        
                
    def check_login(self):                                                                                              #check login
        id_value = self.entry_ID.get()
        password_value = self.entry_Password.get()
        if self.id_login == False:
            self.id_match = False
            for self.customer in server.customer:
                if self.customer.id == id_value and self.customer.password == password_value:
                    self.id_match = True
                    print (self.customer.name)
                    break
            if self.id_match:
                print ("Login success Welcome" ,self.customer.name)
                self.id_login = True
                self.destroy_widgets_login()
                msg.showinfo("Login", "Login success Welcome" + self.customer.name)
                self.infologin = [self.customer.id, self.customer.name, self.customer.address, self.customer.phone, self.customer.email, self.customer.address]
                self.updatelabel()
                print(self.infologin)
            else:
                msg.showinfo("Login Fail", "Login fail")
                raise ValueError("Login fail")
        else:
            raise ValueError("Please logout first")
        
    def updatelabel(self):
        self.canvas.delete(self.shownamelabel)
        self.showname = self.customer.name
        self.TKshowname.set("Welcome " + self.customer.name)
        self.shownamelabel = self.canvas.create_text(1331.0,50.0,anchor="nw",text=self.TKshowname.get(),fill="#FFFFFF",font=("Inter", 16 * -1))

   
    def register_button_clicked(self):
        self.destroy_wigets_regisorlogin()
        id_value = self.entry_ID.get()
        password_value = self.entry_Password.get()
        name_value = self.entry_Name.get()
        email_value = self.entry_Email.get()
        phone_value = self.entry_Phone.get()
        address_value = self.entry_Address.get()
        
        fill_avoid = False
        for i in [id_value, password_value, name_value, email_value, phone_value, address_value]:
            if i == "" or i == " ":
                fill_avoid = True
                raise ValueError("Please fill in all fields")
        if fill_avoid == False:
            id_exists = False
            for customer in server.customer:
                if customer.id == id_value:
                    id_exists = True
                    break

            if id_exists:
                raise ValueError("ID already exists")
            else:
                customer = Customer(id=id_value,
                                    password=password_value,
                                    name=name_value,
                                    email=email_value,
                                    phone=phone_value,
                                    address=address_value)
                server.add_customer(customer)
                msg.showinfo("Register", "Register success")
                self.destroy_widgets_register()


main_shop = MainShop(root)
root.resizable(False, False)
root.mainloop()
