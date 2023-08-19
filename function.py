from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime,date
import os
from bank import *

class student_bench:        
    folderAssets = os.path.dirname(__file__)+'\\assets'

    app = Tk()
    app.title('Banco Alunos')
    app.geometry('700x500')
    app.resizable(width=False,height=False)


    user_infor = None
    color_user = None
    user_cpf = None


    # def go_withdraw(self,frame):
    #     from withdraw import withdraw
    #     frame.destroy()
    #     withdraw()
