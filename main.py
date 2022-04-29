import tkinter as tk
from tkinter import messagebox



font_title = ('Candara', 13, 'bold')
font_entry = ('Arial', 12)
label_font = ('Arial', 11)
entry_font = ('Arial', 16, 'bold')
base_padding = {'padx': 10, 'pady': 8}
header_padding = {'padx': 10, 'pady': 12}

class ShopApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)


        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)



        self.frames = {}
        for F in (LonMenu, MainMenu, SubmitPage, PortfolioPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame


            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("LonMenu")

    def show_frame(self, page_name):

        frame = self.frames[page_name]
        frame.tkraise()


class LonMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.frame = tk.Frame
        self.frame.configure(self, background='#18528A')

        # метка для поля ввода имени
        username_label = tk.Label(self, text='Имя пользователя', font=label_font, **base_padding,
                                  bg='#FFE042')
        username_label.place(x=40,y=150,width=150,height=20)
        self.controller.configure(background='#334353')
        # поле ввода имени
        self.username_entry = tk.Entry(self, bg='#FF9812', fg='#0C1A1E', font=entry_font)
        self.username_entry.place(x=200,y=150,width=150,height=20)

        # метка для поля ввода пароля
        password_label = tk.Label(self, text='Пароль', font=label_font, **base_padding,
                                  bg='#FFE042')
        password_label.place(x=40,y=180,width=150,height=20)

        # поле ввода пароля
        self.password_entry = tk.Entry(self, show='*', bg='#FF9812', fg='#0C1A1E', font=font_entry)
        self.password_entry.place(x=200,y=180,width=150,height=20)

        # кнопка отправки формы
        self.send_btn = tk.Button(self, text='Войти', font='bold',  bg='#F26760',
                                  activebackground='#972C4A', width=10,
                                  command=lambda: self.check_password())
        self.send_btn.place(x=150,y=220,width=100,height=25)

    def check_password(self):
        if self.password_entry.get() == "1" and self.username_entry.get() == "1":
            self.controller.show_frame("MainMenu")
        else:
            messagebox.showinfo("ERROR", "Неверный пароль или логин")


class MainMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.frame = tk.Frame
        self.frame.configure(self, background='#18528A')

        self.title_lbl = tk.Label(self, text='Media Shop - мы предоставляем услуги\n '
                                             'в сфере видео и фото индустрии.',
                                  font=font_title, bg='#FFE042', fg='#2A502A')
        self.title_lbl.place(x=20,y=20,width=350,height=50)

        self.our_comand = tk.Label(self, text='Наша команда',
                                   font=font_title, bg='#FFE042', fg='#2A502A')
        self.our_comand.place(x=140, y=80, width=120, height=20)
        self.image = tk.PhotoImage(file=r"C:\Users\R21211061\Desktop\курасч\main - копия\pro.png")
        self.img1 = tk.Label(self, image=self.image)
        self.img1.place(x=40,y=120,width=80,height=80)

        self.img2 = tk.Label(self, image=self.image)
        self.img2.place(x=160, y=120, width=80, height=80)

        self.img3 = tk.Label(self, image=self.image)
        self.img3.place(x=280, y=120, width=80, height=80)

        self.submit_btn = tk.Button(self, text='Подать заявку', font='bold', bg='#F26760',
                                  activebackground='#972C4A', width=10,
                                  command=lambda: self.clickbtn1())
        self.submit_btn.place(x=20, y=320, width=150, height=25)

        self.look_btn = tk.Button(self, text='Портфольо', font='bold', bg='#F26760',
                                  activebackground='#972C4A', width=10,
                                  command=lambda: self.clickbtn2())
        self.look_btn.place(x=220, y=320, width=150, height=25)

    def clickbtn1(self):
        self.controller.show_frame("SubmitPage")

    def clickbtn2(self):
        self.controller.show_frame("PortfolioPage")

class SubmitPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.frame = tk.Frame
        self.frame.configure(self, background='#18528A')

        self.sub_title = tk.Label(self, text='Напишите требования и \n'
                                             'ваши предпочтения на счет контента',
                                   font=font_title, bg='#FFE042', fg='#2A502A')
        self.sub_title.place(x=50, y=10, width=300)
        self.sub_txt = tk.Text(self,  bg='#FF9812', fg='#0C1A1E', font=font_entry,
                               )
        self.sub_txt.place(x=50, y=100, width=300, height=100)

        self.add_btn1 = tk.Checkbutton(self,text='Эффект1 $10', bg='#AFD4EB', activebackground='#972C4A',
                                name='effect1',
                                  command=lambda: self.sub_txt.insert(1.0,'Эффект1 '))
        self.add_btn1.place(x=50, y=210, width=150, height=25)
        self.add_btn2 = tk.Checkbutton(self, text='Эффект2 $15', bg='#AFD4EB', activebackground='#972C4A',
                                  name='effect2',
                                  command=lambda: self.sub_txt.insert(1.0,'Эффект2 '))
        self.add_btn2.place(x=220, y=210, width=150, height=25)
        self.add_btn3 = tk.Checkbutton(self, text='Эффект3 $20', bg='#AFD4EB', activebackground='#972C4A',
                                  name='effect3',
                                  command=lambda: self.sub_txt.insert(1.0,'Эффект3 '))
        self.add_btn3.place(x=50, y=240, width=150, height=25)
        self.add_btn4 = tk.Checkbutton(self, text='Эффект4 $25', bg='#AFD4EB', activebackground='#972C4A',
                                  name='effect4',
                                  command=lambda: self.sub_txt.insert(1.0,'Эффект4 '))
        self.add_btn4.place(x=220, y=240, width=150, height=25)

        self.sub_btn = tk.Button(self, text='Удалить', font='bold', bg='#F26760',
                                  activebackground='#972C4A',
                                  command=lambda: self.delete_text())
        self.sub_btn.place(x=50, y=280, width=120, height=25)


        self.back_btn = tk.Button(self, text='Назад', font='bold', bg='#F26760',
                                  activebackground='#972C4A', width=10,
                                  command=lambda: self.goback())
        self.back_btn.place(x=20, y=450, width=70, height=25)

        self.get_btn = tk.Button(self, text='Заказать', font='bold', bg='#F26760',
                                  activebackground='#972C4A', width=10,
                                  command=lambda: self.openorder())
        self.get_btn.place(x=310, y=450, width=70, height=25)






    def goback(self):
        self.controller.show_frame("MainMenu")

    def goback2(self):
        self.controller.show_frame("SubmitPage")

    def delete_text(self):
        self.sub_txt.delete(1.0, tk.END)

    def openorder(self):
        messagebox.showinfo("Заказ принят!", self.sub_txt.get(1.0, tk.END))




class PortfolioPage(SubmitPage):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.frame = tk.Frame

        self.frame.configure(self, background='#18528A')


        self.port_title = tk.Label(self, text='Наши работы - довольные клиенты',
                                  font=font_title, bg='#FFE042', fg='#2A502A')
        self.port_title.place(x=50, y=10, width=300)


        self.btn_image1 = tk.Button(self,text='Фотоотчет1', font='bold', bg='#F26760',
                                  activebackground='#972C4A', width=10,
                                  command=lambda: self.Img1())
        self.btn_image2 = tk.Button(self,text='Фотоотчет2', font='bold', bg='#F26760',
                                  activebackground='#972C4A', width=10,
                                  command=lambda: self.Img2())
        self.btn_image3 = tk.Button(self,text='Фотоотчет3', font='bold', bg='#F26760',
                                  activebackground='#972C4A', width=10,
                                  command=lambda: self.Img3())
        self.btn_image4 = tk.Button(self, text='Фотоотчет4', font='bold', bg='#F26760',
                                    activebackground='#972C4A', width=10,
                                    command=lambda: self.Img4())
        self.btn_image1.place(x=50, y=80)
        self.btn_image2.place(x=200, y=80)
        self.btn_image3.place(x=50, y=150)
        self.btn_image4.place(x=200, y=150)

        self.back_btn = tk.Button(self, text='Назад', font='bold', bg='#F26760',
                                  activebackground='#972C4A', width=10,
                                  command=lambda: self.goback())
        self.back_btn.place(x=20, y=450, width=70, height=25)

    def Img1(self):
        self.r = tk.Toplevel()
        self.r.title("My image")

        self.canvas = tk.Canvas(self.r, height=600, width=600)
        self.canvas.pack()
        self.my_image = tk.PhotoImage(file=r"D:\ex\build\main\add.png", master=self.controller)
        self.canvas.create_image(0, 0, anchor='nw', image=self.my_image)
        self.r.mainloop()

    def Img2(self):
        self.r = tk.Toplevel()
        self.r.title("My image")

        self.canvas = tk.Canvas(self.r, height=600, width=600)
        self.canvas.pack()
        self.my_image = tk.PhotoImage(file=r"D:\ex\build\main\pro.png", master=self.controller)
        self.canvas.create_image(0, 0, anchor='nw', image=self.my_image)
        self.r.mainloop()

    def Img3(self):
        self.r = tk.Toplevel()
        self.r.title("My image")

        self.canvas = tk.Canvas(self.r, height=600, width=600)
        self.canvas.pack()
        self.my_image = tk.PhotoImage(file=r"D:\ex\build\main\index.png", master=self.controller)
        self.canvas.create_image(0, 0, anchor='nw', image=self.my_image)
        self.r.mainloop()

    def Img4(self):
        self.r = tk.Toplevel()
        self.r.title("My image")

        self.canvas = tk.Canvas(self.r, height=600, width=600)
        self.canvas.pack()
        self.my_image = tk.PhotoImage(file=r"D:\ex\build\main\air.png", master=self.controller)
        self.canvas.create_image(0, 0, anchor='nw', image=self.my_image)
        self.r.mainloop()

if __name__ == "__main__":
    app = ShopApp()

    app.title("Media Shop")
    app.geometry("400x500")
    app.resizable(False, False)

    app.grid_columnconfigure(0, minsize=100)
    app.mainloop()