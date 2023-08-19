from function import *
from tkinter import font

class information(student_bench):
    def information(self):
        bg_image = PhotoImage(master=super().app,file=super().folderAssets+'\\information\\background.png')
        title_image = PhotoImage(master=super().app,file=super().folderAssets+'\\information\\title.png')
        box_image = PhotoImage(master=super().app,file=super().folderAssets+'\\information\\box.png')
        back_btn_image = PhotoImage(master=super().app,file=super().folderAssets+'\\information\\back_button.png')

        text_fontB = font.Font(family='Inter',weight='bold',size=-12)
        text_fontN = font.Font(family='Inter',size=-12)

        box_color = '#F2C299'

        txt1 = 'O banco alunos é um projeto educacional visando aprimorar conhecimentos sobre\npython, biblioteca de interface gráfica TKinter e de banco de dados SQLite , feita por \nmim, Kaik. Meu propósito é deixar a aplicação visualmente e mecanicamente simples,\nmas que agrade o usuário'
        txt_subtitle = 'Suas páginas são:'
        txt_list_pages = '• Pagina inicial: que ficará responsável pela primeira interação com o usuário\n• Página de cadatros: para inserir os dados de um usuário iniciante\n• Página entrar: para um usuário já cadastrado\n• Home: a primeira tela após entrar com uma conta ou cadastrar\n• Perfil: para o usuário ver suas informações\n• Página de depósito,saque, transferência e pagamento: para realizar ações da conta\n• Lista de cadastros: lista de pessoas cadastradas'
        txt_subtitle2 = 'Nota:'
        txt2 = 'Poderia ser usado o Custom TKiter que é uma versão avançaçado do que o próprio\nTKinter, mas optei por usar o classico TKinter, por isso o uso excessivo de images'
        txt_infor = 'Autor: Francisco Kaik\nData: ?/07/2023'

        self.infor = Frame(super().app, width = 700,height = 500)
        self.infor.pack()

        bg = Canvas(self.infor, width = 700,height = 500)
        bg.pack(fill = "both", expand = True)

        bg.create_image(0,0,image = bg_image,anchor = "nw")

        title = bg.create_image(87,13, image=title_image, anchor='nw')
        box = bg.create_image(87,80,image=box_image,anchor='nw')

        text_box1 = Label(self.infor,text=txt1,justify='left',bg=box_color,font=text_fontN).place(x=108,y=94)
        subtitle = Label(self.infor,text=txt_subtitle,justify='left',bg=box_color,font=text_fontB).place(x=108,y=169)
        list_pages = Label(self.infor,text=txt_list_pages,justify='left',bg=box_color,font=text_fontN).place(x=108,y=199)
        subtitle2 = Label(self.infor,text=txt_subtitle2,justify='left',bg=box_color,font=text_fontB).place(x=108,y=319)
        text_box2 = Label(self.infor,text=txt2,justify='left',bg=box_color,font=text_fontN).place(x=108,y=349)
        txt_infor_box = Label(self.infor,text=txt_infor,justify='left',bg=box_color,font=text_fontN).place(x=108,y=394)

        back_btn = Button(self.infor,image=back_btn_image,bg='#6BA5F2',activebackground='#6BA5F2',bd=0,command=self.go_home).place(x=87,y=449)

        self.infor.mainloop()


    def go_home(self):
            from home import home
            self.infor.destroy()
            home().home()