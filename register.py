from function import *
import re
import random

class register(student_bench):
    def register(self):

        bg_image = PhotoImage(master=self.app,file=self.folderAssets+'\\register\\background.png')
        title_image = PhotoImage(master=self.app,file=self.folderAssets+'\\register\\title.png')
        box_image = PhotoImage(master=self.app,file=self.folderAssets+'\\register\\box.png')
        back_btn_image = PhotoImage(master=self.app,file=self.folderAssets+'\\register\\back_button.png')
        register_btn_image = PhotoImage(master=self.app,file=self.folderAssets+'\\register\\register_button.png')
        self.view_image = PhotoImage(master=self.app,file=self.folderAssets+'\\register\\view.png')
        self.not_view_image = PhotoImage(master=self.app,file=self.folderAssets+'\\register\\not_view.png')

        self.v_gender = IntVar()

        self.register = Frame(self.app,width=700,height=500)
        self.register.pack()
        
        backg = Canvas(self.register, width = 700,height = 500)
        backg.pack(fill = "both", expand = True)

        backg.create_image(0,0,image = bg_image,anchor = "nw")
        title = backg.create_image(87,17, image=title_image, anchor='nw')

        box = backg.create_image(87,100,image=box_image,anchor='nw')


        text_name = Label(self.register,text='Nome completo:',font=('Inter',12,'bold'),bg='#F2C299').place(x=102,y=129)
        self.entry_name = Entry(self.register,bd=0)
        self.entry_name.place(x=102,y=155,width=228,height=21)

        text_birth = Label(self.register,text='Data de nascimento:',font=('Inter',12,'bold'),bg='#F2C299').place(x=102,y=179)
        self.entry_birth = Entry(self.register,bd=0)
        self.entry_birth.place(x=102,y=205,width=228,height=21)

        text_cpf = Label(self.register,text='CPF:',font=('Inter',12,'bold'),bg='#F2C299').place(x=102,y=229)
        self.entry_cpf = Entry(self.register,bd=0)
        self.entry_cpf.place(x=102,y=255,width=228,height=21)

        text_phone = Label(self.register,text='Telefone:',font=('Inter',12,'bold'),bg='#F2C299').place(x=102,y=279)
        self.entry_phone = Entry(self.register,bd=0)
        self.entry_phone.place(x=102,y=305,width=228,height=21)

        text_locality = Label(self.register,text='Localidade:',font=('Inter',12,'bold'),bg='#F2C299').place(x=366,y=129)
        self.entry_locality = Entry(self.register,bd=0)
        self.entry_locality.place(x=366,y=155,width=228,height=21)

        text_gender = Label(self.register,text='Gênero:',font=('Inter',12,'bold'),bg='#F2C299').place(x=366,y=179)
        man_gender = Radiobutton(self.register,text='Masc.',value='1',variable=self.v_gender,bg='#F2C299',activebackground='#F2C299')
        man_gender.place(x=366,y=205)
        wom_gender = Radiobutton(self.register,text='Fem.',value='2',variable=self.v_gender,bg='#F2C299',activebackground='#F2C299')
        wom_gender.place(x=430,y=205)
        other_gender = Radiobutton(self.register,text='Outro.',value='3',variable=self.v_gender,bg='#F2C299',activebackground='#F2C299')
        other_gender.place(x=488,y=205)

        text_email = Label(self.register,text='EMAIL:',font=('Inter',12,'bold'),bg='#F2C299').place(x=366,y=229)
        self.entry_email = Entry(self.register,bd=0)
        self.entry_email.place(x=366,y=255,width=228,height=21)

        text_passw = Label(self.register,text='Senha:',font=('Inter',12,'bold'),bg='#F2C299').place(x=366,y=279)
        self.entry_passw = Entry(self.register,bd=0,show='*')
        self.entry_passw.place(x=366,y=305,width=228,height=21)
        self.view_button = Button(self.register,image=self.not_view_image,bg='#FFF',activebackground='#FFF',bd=0,command=self.view_passw)
        self.view_button.place(x=570,y=306,width=19,height=19)

        text_about = Label(self.register,text='Sobre você:',font=('Inter',12,'bold'),bg='#F2C299').place(x=102,y=329)
        self.entry_about = Text(self.register,bd=0)
        self.entry_about.place(x=102,y=355,width=490,height=70)


        back_btn = Button(self.register,image=back_btn_image,bg='#6BA5F2',activebackground='#6BA5F2',bd=0,command=self.go_home).place(x=87,y=447)
        register_btn = Button(self.register,image=register_btn_image,bg='#6BA5F2',activebackground='#6BA5F2',bd=0,command=self.log_data).place(x=452,y=447)

        self.register.mainloop()


    def view_passw(self):
        self.view_button.config(image=self.view_image,command=self.not_view_passw)
        self.entry_passw.config(show='')

    def not_view_passw(self):
        self.view_button.config(image=self.not_view_image,command=self.view_passw)
        self.entry_passw.config(show='*')


    def card_generator(self):
        while True:
            prefixes = ['4', '51', '52', '53', '54', '55', '34', '37']
            prefix = random.choice(prefixes)
            number = prefix + ''.join(random.choice('0123456789') for _ in range(16 - len(prefix)))
            number = re.sub(r"(\d{4})", r"\1.", number, count=3)
            if not dql(f"SELECT n_cartão FROM alunos WHERE n_cartão = '{number}'"):
                return number


    def log_data(self):
        if self.entry_name.get() == '' or self.entry_birth.get() == '' or self.entry_cpf.get() == '' or self.entry_phone.get() == '' or self.entry_locality.get() == '' or self.v_gender.get() == '' or self.entry_email.get() == '' or self.entry_passw.get() == '':
            messagebox.showerror(title='Erro',message='Preencha os dados obrigatórios')
            return
        
        if dql(f"SELECT email,cpf FROM alunos WHERE email = '{self.entry_email.get()}' OR cpf = '{self.entry_cpf.get()}'"):
            messagebox.showerror(title='Erro',message='Seu EMAIL ou CPF já estão cadastrados')
            return 
        
        regex_email = re.compile(r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$')
        regex_cpf = re.compile(r'^(\d{3}\.){2}\d{3}-\d{2}$')
        regex_date = re.compile(r'(\d{2})/(\d{2})/(\d{4})')
        if not regex_cpf.match(self.entry_cpf.get()) or not regex_email.match(self.entry_email.get()) or not regex_date.match(self.entry_birth.get()):
            messagebox.showerror(title='Erro',message='Digite os dados corretamente')
            return
        
        if self.v_gender.get() == 1:
            self.gender = 'M'
        elif self.v_gender.get() == 2:
            self.gender = 'F'
        else:
            self.gender = 'O'

        self.n_card = self.card_generator()

        dml(f"INSERT INTO alunos (cpf,nome,nascimento,telefone,localidade,sexo,email,senha,obs,n_cartão) VALUES ('{self.entry_cpf.get()}','{self.entry_name.get()}','{self.entry_birth.get()}','{self.entry_phone.get()}','{self.entry_locality.get()}','{self.gender}','{self.entry_email.get()}','{self.entry_passw.get()}','{self.entry_about.get('1.0',END)}','{self.n_card}')")
        messagebox.showinfo(title='Cadastro sucedido',message='O seu cadastro ocorreu com sucesso!')
        self.go_home()


    def go_home(self):
            from home import home
            self.register.destroy()
            home().home()