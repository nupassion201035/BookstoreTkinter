from tkinter import *
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from account import *
from pathlib import Path
from tkinter import messagebox as msg
import tkinter as tk

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\USER\Desktop\BookstoreTKinter\src\img")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

LARGE_FONT= ("Verdana", 12)


class Bookstore(tk.Tk):
    def __init__(self, *args ,**kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.geometry(self, "1440x924")
        tk.Tk.title(self, "Bookstore")
        tk.Tk.resizable(self, False, False)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        
        
        for F in {Mainpage, Loginpage, Registerpage, Cartpage ,MangaPage, NovelPage, AccountPage}:
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(Mainpage)
        
    def show_frame(self, cont):
    
        frame = self.frames[cont]
        frame.tkraise()

        
class Mainpage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        
        self.canvas = Canvas(self, bg="#1895F5", height=110, width=1440, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack()
        
        self.showname = "Guest"
        self.TKshowname = StringVar()
        self.TKshowname.set(self.showname)
        
        self.Lable_main = Label(self, text=self.TKshowname.get(), bg="#1895F5", fg="white", font=("Inter", 16))
        self.Lable_main.place(x=1331, y=45)
        
        self.button_account_image = PhotoImage(file=relative_to_assets("button_account.png"))
        self.button_account = Button(self, image=self.button_account_image,borderwidth=0,highlightthickness=0,command=lambda: controller.show_frame(AccountPage) if server.status else controller.show_frame(Loginpage),relief="flat")
        self.button_account.place(x=1207.0,y=30.0,width=56.0,height=56.0)
        
        self.button_manga_image = PhotoImage(
        file=relative_to_assets("button_manga.png"))
        self.button_manga = Button(self, image=self.button_manga_image, borderwidth=0, highlightthickness=0,command=lambda: print(server.status),relief="flat")
        self.button_manga.place(x=274, y=43)
        
        self.button_novel_image = PhotoImage(
        file=relative_to_assets("button_novel.png"))
        self.button_novel = Button(self, image=self.button_novel_image, borderwidth=0, highlightthickness=0,command=lambda: controller.show_frame(NovelPage),relief="flat")
        self.button_novel.place(x=408, y=43)
        
        
        self.button_cart_image = PhotoImage(
        file=relative_to_assets("button_cart.png"))
        self.button_cart = Button(self,image=self.button_cart_image,borderwidth=0,highlightthickness=0,command=lambda: controller.show_frame(Cartpage),relief="flat")
        self.button_cart.place(x=1083.0, y=30.0, width=56.0, height=56.0)
        
        self.button_bookstore_image = PhotoImage(file=relative_to_assets("button_Bookstore.png"))
        self.button_bookstore = Button(self, image=self.button_bookstore_image,borderwidth=0,highlightthickness=0,command=lambda: controller.show_frame(Mainpage),relief="flat")
        self.button_bookstore.place(x=22.0, y=30.0, width=218.0, height=54.0)
        

class Loginpage(tk.Frame):


    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        self.canvas = Canvas(self, bg="#1895F5", height=110, width=1440, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack()
        self.button_account_image = PhotoImage(file=relative_to_assets("button_account.png"))
        self.button_account = Button(self, image=self.button_account_image,borderwidth=0,highlightthickness=0,command=lambda: controller.show_frame(AccountPage) if server.status else controller.show_frame(Loginpage),relief="flat")
        self.button_account.place(x=1207.0,y=30.0,width=56.0,height=56.0)
        
        self.button_manga_image = PhotoImage(file=relative_to_assets("button_manga.png"))
        self.button_manga = Button(self, image=self.button_manga_image, borderwidth=0, highlightthickness=0,command=lambda: controller.show_frame(MangaPage),relief="flat")
        self.button_manga.place(x=274, y=43)
        
        self.button_novel_image = PhotoImage(file=relative_to_assets("button_novel.png"))
        self.button_novel = Button(self, image=self.button_novel_image, borderwidth=0, highlightthickness=0,command=lambda: controller.show_frame(NovelPage),relief="flat")
        self.button_novel.place(x=408, y=43)
        
        
        self.button_cart_image = PhotoImage(file=relative_to_assets("button_cart.png"))
        self.button_cart = Button(self,image=self.button_cart_image,borderwidth=0,highlightthickness=0,command=lambda: controller.show_frame(Cartpage),relief="flat")
        self.button_cart.place(x=1083.0, y=30.0, width=56.0, height=56.0)
        
        self.button_bookstore_image = PhotoImage(file=relative_to_assets("button_Bookstore.png"))
        self.button_bookstore = Button(self, image=self.button_bookstore_image,borderwidth=0,highlightthickness=0,command=lambda: controller.show_frame(Mainpage),relief="flat")
        self.button_bookstore.place(x=22.0, y=30.0, width=218.0, height=54.0)
        
        self.canvas = Canvas(self, bg="#82C9FF", height=1000, width=811, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=1030, y=110)
        
        self.Lable_main = Label(self, text="Sign in Bookstore", bg="#82c9ff", fg="white", font=("Inter", 16))
        self.Lable_main.place(x=1047.0,y=153.0)
        self.textIdlogin = Label(self, text="ID" ,bg="#82c9ff", fg="#FFFFFF", font=("Inter", 12))
        self.textIdlogin.place(x=1049.0, y=200.0)
        self.textpasslogin = Label(self, text="Password" ,bg="#82c9ff", fg="#FFFFFF", font=("Inter", 12))
        self.textpasslogin.place(x=1047.0, y=290.0)
        
        
        self.entry_image_textfill = PhotoImage(file=relative_to_assets("button_bookstore.png"))
        self.canvas.create_image(1237.0, 241.5, image=self.entry_image_textfill)
        self.entry_ID = Entry(self, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0 ,font=("Inter", 15)) 
        self.entry_ID.place(x=1064.0, y=230.0, width=346.0, height=35.0)
        
        self.entry_Password = Entry(self, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0 , show="*")
        self.entry_Password.place(x=1063.0, y=320.0, width=346.0, height=35.0)
        
        self.button_image_Signin = PhotoImage(file=relative_to_assets("button_signin.png"))
        self.button_Signin = Button(self, image=self.button_image_Signin,borderwidth=0,highlightthickness=0,command=self.system_login,relief="flat")
        self.button_Signin.place(x=1188.0,y=380.0,width=97.0,height=33.0)

        self.canvas1 = Canvas(self, bg="#FEFCFF", height=2, width=348, bd=0, highlightthickness=0, relief="ridge")
        self.canvas1.place(x=1064, y=440)
        
        self.Lable_main = Label(self, text="Don't have an account?", bg="#82c9ff", fg="white", font=("Inter", 16))
        self.Lable_main.place(x=1120.0,y=480.0)
        
        self.button_image_signup = PhotoImage(file=relative_to_assets("button_signup.png"))
        self.button_signup = Button(self, image=self.button_image_signup,borderwidth=0,highlightthickness=0,command=lambda: controller.show_frame(Registerpage),relief="flat")
        self.button_signup.place(x=1188.0,y=530.0,width=97.0,height=33.0)
            

        
    def system_login(self ):
        self.id = self.entry_ID.get()
        self.password = self.entry_Password.get()
        self.entry_ID.delete(0,END)
        self.entry_Password.delete(0,END)
        if server.status == True:
            msg.showinfo("Login", "You are already logged in")
        if server.status == False:
            self.iogin_check = False
            for self.customer in server.customer:
                if self.customer.id == self.id and self.customer.password == self.password:
                    server.status = True
                    self.login_check = True
                    print(self.customer , server.status)
                    msg.showinfo("Login", "Login Success")
                    self.controller.show_frame(Mainpage)
                    break
                else:
                    msg.showinfo("Login", "Login Failed Plase try again")
    
                
        
        
        


        
        
        
        


class Registerpage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.canvas = Canvas(self, bg="#1895F5", height=110, width=1440, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack()
        
        self.button_account_image = PhotoImage(file=relative_to_assets("button_account.png"))
        self.button_account = Button(self, image=self.button_account_image,borderwidth=0,highlightthickness=0,command=lambda: controller.show_frame(AccountPage) if server.status else controller.show_frame(Loginpage),relief="flat")
        self.button_account.place(x=1207.0,y=30.0,width=56.0,height=56.0)
        
        self.button_manga_image = PhotoImage(
        file=relative_to_assets("button_manga.png"))
        self.button_manga = Button(self, image=self.button_manga_image, borderwidth=0, highlightthickness=0,command=lambda: controller.show_frame(MangaPage),relief="flat")
        self.button_manga.place(x=274, y=43)
        
        self.button_novel_image = PhotoImage(
        file=relative_to_assets("button_novel.png"))
        self.button_novel = Button(self, image=self.button_novel_image, borderwidth=0, highlightthickness=0,command=lambda: controller.show_frame(NovelPage),relief="flat")
        self.button_novel.place(x=408, y=43)
        
        
        self.button_cart_image = PhotoImage(
        file=relative_to_assets("button_cart.png"))
        self.button_cart = Button(self,image=self.button_cart_image,borderwidth=0,highlightthickness=0,command=lambda: controller.show_frame(Cartpage),relief="flat")
        self.button_cart.place(x=1083.0, y=30.0, width=56.0, height=56.0)
        
        self.button_bookstore_image = PhotoImage(file=relative_to_assets("button_Bookstore.png"))
        self.button_bookstore = Button(self, image=self.button_bookstore_image,borderwidth=0,highlightthickness=0,command=lambda: controller.show_frame(Mainpage),relief="flat")
        self.button_bookstore.place(x=22.0, y=30.0, width=218.0, height=54.0)

class Cartpage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.canvas = Canvas(self, bg="#1895F5", height=110, width=1440, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack()
        
        self.button_account_image = PhotoImage(file=relative_to_assets("button_account.png"))
        self.button_account = Button(self, image=self.button_account_image,borderwidth=0,highlightthickness=0,command=lambda: controller.show_frame(AccountPage) if server.status else controller.show_frame(Loginpage),relief="flat")
        self.button_account.place(x=1207.0,y=30.0,width=56.0,height=56.0)
        
        self.button_manga_image = PhotoImage(
        file=relative_to_assets("button_manga.png"))
        self.button_manga = Button(self, image=self.button_manga_image, borderwidth=0, highlightthickness=0,command=lambda: controller.show_frame(MangaPage),relief="flat")
        self.button_manga.place(x=274, y=43)
        
        self.button_novel_image = PhotoImage(
        file=relative_to_assets("button_novel.png"))
        self.button_novel = Button(self, image=self.button_novel_image, borderwidth=0, highlightthickness=0,command=lambda: controller.show_frame(NovelPage),relief="flat")
        self.button_novel.place(x=408, y=43)
        
        
        self.button_cart_image = PhotoImage(
        file=relative_to_assets("button_cart.png"))
        self.button_cart = Button(self,image=self.button_cart_image,borderwidth=0,highlightthickness=0,command=lambda: controller.show_frame(Cartpage),relief="flat")
        self.button_cart.place(x=1083.0, y=30.0, width=56.0, height=56.0)
        
        self.button_bookstore_image = PhotoImage(file=relative_to_assets("button_Bookstore.png"))
        self.button_bookstore = Button(self, image=self.button_bookstore_image,borderwidth=0,highlightthickness=0,command=lambda: controller.show_frame(Mainpage),relief="flat")
        self.button_bookstore.place(x=22.0, y=30.0, width=218.0, height=54.0)
        
class MangaPage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.canvas = Canvas(self, bg="#1895F5", height=110, width=1440, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack()
        
        self.button_account_image = PhotoImage(file=relative_to_assets("button_account.png"))
        self.button_account = Button(self, image=self.button_account_image,borderwidth=0,highlightthickness=0,command=lambda: controller.show_frame(AccountPage) if server.status else controller.show_frame(Loginpage),relief="flat")
        self.button_account.place(x=1207.0,y=30.0,width=56.0,height=56.0)
        
        self.button_manga_image = PhotoImage(
        file=relative_to_assets("button_manga.png"))
        self.button_manga = Button(self, image=self.button_manga_image, borderwidth=0, highlightthickness=0,command=lambda: controller.show_frame(MangaPage),relief="flat")
        self.button_manga.place(x=274, y=43)
        
        self.button_novel_image = PhotoImage(
        file=relative_to_assets("button_novel.png"))
        self.button_novel = Button(self, image=self.button_novel_image, borderwidth=0, highlightthickness=0,command=lambda: controller.show_frame(NovelPage),relief="flat")
        self.button_novel.place(x=408, y=43)
        
        
        self.button_cart_image = PhotoImage(
        file=relative_to_assets("button_cart.png"))
        self.button_cart = Button(self,image=self.button_cart_image,borderwidth=0,highlightthickness=0,command=lambda: controller.show_frame(Cartpage),relief="flat")
        self.button_cart.place(x=1083.0, y=30.0, width=56.0, height=56.0)
        
        self.button_bookstore_image = PhotoImage(file=relative_to_assets("button_Bookstore.png"))
        self.button_bookstore = Button(self, image=self.button_bookstore_image,borderwidth=0,highlightthickness=0,command=lambda: controller.show_frame(Mainpage),relief="flat")
        self.button_bookstore.place(x=22.0, y=30.0, width=218.0, height=54.0)
        
class NovelPage(tk.Frame):
    
    def __init__(self , parent, controller):
        tk.Frame.__init__(self, parent)
        self.canvas = Canvas(self, bg="#1895F5", height=110, width=1440, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack()
        
        self.button_account_image = PhotoImage(file=relative_to_assets("button_account.png"))
        self.button_account = Button(self, image=self.button_account_image,borderwidth=0,highlightthickness=0,command=lambda: controller.show_frame(AccountPage) if server.status else controller.show_frame(Loginpage),relief="flat")
        self.button_account.place(x=1207.0,y=30.0,width=56.0,height=56.0)
        
        self.button_manga_image = PhotoImage(
        file=relative_to_assets("button_manga.png"))
        self.button_manga = Button(self, image=self.button_manga_image, borderwidth=0, highlightthickness=0,command=lambda: controller.show_frame(MangaPage),relief="flat")
        self.button_manga.place(x=274, y=43)
        
        self.button_novel_image = PhotoImage(
        file=relative_to_assets("button_novel.png"))
        self.button_novel = Button(self, image=self.button_novel_image, borderwidth=0, highlightthickness=0,command=lambda: controller.show_frame(NovelPage),relief="flat")
        self.button_novel.place(x=408, y=43)
        
        
        self.button_cart_image = PhotoImage(
        file=relative_to_assets("button_cart.png"))
        self.button_cart = Button(self,image=self.button_cart_image,borderwidth=0,highlightthickness=0,command=lambda: controller.show_frame(Cartpage),relief="flat")
        self.button_cart.place(x=1083.0, y=30.0, width=56.0, height=56.0)
        
        self.button_bookstore_image = PhotoImage(file=relative_to_assets("button_Bookstore.png"))
        self.button_bookstore = Button(self, image=self.button_bookstore_image,borderwidth=0,highlightthickness=0,command=lambda: controller.show_frame(Mainpage),relief="flat")
        self.button_bookstore.place(x=22.0, y=30.0, width=218.0, height=54.0)
        
class AccountPage(tk.Frame):
    
    def __init__(self , parent , controller):
        tk.Frame.__init__(self, parent)
        self.canvas = Canvas(self, bg="#1895F5", height=110, width=1440, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack()

        self.button_account_image = PhotoImage(file=relative_to_assets("button_account.png"))
        self.button_account = Button(self, image=self.button_account_image,borderwidth=0,highlightthickness=0,command=lambda: controller.show_frame(AccountPage) if server.status else controller.show_frame(Loginpage),relief="flat")
        self.button_account.place(x=1207.0,y=30.0,width=56.0,height=56.0)
        
        self.button_manga_image = PhotoImage(
        file=relative_to_assets("button_manga.png"))
        self.button_manga = Button(self, image=self.button_manga_image, borderwidth=0, highlightthickness=0,command=lambda: controller.show_frame(MangaPage),relief="flat")
        self.button_manga.place(x=274, y=43)
        
        self.button_novel_image = PhotoImage(
        file=relative_to_assets("button_novel.png"))
        self.button_novel = Button(self, image=self.button_novel_image, borderwidth=0, highlightthickness=0,command=lambda: controller.show_frame(NovelPage),relief="flat")
        self.button_novel.place(x=408, y=43)
        
        
        self.button_cart_image = PhotoImage(
        file=relative_to_assets("button_cart.png"))
        self.button_cart = Button(self,image=self.button_cart_image,borderwidth=0,highlightthickness=0,command=lambda: controller.show_frame(Cartpage),relief="flat")
        self.button_cart.place(x=1083.0, y=30.0, width=56.0, height=56.0)
        
        self.button_bookstore_image = PhotoImage(file=relative_to_assets("button_Bookstore.png"))
        self.button_bookstore = Button(self, image=self.button_bookstore_image,borderwidth=0,highlightthickness=0,command=lambda: controller.show_frame(Mainpage),relief="flat")
        self.button_bookstore.place(x=22.0, y=30.0, width=218.0, height=54.0)
    

app = Bookstore()
app.mainloop()



