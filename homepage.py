from function import *


class homepage(student_bench):
    def homepage(self):

        color_box = '#F2C299'
        color_blue_box = '#699BF7'
        
        if super().color_user == 0:
            color_bg_text = '#FFCE1E'
        elif super().color_user == 1:
            color_bg_text = '#D99BFF'
        elif super().color_user == 2:
            color_bg_text = '#699BF7'
        elif super().color_user == 3:
            color_bg_text = '#434C57'
        else:
            color_bg_text = '#A02324'

        bg_image = PhotoImage(master=super().app,file=self.folderAssets+'\\homepage\\background.png')
        title_image = PhotoImage(master=super().app,file=self.folderAssets+'\\homepage\\title.png')
        box_image = PhotoImage(master=super().app,file=self.folderAssets+'\\homepage\\box.png')
        blue_box_image = PhotoImage(master=super().app,file=self.folderAssets+'\\homepage\\blue_box.png')
        back_btn_image = PhotoImage(master=super().app,file=self.folderAssets+'\\homepage\\back_button.png')
        withdraw_btn_image = PhotoImage(master=super().app,file=self.folderAssets+'\\homepage\\withdraw_btn.png')
        bill_btn_image = PhotoImage(master=super().app,file=self.folderAssets+'\\homepage\\bill_btn.png')
        deposit_btn_image = PhotoImage(master=super().app,file=self.folderAssets+'\\homepage\\deposit_btn.png')
        historic_btn_image = PhotoImage(master=super().app,file=self.folderAssets+'\\homepage\\historic_btn.png')
        transfer_btn_image = PhotoImage(master=super().app,file=self.folderAssets+'\\homepage\\transfer_btn.png')
        card_image = PhotoImage(master=super().app,file=self.folderAssets+f'\\homepage\\card{super().color_user}.png')
        real_box_image = PhotoImage(master=super().app,file=self.folderAssets+'\\homepage\\real_box.png')

        self.homepage = Frame(super().app,width=700,height=500)
        self.homepage.pack()

        backg = Canvas(self.homepage, width = 700,height = 500)
        backg.pack(fill = "both", expand = True)

        backg.create_image(0,0,image = bg_image,anchor = "nw")
        title = backg.create_image(12,12, image=title_image, anchor='nw')

        box = backg.create_image(12,78,image=box_image,anchor='nw')

        back_btn = Button(self.homepage,background=color_box,activebackground=color_box,bd=0,image=back_btn_image,command=self.close_account).place(x=31,y=19)

        blue_box = Label(self.homepage,image=blue_box_image,bg=color_box).place(x=22,y=89)

        card = Label(blue_box,image=card_image,bg=color_blue_box)
        card.place(x=64,y=92)
        card_number = Label(card,text=super().user_infor[11],bg=color_bg_text,fg='#fff',font=('Montserrat',-16)).place(x=15,y=126)
        card_bith = Label(card,text=super().user_infor[3][:5],bg=color_bg_text,fg='#fff',font=('Montserrat',-16)).place(x=78,y=151)
        card_name = Label(card,text=super().user_infor[2],bg=color_bg_text,fg='#fff',font=('Montserrat',-16)).place(x=15,y=173)

        card.bind("<Button-1>", self.go_profile)

        text_balance = Label(blue_box,text='Saldo:',font=('Inter',-21),bg=color_blue_box).place(x=410,y=140)
        box_balance = Label(blue_box,image=real_box_image,bg=color_blue_box).place(x=406,y=167)
        balance = Label(box_balance,text=super().user_infor[10],fg='#7F7F7F',font=('Inter',-23),bg='#fff').place(x=446,y=174,height=23)

        text_credit = Label(blue_box,text='Crédito:',font=('Inter',-21),bg=color_blue_box).place(x=410,y=222)
        box_credit = Label(blue_box,text='',image=real_box_image,bg=color_blue_box).place(x=406,y=249)
        credit = Label(box_balance,text=super().user_infor[13],fg='#7F7F7F',font=('Inter',-23),bg='#fff').place(x=446,y=256,height=23)
        text_limit = Label(blue_box,text=f'Limite: R$ {super().user_infor[12]}',font=('Inter',-12),bg=color_blue_box).place(x=410,y=287)

        withdraw_btn = Button(self.homepage,image=withdraw_btn_image,bd=0,bg=color_box,activebackground=color_box,command=self.go_withdraw).place(x=31,y=328)

        bill_btn = Button(self.homepage,image=bill_btn_image,bd=0,bg=color_box,activebackground=color_box,command=self.go_bill).place(x=276,y=328)

        deposit_btn = Button(self.homepage,image=deposit_btn_image,bd=0,bg=color_box,activebackground=color_box,command=self.go_deposit).place(x=519,y=328)

        historic_btn = Button(self.homepage,image=historic_btn_image,bd=0,bg=color_box,activebackground=color_box,command=self.go_historic).place(x=157,y=401)

        transfer_btn = Button(self.homepage,image=transfer_btn_image,bd=0,bg=color_box,activebackground=color_box,command=self.go_transfer).place(x=406,y=401)
        
        self.update_bill_data()

        self.homepage.mainloop()


    def close_account(self):
        res = messagebox.askyesno(title='Sair da conta',message='Deseja realmente sair da conta?')
        if res:
            self.go_home()

    
    def go_home(self):
            from home import home
            self.homepage.destroy()
            home().home()

    
    def go_withdraw(self):
            from withdrawal_deposit import action
            self.homepage.destroy()
            action().action(1)

        
    def go_deposit(self):
            from withdrawal_deposit import action
            self.homepage.destroy()
            action().action(2)


    def go_transfer(self):
            from transfer import transfer
            self.homepage.destroy()
            transfer().transfer()


    def go_historic(self):
        from historic import historic
        self.homepage.destroy()
        historic().def_historic()


    def go_bill(self):
         from bill import bill
         self.homepage.destroy()
         bill().bill()

        
    def go_profile(self,event):
        from profile import profile
        self.homepage.destroy()
        profile().profile()


    def update_bill_data(self):
        data = dql(f"SELECT * FROM h_fatura WHERE cartão_user = '{super().user_infor[11]}'")
        if data:
            data_biil = data[0]
            update_date_bill = datetime.strptime(data_biil[6],"%d/%m/%Y").date()
            date_today = datetime.now().date()

            different_days = date_today - update_date_bill
            moth_interval = different_days.days//30

            date_formated = date_today.strftime('%d/%m/%Y')
            if moth_interval >= 1:
                new_amout = round(data_biil[2] * 1.05**moth_interval,2)
                dml(f"UPDATE h_fatura SET montante = '{new_amout}', v_parcela = '{round(new_amout/data_biil[3],2)}' ,data_atualização = '{date_formated}' WHERE cartão_user = '{super().user_infor[11]}'")
                messagebox.showerror(title='Atenção',message='Sua fatura foi atualizada!')
            # elif moth_interval >= 3:
            #     messagebox.showerror(title='Atenção',message='Sua conta foi apagada por ter superado a data da fatura que são três meses')
            #     dml(f"DELETE FROM alunos WHERE cpf = '{super().user_cpf}'")
            #     dml(f"DELETE FROM h_fatura WHERE cartão_user = '{super().user_infor[11]}'")
            #     self.go_home()