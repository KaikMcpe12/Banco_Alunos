from function import *

class transfer(student_bench):
    def transfer(self):

        self.str_balance = StringVar()
        self.str_balance.set(super().user_infor[10])

        self.str_credit = StringVar()
        self.str_credit.set(super().user_infor[13])

        color_box = '#F2C299'
        color_blue_box = '#699BF7'
        color_bg = '#6BA5F2'

        self.color_user_sender = super().color_user
        self.color_user_adress = 0

        self.name_user_adress = StringVar()

        self.type_value = IntVar()

        bg_image = PhotoImage(master=super().app,file=super().folderAssets+'\\transfer\\background.png')
        title_image = PhotoImage(master=super().app,file=super().folderAssets+'\\transfer\\title.png')
        box_image = PhotoImage(master=super().app,file=super().folderAssets+'\\transfer\\box.png')
        blue_box_image = PhotoImage(master=super().app,file=super().folderAssets+'\\transfer\\blue_box.png')
        blue_box2_image = PhotoImage(master=super().app,file=super().folderAssets+'\\transfer\\blue_box2.png')
        real_box_image = PhotoImage(master=super().app,file=super().folderAssets+'\\transfer\\real_box.png')
        back_btn_image = PhotoImage(master=super().app,file=super().folderAssets+'\\transfer\\back_button.png')
        seach_btn_image = PhotoImage(master=super().app,file=super().folderAssets+'\\transfer\\seach_button.png')
        transfer_btn_image = PhotoImage(master=super().app,file=super().folderAssets+'\\transfer\\transfer_button.png')
        user_sender_image = PhotoImage(master=super().app,file=super().folderAssets+f'\\transfer\\user{self.color_user_sender}.png')
        self.user_adress_image = PhotoImage(master=super().app,file=super().folderAssets+f'\\transfer\\user{self.color_user_adress}.png')
        infor_btn_image = PhotoImage(master=super().app,file=super().folderAssets+'\\transfer\\infor_button.png')

        self.transfer = Frame(super().app,width=700,height=500)
        self.transfer.pack()


        backg = Canvas(self.transfer, width = 700,height = 500)
        backg.pack(fill = "both", expand = True)

        backg.create_image(0,0,image = bg_image,anchor = "nw")
        title = backg.create_image(13,25, image=title_image, anchor='nw')

        box = backg.create_image(13,87,image=box_image,anchor='nw')


        blue_box = Label(self.transfer,image=blue_box_image,bg=color_box).place(x=25,y=101)

        text_balance = Label(blue_box,text='Saldo:',bg=color_blue_box,font=('Inter',-21)).place(x=49,y=125)
        box_balance = Label(blue_box,image=real_box_image,bg=color_blue_box).place(x=45,y=152)
        self.balance = Label(box_balance,textvariable=self.str_balance,fg='#7F7F7F',font=('Inter',-23),bg='#fff')
        self.balance.place(x=85,y=159,height=23)

        text_credit = Label(blue_box,text='Crédito:',bg=color_blue_box,font=('Inter',-21)).place(x=432,y=125)
        box_credit = Label(blue_box,image=real_box_image,bg=color_blue_box).place(x=427,y=152)
        self.credit = Label(box_credit,textvariable=self.str_credit,fg='#7F7F7F',font=('Inter',-23),bg='#fff')
        self.credit.place(x=467,y=159,height=23)

        blue_box2 = Label(self.transfer,image=blue_box2_image,bg=color_box).place(x=25,y=237)

        user_sender = Label(blue_box2,image=user_sender_image,bg=color_blue_box).place(x=56,y=294)
        name_user_sender = Label(blue_box2,text=super().user_infor[2],bg=color_blue_box,font=('Montserrat',-11,'bold'),fg='#fff').place(x=35,y=384)

        self.user_adress = Label(blue_box2,image=self.user_adress_image,bg=color_blue_box)
        self.user_adress.place(x=240,y=294)
        name_user_adress = Label(blue_box2,textvariable=self.name_user_adress,bg=color_blue_box,font=('Montserrat',-11,'bold'),fg='#fff').place(x=221,y=384)


        text_adress = Label(self.transfer,text='N° do cartão do destinatário:',bg=color_box,font=('Inter',-12,'bold')).place(x=413,y=230)
        self.entry_adress = Entry(self.transfer,bd=0)
        self.entry_adress.place(x=413,y=251,width=195,height=21)

        text_value = Label(self.transfer,text='Valor a ser transferido:',bg=color_box,font=('Inter',-12,'bold')).place(x=413,y=283)
        self.sp_value = Spinbox(self.transfer,bd=0,from_=1,to=9999999)
        self.sp_value.place(x=413,y=304,width=195,height=21)

        text_plots = Label(self.transfer,text='Parecelas:',bg=color_box,font=('Inter',-12,'bold')).place(x=619,y=283)
        self.cb_plots = ttk.Combobox(self.transfer,values=[2,4,5,10,12])
        self.cb_plots.set(2)
        self.cb_plots.place(x=619,y=304,width=59,height=21)

        type_debit = Radiobutton(self.transfer,text='Débito',value='0',variable=self.type_value,bg=color_box,activebackground=color_box)
        type_debit.place(x=416,y=343)

        type_credit = Radiobutton(self.transfer,text='Crédito',value='1',variable=self.type_value,bg=color_box,activebackground=color_box)
        type_credit.place(x=480,y=343)

        infor_btn = Button(self.transfer,image=infor_btn_image,bg=color_box,activebackground=color_box,bd=0,command=self.infor_message).place(x=550,y=347)

        seach_btn = Button(self.transfer,image=seach_btn_image,bg=color_box,activebackground=color_box,bd=0,command=self.seach_adress).place(x=619,y=249)

        transfer_btn = Button(self.transfer,image=transfer_btn_image,bg=color_box,activebackground=color_box,bd=0,command=self.transfer_money).place(x=473,y=379)

        back_btn = Button(self.transfer,background=color_bg,activebackground=color_bg,bd=0,image=back_btn_image,command=self.go_homepage).place(x=13,y=446)

        self.transfer.mainloop()


    def infor_message(self):
         messagebox.showinfo(title='Informação sobre crréditos',message='Caso você tenha escolhido crédito como a forma de transferência, saiba que a sua fatura terá aumento de 5% do valor transferido')


    def seach_adress(self):
        try:
            adress = dql(f"SELECT cpf,nome,n_cartão FROM alunos WHERE n_cartão = '{self.entry_adress.get()}' AND n_cartão <> '{super().user_infor[11]}'")[0]
        except:
            messagebox.showerror(title='Erro',message='Digite um número de cartão válido')
            return
        else:
            self.color_user_adress = int(adress[2][-1]) // 2
            self.name_user_adress.set(adress[1])
            self.user_adress_image.config(file=super().folderAssets+f'\\transfer\\user{self.color_user_adress}.png')


    def transfer_money(self):
        data = dql(f"SELECT * FROM alunos WHERE n_cartão = '{self.entry_adress.get()}'")
        if not self.sp_value.get().isdigit() or not round(int(self.sp_value.get()),2) or not self.cb_plots.get().isdigit() or self.entry_adress.get()== '' or not data: #Verifica se valor digitado é número e se o mesmo possui duas cassas decimais, verifica se o campo de parcela é número e se o campo de número de cartão não está vazio
            messagebox.showerror(title='Erro',message='Preecha os dados corretamente')
            return
        
        dml(f"UPDATE alunos SET saldo = saldo+'{self.sp_value.get()}' WHERE n_cartão = '{self.entry_adress.get()}'")
        date_today = datetime.now().date()
        date_formated = date_today.strftime('%d/%m/%Y')

        if self.type_value.get() == 0 and int(self.sp_value.get()) <= super().user_infor[10]:
            dml(f"UPDATE alunos SET saldo = saldo-'{self.sp_value.get()}' WHERE cpf = '{super().user_cpf}'")
            dml(f"INSERT INTO historico(ação,remetente_cpf,valor,destinatario_cpf,data,tipo_pg) VALUES ('Transferência','{super().user_cpf}','{self.sp_value.get()}','{data[0][1]}','{date_formated}','Débito')")
            
            student_bench.user_infor = dql(f"SELECT * FROM alunos WHERE cpf = '{super().user_cpf}'")[0]
            self.str_balance.set(super().user_infor[10])

            messagebox.showinfo(title='Sucesso',message='Transferência por débito bem sucedida')

        elif self.type_value.get() == 1 and int(self.sp_value.get()) <= super().user_infor[13]: #Se o valor digitado é menor do que os créditos
            new_card_limit = round(int(self.sp_value.get()) * 1.05,2)
            dml(f"UPDATE alunos SET v_crédito = v_crédito-'{self.sp_value.get()}',limite_cartão = limite_cartão+'{new_card_limit}'  WHERE cpf = '{super().user_cpf}'")
            dml(f"INSERT INTO historico(ação,remetente_cpf,valor,destinatario_cpf,data,tipo_pg) VALUES ('Transferência','{super().user_cpf}','{self.sp_value.get()}','{data[0][1]}','{date_formated}','Crédito')")
            valor = round(int(self.sp_value.get())*1.05,2)
            v_parcela = round(valor/int(self.cb_plots.get()),2)
            dml(f"INSERT INTO h_fatura(cartão_user,valor,montante,parcelas,v_parcela,data,data_atualização) VALUES ('{super().user_infor[11]}','{valor}','{valor}','{self.cb_plots.get()}','{v_parcela}','{date_formated}','{date_formated}')")
        
            student_bench.user_infor = dql(f"SELECT * FROM alunos WHERE cpf = '{super().user_cpf}'")[0]
            self.str_credit.set(super().user_infor[13])

            messagebox.showinfo(title='Sucesso',message='Transferência por crédito bem sucedida')

        else:
            messagebox.showerror(title='Erro',message='Não é possivel transferir essa quantia de dinheiro')

    def go_homepage(self):
            from homepage import homepage
            self.transfer.destroy()
            homepage().homepage()
