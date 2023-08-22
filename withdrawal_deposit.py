from function import *

class action(student_bench):
    def action(self,action):
        self.str_balance = StringVar()
        self.str_balance.set(super().user_infor[10])

        self.str_credit = StringVar()
        self.str_credit.set(super().user_infor[13])

        color_box = '#F2C299'
        color_blue_box = '#699BF7'
        color_bg = '#6BA5F2'

        bg_image = PhotoImage(master=super().app,file=super().folderAssets+'\\withdraw_deposit\\background.png')

        if action == 1:
            title_image = PhotoImage(master=super().app,file=super().folderAssets+'\\withdraw_deposit\\title_withdraw.png')
            withdraw_btn_image = PhotoImage(master=super().app,file=super().folderAssets+'\\withdraw_deposit\\withdraw_button.png')
        else:
            title_image = PhotoImage(master=super().app,file=super().folderAssets+'\\withdraw_deposit\\title_deposit.png')
            deposit_btn_image = PhotoImage(master=super().app,file=super().folderAssets+'\\withdraw_deposit\\deposit_button.png')
             
        box_image = PhotoImage(master=super().app,file=super().folderAssets+'\\withdraw_deposit\\box.png')
        back_btn_image = PhotoImage(master=super().app,file=super().folderAssets+'\\withdraw_deposit\\back_button.png')
        blue_box_image = PhotoImage(master=super().app,file=super().folderAssets+'\\withdraw_deposit\\blue_box.png')
        real_box_image = PhotoImage(master=super().app,file=super().folderAssets+'\\withdraw_deposit\\real_box.png')
        
        user_image = PhotoImage(master=super().app,file=super().folderAssets+f'\\withdraw_deposit\\user{super().color_user}.png')


        self.frame = Frame(super().app,width=700,height=500)
        self.frame.pack()

        backg = Canvas(self.frame, width = 700,height = 500)
        backg.pack(fill = "both", expand = True)
        backg.create_image(0,0,image = bg_image,anchor = "nw")

        title = backg.create_image(13,25, image=title_image, anchor='nw')

        box = backg.create_image(13,104,image=box_image,anchor='nw')

        blue_box = Label(self.frame,image=blue_box_image,bg=color_box).place(x=25,y=118)


        text_balance = Label(blue_box,text='Saldo:',font=('Inter',-21),bg=color_blue_box).place(x=49,y=142)
        box_balance = Label(blue_box,image=real_box_image,bg=color_blue_box).place(x=45,y=169)
        self.balance = Label(box_balance,textvariable=self.str_balance,fg='#7F7F7F',font=('Inter',-23),bg='#fff')
        self.balance.place(x=85,y=176,height=23)

        text_credit = Label(blue_box,text='Crédito:',font=('Inter',-21),bg=color_blue_box).place(x=432,y=142)
        box_credit = Label(blue_box,image=real_box_image,bg=color_blue_box).place(x=427,y=169)
        credit = Label(box_balance,textvariable=self.str_credit,fg='#7F7F7F',font=('Inter',-23),bg='#fff').place(x=467,y=176,height=23)

        user = Label(self.frame,image=user_image,bg=color_box).place(x=69,y=255)

        if action == 1:
            text_withdraw = Label(self.frame,text='Valor a ser sacado:',bg=color_box,font=('Inter',-16)).place(x=326,y=267)
        else:
            text_deposit = Label(self.frame,text='Valor a ser depositado:',bg=color_box,font=('Inter',-16)).place(x=326,y=267)
             
        self.sp_value = Spinbox(self.frame,from_=1,to=9999999,bd=0)
        self.sp_value.place(x=326,y=296,width=291,height=26)

        if action == 1:
            withdraw_btn = Button(self.frame,image=withdraw_btn_image,bg=color_box,activebackground=color_box,bd=0,command=lambda:self.action_money(1)).place(x=405,y=351)
        else:
            deposit_btn = Button(self.frame,image=deposit_btn_image,bg=color_box,activebackground=color_box,bd=0,command=lambda:self.action_money(2)).place(x=405,y=351)

        back_btn = Button(self.frame,background=color_bg,activebackground=color_bg,bd=0,image=back_btn_image,command=self.go_homepage).place(x=13,y=446)

        self.frame.mainloop()


    def action_money(self,action):
        if not self.sp_value.get().isdigit():
            messagebox.showerror(title='Erro',message='Digite apenas números')
            return
        
        date_today = datetime.now().date()
        date_formated = date_today.strftime('%d/%m/%Y')
        if action == 1:
            dml(f"UPDATE alunos SET saldo=saldo-'{self.sp_value.get()}' WHERE cpf='{super().user_cpf}'")
            dml(f"INSERT INTO historico (ação,remetente_cpf,valor,data) VALUES ('Saque','{student_bench.user_cpf}','{self.sp_value.get()}','{date_formated}')")
            messagebox.showinfo(title='Sucesso',message='Saque sucedido')
        else:
            dml(f"UPDATE alunos SET saldo=saldo+'{self.sp_value.get()}' WHERE cpf='{super().user_cpf}'")
            dml(f"INSERT INTO historico (ação,remetente_cpf,valor,data) VALUES ('Deposito','{student_bench.user_cpf}','{self.sp_value.get()}','{date_formated}')")
            messagebox.showinfo(title='Sucesso',message='Deposito sucedido')

        student_bench.user_infor = dql(f"SELECT * FROM alunos WHERE cpf = '{super().user_cpf}'")[0]
        self.str_balance.set(super().user_infor[10])


    def go_homepage(self):
            from homepage import homepage
            self.frame.destroy()
            homepage().homepage()