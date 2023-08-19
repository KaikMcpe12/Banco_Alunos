from function import *

class register_list(student_bench):
    def register_list(self):

        color_box = '#F2C299'
        color_bg = '#6BA5F2'

        self.users_img = []
        users_list = dql(f"SELECT id,nome,n_cartão FROM alunos WHERE cpf <> '{super().user_cpf}'")

        bg_image = PhotoImage(master=super().app,file=super().folderAssets+'\\register_list\\background.png')
        title_image = PhotoImage(master=super().app,file=super().folderAssets+f'\\register_list\\title.png')
        box_image = PhotoImage(master=super().app,file=super().folderAssets+'\\register_list\\box.png')
        name_rect_image = PhotoImage(master=super().app,file=super().folderAssets+'\\register_list\\name_rectangle.png')
        seach_btn_image = PhotoImage(master=super().app,file=super().folderAssets+'\\register_list\\seach_button.png')
        see_people_btn_image = PhotoImage(master=super().app,file=super().folderAssets+'\\register_list\\see_people_button.png')
        user_b_image = PhotoImage(master=super().app,file=super().folderAssets+f'\\register_list\\user{super().color_user}_b.png')
        back_btn_image = PhotoImage(master=super().app,file=super().folderAssets+'\\profile\\back_button.png')
        
        for i in range(5):
            self.users_img.append(PhotoImage(master=super().app,file=super().folderAssets+f'\\register_list\\user{i}_s.png'))

        self.regs_list_f = Frame(super().app,width=700,height=500)
        self.regs_list_f.pack()

        fundo = Canvas(self.regs_list_f, width = 700,height = 500)
        fundo.pack(fill = "both", expand = True)

        fundo.create_image(0,0,image = bg_image,anchor = "nw")
        title = fundo.create_image(14,25, image=title_image, anchor='nw')

        box = fundo.create_image(14,87,image=box_image,anchor='nw')

        name_rect = Label(self.regs_list_f,image=name_rect_image,bg=color_box).place(x=26,y=97)
        user = Label(name_rect,image=user_b_image,bg='#fff').place(x=52,y=100)
        name_user = Label(name_rect,text=super().user_infor[2],font=('Inter',-20),fg='#699BF7',bg='#fff').place(x=120,y=110)

        style = ttk.Style()

        self.tree = ttk.Treeview(self.regs_list_f,columns=('ID','Nome','N° Cartão'),show='tree headings')
        self.tree.heading('#0',text='Foto')
        self.tree.column('#0',width=65,anchor='center')
        self.tree.heading('ID',text='ID')
        self.tree.column('ID',width=150,anchor='center')
        self.tree.heading('Nome',text='Nome')
        self.tree.column('Nome',width=220,anchor='center')
        self.tree.heading('N° Cartão',text='N° Cartão')
        self.tree.column('N° Cartão',width=214,anchor='center')

        style.theme_use('default')
        style.configure('Treeview',background='#699BF7',foreground='#fff',font=('Inter',10),fieldbackground="#699BF7",rowheight=30)
        style.map('Treeview',background=[('selected','#96BAFB')])
        style.configure('Treeview.Heading',font=('Inter',-22),background='#699BF7',borderwidth=1)
        style.map('Treeview.Heading',background=[('active','#96BAFB')])
        self.tree.place(x=26,y=168,width=649,height=212)

        scrollbar = ttk.Scrollbar(self.tree, orient="vertical", command=self.tree.yview)
        scrollbar.pack(side="right", fill="y")

        self.tree.configure(yscrollcommand=scrollbar.set)

        for i,user in enumerate(users_list):
            num = int(user[2][-1]) // 2
            if i % 2 == 0:
                self.tree.insert('',END,values=user,image=self.users_img[num])
            else:
                self.tree.insert('',END,values=user,tags='diferent',image=self.users_img[num])
        
        self.tree.tag_configure('diferent',background='#6BA5F2')

        text_seach = Label(self.regs_list_f,text='Pesquisar por nome:',font=('Inter',-15,'bold'),bg=color_box).place(x=26,y=394)
        self.entry_name = Entry(self.regs_list_f,bd=0)
        self.entry_name.place(x=193,y=392,width=199,height=25)

        seach_btn = Button(self.regs_list_f,bd=0,bg=color_box,image=seach_btn_image,activebackground=color_box,command=self.seach_people).place(x=409,y=387)

        see_people_btn = Button(self.regs_list_f,bd=0,bg=color_box,activebackground=color_box,image=see_people_btn_image,command=self.see_people).place(x=537,y=387)

        back_btn = Button(self.regs_list_f,image=back_btn_image,bd=0,bg=color_bg,activebackground=color_bg,command=self.go_profile).place(x=14,y=446)
        
        self.regs_list_f.mainloop()
        

    def seach_people(self):
        people = self.entry_name.get()
        self.entry_name.delete(0,END)

        self.tree.delete(*self.tree.get_children())

        users_list = dql(f"SELECT id,nome,n_cartão FROM alunos WHERE cpf <> '{super().user_cpf}' AND nome LIKE '%{people}%'")
        
        for i,user in enumerate(users_list):
            num = int(user[2][-1]) // 2
            if i % 2 == 0:
                self.tree.insert('',END,values=user,image=self.users_img[num])
            else:
                self.tree.insert('',END,values=user,tags='diferent',image=self.users_img[num])


    def see_people(self):
        select_item = self.tree.selection()[0]
        values = self.tree.item(item=select_item,option='values')

        if not values:
            messagebox.showerror(title='Erro',message='Selecione um usuário')

        select_user = dql(f"SELECT * FROM alunos WHERE n_cartão = '{values[2]}'")[0]
        self.go_profile(select_user)
    
    
    def go_profile(self,user=False):
        from profile import profile
        self.regs_list_f.destroy()
        if not user:
            profile().profile()
        else:
            profile().profile(user)