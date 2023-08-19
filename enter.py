from function import *

class enter(student_bench):
    def enter(self):

        bg_image = PhotoImage(master=super().app,file=super().folderAssets+'\\enter\\background.png')
        title_image = PhotoImage(master=super().app,file=super().folderAssets+'\\enter\\title.png')
        box_image = PhotoImage(master=super().app,file=super().folderAssets+'\\enter\\box.png')
        back_btn_image = PhotoImage(master=super().app,file=super().folderAssets+'\\enter\\back_button.png')
        enter_btn_image = PhotoImage(master=super().app,file=super().folderAssets+'\\enter\\enter_button.png')
        self.view_image = PhotoImage(master=super().app,file=super().folderAssets+'\\enter\\view.png')
        self.not_view_image = PhotoImage(master=super().app,file=super().folderAssets+'\\enter\\not_view.png')

        self.enter = Frame(super().app,width=700,height=500)
        self.enter.pack()


        fundo = Canvas(self.enter, width = 700,height = 500)
        fundo.pack(fill = "both", expand = True)

        fundo.create_image(0,0,image = bg_image,anchor = "nw")
        title = fundo.create_image(87,31, image=title_image, anchor='nw')

        box = fundo.create_image(87,127,image=box_image,anchor='nw')

        text_email = Label(self.enter,text='EMAIL:',font=('Inter',12,'bold'),bg='#F2C299').place(x=236,y=169)
        self.entry_email = Entry(self.enter,bd=0)
        self.entry_email.place(x=236,y=197,width=228,height=21)

        text_passw = Label(self.enter,text='Senha:',font=('Inter',12,'bold'),bg='#F2C299').place(x=236,y=224)
        self.entry_passw = Entry(self.enter,bd=0,show='*')
        self.entry_passw.place(x=236,y=252,width=228,height=21)
        self.view_button = Button(self.enter,image=self.not_view_image,bg='#FFF',activebackground='#FFF',bd=0,command=self.view_passw)
        self.view_button.place(x=440,y=253,width=19,height=19)

        text_cpf = Label(self.enter,text='CPF:',font=('Inter',12,'bold'),bg='#F2C299').place(x=236,y=279)
        self.entry_cpf = Entry(self.enter,bd=0)
        self.entry_cpf.place(x=236,y=307,width=228,height=21)

        back_btn = Button(self.enter,image=back_btn_image,bg='#6BA5F2',activebackground='#6BA5F2',bd=0,command=self.go_home).place(x=92,y=395)

        enter_btn = Button(self.enter,image=enter_btn_image,bg='#6BA5F2',activebackground='#6BA5F2',bd=0,command=self.verify_data).place(x=457,y=395)

        self.enter.mainloop()


    def view_passw(self):
        self.view_button.config(image=self.view_image,command=self.not_view_passw)
        self.entry_passw.config(show='')

    def not_view_passw(self):
        self.view_button.config(image=self.not_view_image,command=self.view_passw)
        self.entry_passw.config(show='*')


    def verify_data(self):
        dados = dql(f"SELECT email,senha,cpf FROM alunos WHERE email = '{self.entry_email.get()}' AND senha = '{self.entry_passw.get()}' AND cpf = '{self.entry_cpf.get()}'")
        if dados:
            messagebox.showinfo(title='Entrada sucedida',message='A entrada ocorreu com sucesso!')
            self.grab_data()
            self.go_homepage()
        else:
            messagebox.showerror(title='Erro',message='Seus dados estão incorretos')
    

    def grab_data(self):
        student_bench.user_infor = dql(f"SELECT * FROM alunos WHERE cpf = '{self.entry_cpf.get()}'")[0]
        student_bench.color_user = int(self.user_infor[11][-1]) // 2
        student_bench.user_cpf = self.entry_cpf.get()


    def go_home(self):
        from home import home
        self.enter.destroy()
        home().home()


    def go_homepage(self):
        from homepage import homepage
        self.enter.destroy()
        homepage().homepage()
