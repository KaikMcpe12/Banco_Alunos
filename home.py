from function import *

class home(student_bench):
    def home(self):

        bg_image = PhotoImage(master=self.app,file=self.folderAssets+'\\home\\background.png')
        title_image = PhotoImage(master=self.app,file=self.folderAssets+'\\home\\title.png')
        enter_btn_image = PhotoImage(master=self.app,file=self.folderAssets+'\\home\\enter_btn.png')
        register_btn_image = PhotoImage(master=self.app,file=self.folderAssets+'\\home\\register_btn.png')
        infor_btn_image = PhotoImage(master=self.app,file=self.folderAssets+'\\home\\infor_btn.png')


        self.home = Frame(self.app,width=700,height=500)
        self.home.pack()


        self.backg = Canvas(self.home, width = 700,height = 500)
        self.backg.pack(fill = "both", expand = True) 

        self.backg.create_image(0,0,image = bg_image,anchor = "nw")
        self.title = self.backg.create_image(87,40, image=title_image, anchor='nw')


        self.enter_btn = Button(self.home,image=enter_btn_image,bg='#6BA5F2',activebackground='#6BA5F2',bd=0,command=self.go_enter).place(x=269,y=228)

        self.register_btn = Button(self.home,image=register_btn_image,bg='#6BA5F2',activebackground='#6BA5F2',bd=0,command=self.go_register).place(x=269,y=288)

        self.infor_btn = Button(self.home,image=infor_btn_image,bg='#6BA5F2',activebackground='#6BA5F2',bd=0,command=self.go_infor).place(x=269,y=348)

        self.home.mainloop()


    def go_enter(self):
        from enter import enter
        self.home.destroy()
        enter().enter()



    def go_register(self):
        from register import register
        self.home.destroy()
        register().register()


    def go_infor(self):
        from information import information
        self.home.destroy()
        information().information()