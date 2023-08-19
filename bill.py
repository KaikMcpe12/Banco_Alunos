from function import *

class bill(student_bench):
    def bill(self):
        color_box = '#F2C299'
        color_blue_box = '#699BF7'
        color_bg = '#6BA5F2'
        self.page = 0

        self.initial_value = StringVar()
        self.amount = StringVar()
        self.num_plots = StringVar()
        self.value_plot = StringVar()
        self.dates = StringVar()
        
        self.bill_historic = dql(f"SELECT id_fatura,valor,montante,parcelas,v_parcela,data,data_atualização FROM h_fatura WHERE cartão_user = '{super().user_infor[11]}'")

        if self.page == len(self.bill_historic)-1 or len(self.bill_historic) == 0:
            self.next_btn_active = 0
        else:
            self.next_btn_active = 1
        self.previsous_btn_active = 0

        bg_image = PhotoImage(master=super().app,file=super().folderAssets+'\\bill\\background.png')
        title_image = PhotoImage(master=super().app,file=super().folderAssets+f'\\bill\\title.png')
        box_image = PhotoImage(master=super().app,file=super().folderAssets+'\\bill\\box.png')
        back_btn_image = PhotoImage(master=super().app,file=super().folderAssets+'\\bill\\back_button.png')
        box2_image = PhotoImage(master=super().app,file=super().folderAssets+'\\bill\\box2.png')
        infor_box_image = PhotoImage(master=super().app,file=super().folderAssets+f'\\bill\\infor_box{super().color_user}.png')
        self.next_btn_image = PhotoImage(master=super().app,file=super().folderAssets+f'\\bill\\next_button{self.next_btn_active}.png')
        self.previous_btn_image = PhotoImage(master=super().app,file=super().folderAssets+f'\\bill\\previous_button{self.previsous_btn_active}.png')
        pay_btn_image = PhotoImage(master=super().app,file=super().folderAssets+'\\bill\\pay_button.png')
        value_box_image = PhotoImage(master=super().app,file=super().folderAssets+'\\bill\\value_box.png')

        self.bill_f = Frame(super().app,width=700,height=500)
        self.bill_f.pack()

        fundo = Canvas(self.bill_f, width = 700,height = 500)
        fundo.pack(fill = "both", expand = True)

        fundo.create_image(0,0,image = bg_image,anchor = "nw")
        title = fundo.create_image(14,25, image=title_image, anchor='nw')

        box = fundo.create_image(14,87,image=box_image,anchor='nw')

        self.previous_btn = Button(self.bill_f,image=self.previous_btn_image,bg=color_box,activebackground=color_box,bd=0)
        self.previous_btn.place(x=24,y=236)
        
        if self.next_btn_active:
            self.next_btn = Button(self.bill_f,image=self.next_btn_image,bg=color_box,activebackground=color_box,bd=0,command=self.next_page)
        else:
            self.next_btn = Button(self.bill_f,image=self.next_btn_image,bg=color_box,activebackground=color_box,bd=0)

        self.next_btn.place(x=636,y=236)

        infor_box = Label(self.bill_f,bg=color_box,image=infor_box_image).place(x=80,y=93)

        if self.bill_historic:
            self.initial_value.set(self.bill_historic[self.page][1])
            self.amount.set(self.bill_historic[self.page][2])
            self.num_plots.set(self.bill_historic[self.page][3])
            self.value_plot.set(self.bill_historic[self.page][4])
            self.dates.set(f'{self.bill_historic[self.page][5]} - {self.bill_historic[self.page][6]}')

            text_value1 = Label(infor_box,text='Valor inicial:',bg=color_blue_box,font=('Inter',-21,'bold')).place(x=100,y=181)
            box_value1 = Label(infor_box,image=value_box_image,bg=color_blue_box).place(x=93,y=208)
            value1 = Label(box_value1,bg='#fff',fg='#7F7F7F',textvariable=self.initial_value,font=('Inter',-17)).place(x=137,y=216)

            text_amount = Label(infor_box,text='Montante:',bg=color_blue_box,font=('Inter',-21,'bold')).place(x=406,y=181)
            box_amount = Label(infor_box,image=value_box_image,bg=color_blue_box).place(x=393,y=208)
            amount_val = Label(box_amount,bg='#fff',fg='#7F7F7F',textvariable=self.amount,font=('Inter',-17)).place(x=437,y=216)

            text_num_plots = Label(infor_box,text='Quantidades de parcelas:',bg=color_blue_box,font=('Inter',-21,'bold')).place(x=100,y=260)
            box_num_plots = Label(infor_box,image=box2_image,bg=color_blue_box).place(x=93,y=286)
            num_plots_val = Label(box_num_plots,bg='#fff',fg='#7F7F7F',textvariable=self.num_plots,font=('Inter',-17)).place(x=117,y=294)

            text_value_plot = Label(infor_box,text='Valor da parcela:',bg=color_blue_box,font=('Inter',-21,'bold')).place(x=406,y=260)
            box_value_plot = Label(infor_box,image=value_box_image,bg=color_blue_box).place(x=393,y=286)
            value_plot_val = Label(box_value_plot,bg='#fff',fg='#7F7F7F',textvariable=self.value_plot,font=('Inter',-17)).place(x=437,y=294)

            date = Label(infor_box,bg=color_blue_box,font=('Inter',-12,'bold'),textvariable=self.dates).place(x=286,y=356)
        
        else:
            warning_text = Label(infor_box,bg=color_blue_box,text='Nenhuma fatura disponivel',font=('Inter',-32,'bold')).place(x=144,y=240)


        pay_btn = Button(self.bill_f,bg=color_box,activebackground=color_box,image=pay_btn_image,bd=0,command=self.pay_bill).place(x=281,y=393)

        back_btn = Button(self.bill_f,image=back_btn_image,bd=0,bg=color_bg,activebackground=color_bg,command=self.go_homepage).place(x=14,y=446)

        self.bill_f.mainloop()

    
    def next_page(self):
        self.page += 1
        self.previsous_btn_active = 1
        self.previous_btn_image.config(file=super().folderAssets+f'\\bill\\previous_button{self.previsous_btn_active}.png')
        self.previous_btn.config(command=self.previous_page)

        self.initial_value.set(self.bill_historic[self.page][1])
        self.amount.set(self.bill_historic[self.page][2])
        self.num_plots.set(self.bill_historic[self.page][3])
        self.value_plot.set(self.bill_historic[self.page][4])
        self.dates.set(f'{self.bill_historic[self.page][5]} - {self.bill_historic[self.page][6]}')
        
        if self.page == len(self.bill_historic)-1:
            self.next_btn_active = 0
            self.next_btn.config(command=False)

        self.next_btn_image.config(file=super().folderAssets+f'\\bill\\next_button{self.next_btn_active}.png')

    
    def previous_page(self):
        self.page -= 1
        self.next_btn_active = 1
        self.next_btn_image.config(file=super().folderAssets+f'\\bill\\next_button{self.next_btn_active}.png')
        self.next_btn.config(command=self.next_page)

        self.initial_value.set(self.bill_historic[self.page][1])
        self.amount.set(self.bill_historic[self.page][2])
        self.num_plots.set(self.bill_historic[self.page][3])
        self.value_plot.set(self.bill_historic[self.page][4])
        self.dates.set(f'{self.bill_historic[self.page][5]} - {self.bill_historic[self.page][6]}')

        if self.page == 0:
            self.previsous_btn_active = 0
            self.previous_btn.config(command=False)
        
        self.previous_btn_image.config(file=super().folderAssets+f'\\bill\\previous_button{self.previsous_btn_active}.png')

    
    def pay_bill(self):
        if not self.bill_historic:
            messagebox.showerror(title='Erro',message='Você não tem fatura disponivel')
            return

        if super().user_infor[10] < self.bill_historic[self.page][2]:
            messagebox.showerror(title='Erro',message='Seu saldo não é o bastante')

        date_today = datetime.now().date()
        date_formated = date_today.strftime('%d/%m/%Y')

        new_value = round(self.bill_historic[self.page][2] - self.bill_historic[self.page][4],2)
        new_plot = self.bill_historic[self.page][3] - 1

        value_user = round(super().user_infor[10]-self.bill_historic[self.page][4],2)
        if new_value == 0:
            new_value_plot = 0
        else:
            new_value_plot = round(new_value / new_plot,2)

        dml(f"INSERT INTO historico(ação,remetente_cpf,valor,data) VALUES ('Fatura','{super().user_cpf}','{self.bill_historic[self.page][4]}','{date_formated}')")
        dml(f"UPDATE alunos SET saldo = '{value_user}' WHERE cpf = '{super().user_cpf}'")
        dml(f"UPDATE h_fatura SET valor = '{new_value}',montante = '{new_value}', parcelas = '{new_plot}', v_parcela = '{new_value_plot}', data_atualização = '{date_formated}' WHERE cartão_user = '{super().user_infor[11]}' AND id_fatura = '{self.bill_historic[self.page][0]}'")

        if dql(f"SELECT valor FROM h_fatura WHERE cartão_user = '{super().user_infor[11]}'")[0][0] == 0:
            dml(f"DELETE FROM h_fatura WHERE cartão_user = '{super().user_infor[11]}' AND id_fatura = '{self.bill_historic[self.page][0]}'")

        if not dql(f"SELECT valor FROM h_fatura WHERE cartão_user = '{super().user_infor[11]}'"):
            dml(f"UPDATE alunos SET v_crédito = limite_cartão WHERE cpf = '{super().user_cpf}'")

        student_bench.user_infor = dql(f"SELECT * FROM alunos WHERE cpf = '{super().user_cpf}'")[0]
        
        self.bill_f.destroy()
        self.bill()

    
    def go_homepage(self):
        from homepage import homepage
        self.bill_f.destroy()
        homepage().homepage()
