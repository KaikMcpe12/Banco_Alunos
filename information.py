from function import *
from tkinter import font

class information(student_bench):
    def information(self):
        
        color_box = '#F2C299'
        color_bg = '#6BA5F2'

        style = ttk.Style()
        style.theme_use('default')
        style.configure('TNotebook',tabmargins=0,borderwidth=0,background=color_box,relief='solid')
        style.configure("TNotebook.Tab",padding=[5, 1],background=color_bg,foreground='#fff',borderwidth=1,font=('Inter',-11,'bold'))
        style.map("TNotebook.Tab",background=[("selected", color_box)],expand=[("selected", [1, 1, 1, 0])])

        bg_image = PhotoImage(master=super().app,file=super().folderAssets+'\\information\\background.png')
        title_image = PhotoImage(master=super().app,file=super().folderAssets+'\\information\\title.png')
        box_image = PhotoImage(master=super().app,file=super().folderAssets+'\\information\\box.png')
        back_btn_image = PhotoImage(master=super().app,file=super().folderAssets+'\\information\\back_button.png')

        text_fontB = font.Font(family='Inter',weight='bold',size=-12)
        text_fontN = font.Font(family='Inter',size=-12)

        self.infor = Frame(super().app, width = 700,height = 500)
        self.infor.pack()

        bg = Canvas(self.infor, width = 700,height = 500)
        bg.pack(fill = "both", expand = True)

        bg.create_image(0,0,image = bg_image,anchor = "nw")

        title = bg.create_image(87,13, image=title_image, anchor='nw')
        self.box = Label(self.infor,image=box_image,anchor='nw',bg=color_bg)
        self.box.place(x=87,y=83)

        note = ttk.Notebook(self.infor)
        note.place(x=94,y=80)

        inf = Frame(note,bg=color_box,width=490,height=335)
        note.add(inf,text='Infor')

        ini = Frame(note,bg=color_box,width=490,height=335)
        note.add(ini,text='Ini.')

        regs = Frame(note,bg=color_box,width=490,height=335)
        note.add(regs,text='Cadas.')

        enter = Frame(note,bg=color_box,width=490,height=335)
        note.add(enter,text='Entrar')

        home = Frame(note,bg=color_box,width=490,height=335)
        note.add(home,text='Home')

        prf_bill = Frame(note,bg=color_box,width=490,height=335)
        note.add(prf_bill,text='Perfil|Fatura')

        with_depo = Frame(note,bg=color_box,width=490,height=335)
        note.add(with_depo,text='Saque|deposito')

        transfer = Frame(note,bg=color_box,width=490,height=335)
        note.add(transfer,text='Transf.')

        hist_list = Frame(note,bg=color_box,width=490,height=335)
        note.add(hist_list,text='Hist.|Lista')

        ####################################################################################################################################
        #Inf
        ####################################################################################################################################
        txt1_inf = 'O banco alunos é um projeto educacional visando aprimorar conhecimentos sobre\npython, biblioteca de interface gráfica TKinter e de banco de dados SQLite , feita por \nmim, Kaik. Meu propósito é deixar a aplicação visualmente e mecanicamente simples,\nmas que agrade o usuario'
        txt_subtitle_inf = 'Suas páginas são:'
        txt_list_pages_inf = '• Pagina inicial: que ficará responsável pela primeira interação com o usuario\n• Página de cadatros: para inserir os dados de um usuario iniciante\n• Página entrar: para um usuario já cadastrado\n• Home: a primeira tela após entrar com uma conta ou cadastrar\n• Perfil: para o usuario ver suas informações\n• Página de depósito,saque, transferência e pagamento: para realizar ações da conta\n• Lista de cadastros: lista de pessoas cadastradas'
        txt_subtitle2_inf = 'Nota:'
        txt2_inf = 'Poderia ser usado o Custom TKiter que é uma versão avançaçado do que o próprio\nTKinter, mas optei por usar o classico TKinter, por isso o uso excessivo de images'
        txt_author_inf = 'Autor: Francisco Kaik\nData: ?/07/2023'

        txt_box_inf = Label(inf,text=txt1_inf,justify='left',bg=color_box,font=text_fontN).grid(row=0,column=0,pady=(5,0))
        subtitle_box_inf = Label(inf,text=txt_subtitle_inf,justify='left',bg=color_box,font=text_fontB).grid(row=1,column=0,pady=(5,0),sticky='w')
        list_pages_box_inf = Label(inf,text=txt_list_pages_inf,justify='left',bg=color_box,font=text_fontN).grid(row=2,column=0,pady=(5,0))
        subtitle2_box_inf = Label(inf,text=txt_subtitle2_inf,justify='left',bg=color_box,font=text_fontB).grid(row=3,column=0,pady=(5,0),sticky='w')
        txt_box2_inf = Label(inf,text=txt2_inf,justify='left',bg=color_box,font=text_fontN).grid(row=4,column=0,pady=(5,0),sticky='w')
        txt_author_box_inf = Label(inf,text=txt_author_inf,justify='left',bg=color_box,font=text_fontN).grid(row=5,column=0,pady=(20,0),sticky='w')

        ####################################################################################################################################
        #Ini
        ####################################################################################################################################
        txt_subtitle_ini = 'Tela inicial'
        txt1_ini = 'A tela inicial é a mais marcante, pois simboliza o ínicio de tudo e só pela aparência é\nconsiderado facil, mas no fundo foi a tela que mais tive problemas, já que o modo em que\ndecidi fazer sai totalmente do que eu queria e a parti dessa tela aprendi uma  nova forma de\nprogramar.'
        txt2_ini = 'Para fazer essa e outras telas futuras usei muitas imagens e para mim no ínicio\nfoi algo negativo já que iria depender mais de imagens do que a estilização do TKinter,\nprocurei varias formas de fazer o que eu queria usando apenas o TKinter, mas não\nencontrei, depois de um tempo pensando decidi usar imagens já que o próprio TKinter no\nmeu caso é limitado, mas acredito que meu nível de conhecimento que é limitado sobre o\nuso da ferramenta'
        txt_subtitle2_ini = 'Telas'
        txt_list_pages_ini = '• Entrar: Tela responsável por fazer a entrada do usuario e de pegar os dados do respectivo\n  usuario\n• Cadastarar: Tela responsável por cadastrar um novo usuario, enviando os dados para o\n  banco de dados\n• Informações: Tela responsável por disponibilizar as informações sobre o projeto, que é\n  essa mesma tela'

        txt_subtitle_box_ini = Label(ini,text=txt_subtitle_ini,justify='left',bg=color_box,font=text_fontB).grid(row=0,column=0,pady=(5,0),sticky='w')
        txt1_box_ini = Label(ini,text=txt1_ini,justify='left',bg=color_box,font=text_fontN).grid(row=1,column=0,pady=(5,0),sticky='w')
        txt2_box_ini = Label(ini,text=txt2_ini,justify='left',bg=color_box,font=text_fontN).grid(row=2,column=0,pady=(5,0),sticky='w')
        txt_subtitle2_box_ini = Label(ini,text=txt_subtitle2_ini,justify='left',bg=color_box,font=text_fontB).grid(row=3,column=0,pady=(5,0),sticky='w')
        txt_list_pages_box_ini = Label(ini,text=txt_list_pages_ini,justify='left',bg=color_box,font=text_fontN).grid(row=4,column=0,pady=(5,0),sticky='w')
        ####################################################################################################################################
        #Regs
        ####################################################################################################################################
        txt_subtitle_regs = 'Cadastro'
        txt1_regs = 'A tela de registro é principal tela em que toda pessoa que entra na aplicação pela primeira\nvez verá, já que terá que fazer o cadastro para entra, primeiramente essa tela é a que possui\nmais campos e até alguns não parecem terem em um app de banco real, no caso\no campo SOBRE, mas ressaltando que essa aplicação é só para uso didático'
        txt2_regs = 'Parece muito cansativo preecher todos esses campos principalmente por causa desses\ncampos serem obrigatórios, com excessão do campo SOBRE,mas eu precisava desses\ndados, além de existir um campo que não será preenchido pelo usuario, mas sim gerado\naleatoriamente, no caso o número do cartão. Uma funcionalidade (que é a que mais gosto\npor ser simples) que tem nessa tela e a de entrada é a de visualizador de senha, que por\nparecer simples é muito interessante a sua mecânica'
        txt3_regs = 'Após os dados obrigatórios serem preenchidos é possivel fazer o cadastro, clicando no\nbotão e se estiverem na formatação correta (A data,cpf e email possuem verificação caso\nseja preechido de forma errada) os dados serão salvos e o usuario será direcionado para\na tela inicial e com os dados cadastrados já será possivel fazer a entradas com os dados\ncadastrados'

        txt_subtitle_box_regs = Label(regs,text=txt_subtitle_regs,justify='left',bg=color_box,font=text_fontB).grid(row=0,column=0,pady=(5,0),sticky='w')
        txt1_box_regs = Label(regs,text=txt1_regs,justify='left',bg=color_box,font=text_fontN).grid(row=1,column=0,pady=(5,0),sticky='w')
        txt2_box_regs = Label(regs,text=txt2_regs,justify='left',bg=color_box,font=text_fontN).grid(row=2,column=0,pady=(5,0),sticky='w')
        txt3_box_regs = Label(regs,text=txt3_regs,justify='left',bg=color_box,font=text_fontN).grid(row=3,column=0,pady=(5,0),sticky='w')
        ####################################################################################################################################
        #Enter
        ####################################################################################################################################
        txt_subtitle_enter = 'Entrada'
        txt1_enter = 'A tela de entrada é a principal responsável por ser como o próprio nome já diz a entrada da\nverdadeira experiência da aplicação'
        txt2_enter = 'Diferente da tela de cadastro, essa tela possui poucos campos de digitação, são elas\no email,senha(da mesma forma que a tela de cadastro também possui a função de ver e\nnão ver a senha) e o cpf, com os dados fornecidos será feita uma busca com esses dados\ne caso ocorra corretamente será pego todos os dados do usuario e que será usado mais\npara frente na aplicação'
        txt3_enter = 'Nessa tela admito que foi a que menos tive criatividade já que não teve algo muito inovador\nou algo que acho bonito, mas para mim que estive programando todas as telas, essa tela\nfoi a que mais vi e por mim estou enjoado dela e principalmente do tom simplicista que ela\ntransmite, mas essa é a minha opinião que por causa de tanta dor de cabeça comecei\na não gostar dela, mas não sou contra qualquer outra opinião já que é só uma brincadeira,\nmas não significa que eu a goste ^_^'

        txt_subtitle_box_enter = Label(enter,text=txt_subtitle_enter,justify='left',bg=color_box,font=text_fontB).grid(row=0,column=0,pady=(5,0),sticky='w')
        txt1_box_enter = Label(enter,text=txt1_enter,justify='left',bg=color_box,font=text_fontN).grid(row=1,column=0,pady=(5,0),sticky='w')
        txt2_box_enter = Label(enter,text=txt2_enter,justify='left',bg=color_box,font=text_fontN).grid(row=2,column=0,pady=(5,0),sticky='w')
        txt3_box_enter = Label(enter,text=txt3_enter,justify='left',bg=color_box,font=text_fontN).grid(row=3,column=0,pady=(5,0),sticky='w')
        ####################################################################################################################################
        #Home
        ####################################################################################################################################
        txt_subtitle_home = 'Página de entrada'
        txt1_home = 'Tela mais importante da aplicação já que é a responsável por ligar os outros componentes\ne umas das mais que possui mecânica, uma de suas mecânicas é a foto do usuario que\nserá de acordo com a  terminação do CPF'
        txt2_home = 'A mesma possui várias funções e importância para a aplicação, já que é a responsável\npela ligação com as demais e a responsável pela atualização dos dados do usuario e\nressaltando que é a tela que o usuario verá após a entrada.'
        txt3_home = 'Posteriomente na aplicação terá a tela de fatura que é a responsável por pagar o valor da\nfatura e a mesma possui juros mensais de 5% e que todo mês será atualizado e é por\nmeio da tela de entrada que a atualização é feita'
        txt4_home = 'Essa tela possui algumas informações do usuario e uma grande quantidade de botões,\nalgo que pode passar despercebido é um "botão" escondido na tela e que não é um botão\ne sim um evento que é a do PERFIL que mostrará todas as informações do usuario, para\nacessa-lo basta clicar nas suas informações ou só no cartão de crédito será direcionado\ndiretamente para essa página de perfil'

        txt_subtitle_box_home = Label(home,text=txt_subtitle_home,justify='left',bg=color_box,font=text_fontB).grid(row=0,column=0,pady=(5,0),sticky='w')
        txt1_home_box_home = Label(home,text=txt1_home,justify='left',bg=color_box,font=text_fontN).grid(row=1,column=0,pady=(5,0),sticky='w')
        txt2_home_box_home = Label(home,text=txt2_home,justify='left',bg=color_box,font=text_fontN).grid(row=2,column=0,pady=(5,0),sticky='w')
        txt3_home_box_home = Label(home,text=txt3_home,justify='left',bg=color_box,font=text_fontN).grid(row=3,column=0,pady=(5,0),sticky='w')
        txt4_home_box_home = Label(home,text=txt4_home,justify='left',bg=color_box,font=text_fontN).grid(row=4,column=0,pady=(5,0),sticky='w')
        ####################################################################################################################################
        #Perfil | Fatura
        ####################################################################################################################################
        txt_subtitle1_pb = 'Perfil'
        txt1_pb = 'Tela visualmente simples que apresenta apenas as informações do usuario e dois botões'
        txt2_pb = 'Essa mesma tela possui variações que dependendo de quem está acesssando mudará,\nse o usuario que está acessando for o que estiver entrado mostrará todas as informações\ne caso contrário terá restrições no caso do cpf,email e senha que não será mostrado'
        txt3_pb = 'A tela possui dois botões que um deles é o de voltar e ver pessoas que possuem\nrespectivamente função de voltar a tela anterior e ver todas as pessoas cadastradas'
        txt4_pb = 'Da mesma forma que a tela de entrada, a tela de perfil possui também a função de mostrar\na imagem do personagem'
        txt_subtitle2_pb = 'Fatura'
        txt5_pb = 'A tela de FATURA possui o próposito de pagar os valores transferido com crédito e podendo\nser escolhido a fatura que quer pagar. As informações mostradas na tela de FATURA são\nsimples. Caso a fatura seja paga já será descontado do saldo e é claro o valor do montante\nserá diminuido e como toda ação essa também será salva no histórico'
        txt6_pb = 'Caso todas as faturas sejam pagas o crédito voltará a ser o limite'


        txt_subtitle1_box_pb = Label(prf_bill,text=txt_subtitle1_pb,justify='left',bg=color_box,font=text_fontB).grid(row=0,column=0,pady=(5,0),sticky='w')
        txt1_box_pb = Label(prf_bill,text=txt1_pb,justify='left',bg=color_box,font=text_fontN).grid(row=1,column=0,pady=(5,0),sticky='w')
        txt2_box_pb = Label(prf_bill,text=txt2_pb,justify='left',bg=color_box,font=text_fontN).grid(row=2,column=0,pady=(5,0),sticky='w')
        txt3_box_pb = Label(prf_bill,text=txt3_pb,justify='left',bg=color_box,font=text_fontN).grid(row=3,column=0,pady=(5,0),sticky='w')
        txt4_box_pb = Label(prf_bill,text=txt4_pb,justify='left',bg=color_box,font=text_fontN).grid(row=4,column=0,pady=(5,0),sticky='w')
        txt_subtitle2_box_pb = Label(prf_bill,text=txt_subtitle2_pb,justify='left',bg=color_box,font=text_fontB).grid(row=5,column=0,pady=(5,0),sticky='w')
        txt5_box_pb = Label(prf_bill,text=txt5_pb,justify='left',bg=color_box,font=text_fontN).grid(row=6,column=0,pady=(5,0),sticky='w')
        txt6_box_pb = Label(prf_bill,text=txt6_pb,justify='left',bg=color_box,font=text_fontN).grid(row=7,column=0,pady=(5,0),sticky='w')

        ####################################################################################################################################
        #Saque | Deposito
        ####################################################################################################################################
        txt_subtitle1_wd = 'Deposito'
        txt1_wd = 'A tela de DEPOSITO como o próprio nome já diz faz o deposito de um certo valor para que\nseja somado com o valor atual da conta, além de ter apenas esse próposito também é\npossivel ver o deposito sendo acrescentado na conta em tempo real, já que na parte\nsuperior possui caixas que mostra o saldo e crédito e é atualizado em tempo real'
        txt2_wd = 'O deposito não possui limite e quando o deposito é executado com sucesso o valor já\né acrescido no saldo e alguns dados são salvos no historico'
        txt_subtitle2_wd = 'Saque'
        txt3_wd = 'A tela de SAQUE não é muito diferente da tela de deposito já que é a mesma, mudando\napenas o nome e função. Sendo o contrárior da tela de deposito, a tela de saque retira um\ncerto valor do saldo, é claro que não excedido do saldo senão não sera feito a ação, além\ndisso da mesma forma que o deposito o saldo é atualizado em tempo real também'
        txt4_wd = 'Após o saque for sucedido, as atualizaçoes já serão feitas e mostradas em tempo real e é\nclaro todas as informações serão salvas no historico'

        txt_subtitle1_box_wd = Label(with_depo,text=txt_subtitle1_wd,justify='left',bg=color_box,font=text_fontB).grid(row=0,column=0,pady=(5,0),sticky='w')
        txt1_box_wd = Label(with_depo,text=txt1_wd,justify='left',bg=color_box,font=text_fontN).grid(row=1,column=0,pady=(5,0),sticky='w')
        txt2_box_wd = Label(with_depo,text=txt2_wd,justify='left',bg=color_box,font=text_fontN).grid(row=2,column=0,pady=(5,0),sticky='w')
        txt_subtitle2_box_wd = Label(with_depo,text=txt_subtitle2_wd,justify='left',bg=color_box,font=text_fontB).grid(row=3,column=0,pady=(5,0),sticky='w')
        txt3_box_wd = Label(with_depo,text=txt3_wd,justify='left',bg=color_box,font=text_fontN).grid(row=4,column=0,pady=(5,0),sticky='w')
        txt4_box_wd = Label(with_depo,text=txt4_wd,justify='left',bg=color_box,font=text_fontN).grid(row=5,column=0,pady=(5,0),sticky='w')
        ####################################################################################################################################
        #Transferência | Fatura
        ####################################################################################################################################
        txt_subtitle1_tf = 'Transferência'
        txt1_tf = 'A tela de tranferência possui funçâo de transferir algum valor para algum outro usuario pelo\nnúmero de cartão de crédito, esse valor pode ser débito e até crédito'
        txt2_tf = 'Caso o valor seja débito o valor será transferido de forma direta e o valor enviado já será\ndecontado no saldo do remetente quanto do destinatário,porém caso contrário e seja\ncrédito terá algo a mais, o valor do destinatário já será enviando e enquanto do remetente,\no valor do crédito será descontato e com 5% de juros,é importante ressaltar que caso não\ntenha o valor especificado do crédito ou saldo a transferência não será concluida'
        txt3_tf = 'Caso a forma de transferência seja crédito, o valor valor transferido terá que ser pago na\ntela FATURA e de forma parcelada, de acordo com a quantidade de parcelas especificadas\ne a cada mês será preciso pagar o certo valor e caso contrário será acrescido 5% de juros\nao montante, além também, se a transferência for por crédito o limite do cartão será\naumentado 5% em relação ao valor transferido'
        txt4_tf = 'Todos os dados serão salvos no histórico. Algo diferencial dessa tela é a procura, que\npossui função de procurar o usuario com o número de cartão sugerido e caso seja\nencontrado será mostrado o nome do usuario e a foto do usuario, claro que não é\nobrigatório mas é um diferencial para que não seja transferido errado'
        
        txt_subtitle1_box_tf = Label(transfer,text=txt_subtitle1_tf,justify='left',bg=color_box,font=text_fontB).grid(row=0,column=0,pady=(5,0),sticky='w')
        txt1_box_tf = Label(transfer,text=txt1_tf,justify='left',bg=color_box,font=text_fontN).grid(row=1,column=0,pady=(5,0),sticky='w')
        txt2_box_tf = Label(transfer,text=txt2_tf,justify='left',bg=color_box,font=text_fontN).grid(row=2,column=0,pady=(5,0),sticky='w')
        txt3_box_tf = Label(transfer,text=txt3_tf,justify='left',bg=color_box,font=text_fontN).grid(row=3,column=0,pady=(5,0),sticky='w')
        txt3_box_tf = Label(transfer,text=txt4_tf,justify='left',bg=color_box,font=text_fontN).grid(row=4,column=0,pady=(5,0),sticky='w')
        ####################################################################################################################################
        #Historico | Lista de usuario
        ####################################################################################################################################
        txt_subtitle1_hl = 'Histórico'
        txt1_hl = 'A tela de histórico armazenará todas as informações das açoes feitas, são elas DEPOSITO,\nSAQUE,FATURA e TRANSFERÊNCIA, armazenando o usuario,valor e data e no caso da\ntransferência o remetente e tipo de transferência'
        txt2_hl = 'Para facilitar a busca é possivel buscar por DIA,MÊS e ANO, sendo não obrigatório preecher\ntodos, apenas o necessário. Os dados estão em ordem decrescente por data, sendo do\nmais atual para o mais antigo'
        txt_subtitle2_hl = 'Lista de Usuarios'
        txt3_hl = 'A LISTA DE USUARIOS é uma tabela com todos os registros cadatrados, é claro que\nsem contar com o usuario atual, sua principal função é conhecer os outros usuarios e\nolhar o perfil deles'
        txt4_hl = 'Os perfils do registros por meio da LISTA DE USUARIO é um puco diferente do usuario\natual, já que é limitado em informações, é claro para que não mostre informações pessoais'
        txt5_hl = 'Como pode ter muitos usuarios, é possivel pesquisar por nome, pode não ser o nome por\ncompleto mas alguma parte'


        txt_subtitl1_box_hl = Label(hist_list,text=txt_subtitle1_hl,justify='left',bg=color_box,font=text_fontB).grid(row=0,column=0,pady=(5,0),sticky='w')
        txt1_box_hl = Label(hist_list,text=txt1_hl,justify='left',bg=color_box,font=text_fontN).grid(row=1,column=0,pady=(5,0),sticky='w')
        txt2_box_hl = Label(hist_list,text=txt2_hl,justify='left',bg=color_box,font=text_fontN).grid(row=2,column=0,pady=(5,0),sticky='w')
        txt_subtitl2_box_hl = Label(hist_list,text=txt_subtitle2_hl,justify='left',bg=color_box,font=text_fontB).grid(row=3,column=0,pady=(5,0),sticky='w')
        txt3_box_hl = Label(hist_list,text=txt3_hl,justify='left',bg=color_box,font=text_fontN).grid(row=4,column=0,pady=(5,0),sticky='w')
        txt4_box_hl = Label(hist_list,text=txt4_hl,justify='left',bg=color_box,font=text_fontN).grid(row=5,column=0,pady=(5,0),sticky='w')
        txt5_box_hl = Label(hist_list,text=txt5_hl,justify='left',bg=color_box,font=text_fontN).grid(row=6,column=0,pady=(5,0),sticky='w')

        back_btn = Button(self.infor,image=back_btn_image,bg='#6BA5F2',activebackground='#6BA5F2',bd=0,command=self.go_home).place(x=87,y=449)

        self.infor.mainloop()


    def go_home(self):
            from home import home
            self.infor.destroy()
            home().home()