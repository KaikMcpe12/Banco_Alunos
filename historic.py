from function import *

class historic(student_bench):
    def def_historic(self,type='withdraw'):
        student_bench.user_cpf = '123.456.789-10'

        style = ttk.Style()

        color_box = '#F2C299'
        color_bg = '#6BA5F2'

        bg_image = PhotoImage(master=super().app,file=super().folderAssets+'\\historic\\background.png')
        title_image = PhotoImage(master=super().app,file=super().folderAssets+f'\\historic\\{type}_title.png')
        box_image = PhotoImage(master=super().app,file=super().folderAssets+'\\historic\\box.png')
        back_btn_image = PhotoImage(master=super().app,file=super().folderAssets+'\\historic\\back_button.png')
        seach_btn_image = PhotoImage(master=super().app,file=super().folderAssets+'\\historic\\seach_button.png')
        transfer_btn_image = PhotoImage(master=super().app,file=super().folderAssets+'\\historic\\transfer_button.png')
        bill_btn_image = PhotoImage(master=super().app,file=super().folderAssets+'\\historic\\bill_button.png')
        deposit_btn_image = PhotoImage(master=super().app,file=super().folderAssets+'\\historic\\deposit_button.png')
        seach_btn_image = PhotoImage(master=super().app,file=super().folderAssets+'\\historic\\seach_button.png')
        withdraw_btn_image = PhotoImage(master=super().app,file=super().folderAssets+'\\historic\\withdraw_button.png')


        self.historic = Frame(super().app,width=700,height=500)
        self.historic.pack()


        fundo = Canvas(self.historic, width = 700,height = 500)
        fundo.pack(fill = "both", expand = True)

        fundo.create_image(0,0,image = bg_image,anchor = "nw")
        title = fundo.create_image(14,25, image=title_image, anchor='nw')

        box = fundo.create_image(14,87,image=box_image,anchor='nw')

        if type == 'withdraw':
            bill_btn = Button(self.historic,image=bill_btn_image,bd=0,bg=color_box,activebackground=color_box,command=lambda:self.go_historic('bill')).place(x=70,y=101)
            transfer_btn = Button(self.historic,image=transfer_btn_image,bd=0,bg=color_box,activebackground=color_box,command=lambda:self.go_historic('transfer')).place(x=301,y=101)
            deposit_btn = Button(self.historic,image=deposit_btn_image,bd=0,bg=color_box,activebackground=color_box,command=lambda:self.go_historic('deposit')).place(x=532,y=101)
            
            data_historic = dql(f"SELECT a.nome,valor,data FROM historico AS h JOIN alunos AS a ON remetente_cpf = cpf WHERE ação = 'Saque' AND cpf = '{super().user_cpf}'")
        
        elif type == 'deposit':
            bill_btn = Button(self.historic,image=bill_btn_image,bd=0,bg=color_box,activebackground=color_box,command=lambda:self.go_historic('bill')).place(x=70,y=101)
            transfer_btn = Button(self.historic,image=transfer_btn_image,bd=0,bg=color_box,activebackground=color_box,command=lambda:self.go_historic('transfer')).place(x=301,y=101)
            withdraw_btn = Button(self.historic,image=withdraw_btn_image,bd=0,bg=color_box,activebackground=color_box,command=lambda:self.go_historic('withdraw')).place(x=532,y=101)
            
            data_historic = dql(f"SELECT a.nome,valor,data FROM historico AS h JOIN alunos AS a ON remetente_cpf = cpf WHERE ação = 'Deposito' AND cpf = '{super().user_cpf}'")
        
        elif type == 'bill':
            deposit_btn = Button(self.historic,image=deposit_btn_image,bd=0,bg=color_box,activebackground=color_box,command=lambda:self.go_historic('deposit')).place(x=70,y=101)            
            transfer_btn = Button(self.historic,image=transfer_btn_image,bd=0,bg=color_box,activebackground=color_box,command=lambda:self.go_historic('transfer')).place(x=301,y=101)
            withdraw_btn = Button(self.historic,image=withdraw_btn_image,bd=0,bg=color_box,activebackground=color_box,command=lambda:self.go_historic('withdraw')).place(x=532,y=101)
            
            data_historic = dql(f"SELECT a.nome,valor,data FROM historico AS h JOIN alunos AS a ON remetente_cpf = cpf WHERE ação = 'Fatura' AND cpf = '{super().user_cpf}'")

        else:
            deposit_btn = Button(self.historic,image=deposit_btn_image,bd=0,bg=color_box,activebackground=color_box,command=lambda:self.go_historic('deposit')).place(x=70,y=101)            
            bill_btn = Button(self.historic,image=bill_btn_image,bd=0,bg=color_box,activebackground=color_box,command=lambda:self.go_historic('bill')).place(x=301,y=101)
            withdraw_btn = Button(self.historic,image=withdraw_btn_image,bd=0,bg=color_box,activebackground=color_box,command=lambda:self.go_historic('withdraw')).place(x=532,y=101)
            
            data_historic = dql(f"SELECT remetente.nome AS remetente, historico.valor, destinatario.nome AS destinatario, historico.data,historico.tipo_pg FROM historico JOIN alunos AS remetente ON historico.remetente_cpf = remetente.cpf JOIN alunos AS destinatario ON historico.destinatario_cpf = destinatario.cpf WHERE historico.remetente_cpf = '{super().user_cpf}' OR historico.destinatario_cpf = '{super().user_cpf}'")

        if type == 'withdraw' or type == 'deposit' or type == 'bill':
            self.tree = ttk.Treeview(self.historic,columns=('Nome','Valor','Data'),show='headings')
            self.tree.heading('Nome',text='Nome')
            self.tree.column('Nome',width=241,anchor='center')
            self.tree.heading('Valor',text='Valor')
            self.tree.column('Valor',width=245,anchor='center')
            self.tree.heading('Data',text='Data')
            self.tree.column('Data',width=155,anchor='center')
        else:
            self.tree = ttk.Treeview(self.historic,columns=('Remetente','Valor','Destinatário','Data','Tipo'),show='headings')
            self.tree.heading('Remetente',text='Remetente')
            self.tree.column('Remetente',width=169,anchor='center')
            self.tree.heading('Valor',text='Valor')
            self.tree.column('Valor',width=116,anchor='center')
            self.tree.heading('Destinatário',text='Destinatário')
            self.tree.column('Destinatário',width=169,anchor='center')
            self.tree.heading('Data',text='Data')
            self.tree.column('Data',width=104,anchor='center')
            self.tree.heading('Tipo',text='Tipo')
            self.tree.column('Tipo',width=84,anchor='center')
        
        for i,data in enumerate(data_historic):
            if i % 2 == 0:
                self.tree.insert('',END,values=data)
            else:
                self.tree.insert('',END,values=data,tags='diferent')
        
        self.tree.tag_configure('diferent',background='#6BA5F2')

        style.theme_use('default')
        style.configure('Treeview',background='#699BF7',foreground='#fff',font=('Inter',10),fieldbackground="#699BF7",rowheight=30)
        style.map('Treeview',background=[('selected','#96BAFB')])
        style.configure('Treeview.Heading',font=('Inter',-22),background='#699BF7',borderwidth=1)
        style.map('Treeview.Heading',background=[('active','#96BAFB')])
        self.tree.place(x=26,y=168,width=649,height=212)

        scrollbar = ttk.Scrollbar(self.tree, orient="vertical", command=self.tree.yview)
        scrollbar.pack(side="right", fill="y")

        self.tree.configure(yscrollcommand=scrollbar.set)


        text_seach = Label(self.historic,text='Pesquisar data:',font=('Inter',-15,'bold'),bg=color_box).place(x=36,y=398)
        self.entry_day = Entry(self.historic,justify='center',bd=0)
        self.entry_day.place(x=187,y=395,width=51,height=25)
        text_bar = Label(self.historic,text='/',font=('Inter',-32),bg=color_box).place(x=249,y=388)
        self.entry_moth = Entry(self.historic,justify='center',bd=0)
        self.entry_moth.place(x=267,y=395,width=51,height=25)
        text_bar = Label(self.historic,text='/',font=('Inter',-32),bg=color_box).place(x=326,y=388)
        self.entry_year = Entry(self.historic,justify='center',bd=0)
        self.entry_year.place(x=347,y=395,width=51,height=25)

        seach_btn = Button(self.historic,image=seach_btn_image,bd=0,bg=color_box,activebackground=color_box,command=lambda:self.seach_historic(type)).place(x=431,y=391)


        back_btn = Button(self.historic,image=back_btn_image,bd=0,bg=color_bg,activebackground=color_bg,command=self.go_homepage).place(x=14,y=446)

        self.historic.mainloop()
    

    def seach_historic(self,type):
        day = self.entry_day.get()
        moth = self.entry_moth.get()
        year = self.entry_year.get()

        if not day.isdigit() and day != '' and moth.isdigit() and moth != '' and year.isdigit() and year != '':
            messagebox.showerror('Erro',message='Digite a pesquisa corretamente')

        self.entry_day.delete(0,END)
        self.entry_moth.delete(0,END)
        self.entry_year.delete(0,END)

        self.tree.delete(*self.tree.get_children())
        wdb = ['withdraw','deposit','bill']
        if type in wdb:
            translate_type = ['Saque','Deposito','Fatura'][wdb.index(type)]
            linhas = dql(f"SELECT a.nome,valor,data FROM historico AS h JOIN alunos AS a ON remetente_cpf = cpf WHERE ação = '{translate_type}' AND cpf = '{super().user_cpf}' AND data LIKE '%{day}%/%{moth}%/%{year}%'")
        else:
            linhas = dql(f"SELECT remetente.nome AS remetente, historico.valor, destinatario.nome AS destinatario, historico.data,historico.tipo_pg FROM historico JOIN alunos AS remetente ON historico.remetente_cpf = remetente.cpf JOIN alunos AS destinatario ON historico.destinatario_cpf = destinatario.cpf WHERE historico.data LIKE '%{day}%/%{moth}%/%{year}%' AND (historico.remetente_cpf = '{super().user_cpf}' OR historico.destinatario_cpf = '{super().user_cpf}')")
        
        for i,data in enumerate(linhas):
            if i % 2 == 0:
                self.tree.insert('',END,values=data)
            else:
                self.tree.insert('',END,values=data,tags='diferent')

    
    def go_historic(self,type):
        self.historic.destroy()
        self.def_historic(type)


    def go_homepage(self):
        from homepage import homepage
        self.historic.destroy()
        homepage().homepage()

