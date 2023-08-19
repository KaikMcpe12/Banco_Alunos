from function import *

class profile(student_bench):
    def profile(self,user=student_bench.user_infor):
        color_box = '#F2C299'
        color_blue_box = '#699BF7'
        color_bg = '#6BA5F2'

        color_user_temp = int(user[11][-1]) // 2

        bg_image = PhotoImage(master=super().app,file=super().folderAssets+'\\profile\\background.png')
        title_image = PhotoImage(master=super().app,file=super().folderAssets+f'\\profile\\title.png')
        box_image = PhotoImage(master=super().app,file=super().folderAssets+'\\profile\\box.png')
        frame_image = PhotoImage(master=super().app,file=super().folderAssets+f'\\profile\\frame{color_user_temp}.png')
        more_people_image = PhotoImage(master=super().app,file=super().folderAssets+'\\profile\\more_people.png')
        back_btn_image = PhotoImage(master=super().app,file=super().folderAssets+'\\profile\\back_button.png')

        self.profile_f = Frame(super().app,width=700,height=500)
        self.profile_f.pack()

        fundo = Canvas(self.profile_f, width = 700,height = 500)
        fundo.pack(fill = "both", expand = True)

        fundo.create_image(0,0,image = bg_image,anchor = "nw")
        title = fundo.create_image(14,25, image=title_image, anchor='nw')

        box = fundo.create_image(14,87,image=box_image,anchor='nw')

        frame = Label(self.profile_f,image=frame_image,bg=color_box).place(x=18,y=104)

        text_name = Label(frame,text='Nome:',bg=color_blue_box,font=('Inter',-16,'bold')).place(x=104,y=125)
        text_gender = Label(frame,text='Sexo:',bg=color_blue_box,font=('Inter',-16,'bold')).place(x=466,y=125)
        text_local = Label(frame,text='Local:',bg=color_blue_box,font=('Inter',-16,'bold')).place(x=104,y=157)
        text_phone = Label(frame,text='Telefone:',bg=color_blue_box,font=('Inter',-16,'bold')).place(x=466,y=157)
        text_card = Label(frame,text='N° do cartão:',bg=color_blue_box,font=('Inter',-16,'bold')).place(x=126,y=189)
        text_real = Label(frame,text='Saldo:',bg=color_blue_box,font=('Inter',-16,'bold')).place(x=466,y=189)
        text_email = Label(frame,text='Email:',bg=color_blue_box,font=('Inter',-16,'bold')).place(x=158,y=221)
        text_credit = Label(frame,text='Crédito:',bg=color_blue_box,font=('Inter',-16,'bold')).place(x=466,y=221)
        text_passw = Label(frame,text='Senha:',bg=color_blue_box,font=('Inter',-16,'bold')).place(x=162,y=253)
        text_about = Label(frame,text='Sobre:',bg=color_blue_box,font=('Inter',-16,'bold')).place(x=174,y=285)
        text_number = Label(frame,text='N°:',bg=color_blue_box,font=('Inter',-16,'bold')).place(x=104,y=386)
        text_cpf = Label(frame,text='CPF:',bg=color_blue_box,font=('Inter',-16,'bold')).place(x=495,y=386)

        name_user = Label(frame,text=user[2],bg=color_blue_box,fg='#fff',font=('Inter',-16)).place(x=158,y=125)
        gender_user = Label(frame,text=user[6],bg=color_blue_box,fg='#fff',font=('Inter',-16)).place(x=512,y=125)
        local_user = Label(frame,text=user[5],bg=color_blue_box,fg='#fff',font=('Inter',-16)).place(x=154,y=157)
        phone_user = Label(frame,text=user[4],bg=color_blue_box,fg='#fff',font=('Inter',-14)).place(x=541,y=157)
        card_user = Label(frame,text=user[11],bg=color_blue_box,fg='#fff',font=('Inter',-14)).place(x=233,y=191)
        real_user = Label(frame,text=f'R$ {user[10]}',bg=color_blue_box,fg='#fff',font=('Inter',-14)).place(x=519,y=191)
        credit_user = Label(frame,text=f'R$ {user[13]}',bg=color_blue_box,fg='#fff',font=('Inter',-14)).place(x=531,y=222)
        about_user = Label(frame,text=user[9],bd=1,relief='solid',anchor='nw',font=('Inter',-14),padx=2).place(x=176,y=309,width=490,height=70)
        number_user = Label(frame,text=user[0],bg=color_blue_box,fg='#fff',font=('Inter',-16)).place(x=140,y=386)
        birthday_user = Label(frame,text=user[3],bg=color_blue_box,font=('Inter',-12)).place(x=318,y=402)
        
        if user == super().user_infor: #Verifica se está acessando o próprio usuario ou se é outro usuario
            cpf_user = Label(frame,text=user[1],bg=color_blue_box,fg='#fff',font=('Inter',-16)).place(x=537,y=386)
            email_user = Label(frame,text=user[7],bg=color_blue_box,fg='#fff',font=('Inter',-15)).place(x=208,y=221)
            passw_user = Label(frame,text=user[8],bg=color_blue_box,fg='#fff',font=('Inter',-14)).place(x=219,y=255)


        back_btn = Button(self.profile_f,image=back_btn_image,bd=0,bg=color_bg,activebackground=color_bg,command=self.go_homepage).place(x=14,y=446)

        more_people_btn = Button(self.profile_f,bg=color_bg,activebackground=color_bg,image=more_people_image,bd=0,command=self.go_register_list).place(x=527,y=446)

        self.profile_f.mainloop()
    

    def go_homepage(self):
        from homepage import homepage
        self.profile_f.destroy()
        homepage().homepage()

    def go_register_list(self):
        from register_list import register_list
        self.profile_f.destroy()
        register_list().register_list()