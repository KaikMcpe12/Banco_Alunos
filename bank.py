import sqlite3
from sqlite3 import Error
import os

pastaAPP = os.path.dirname(__file__)
nomeBanco = pastaAPP+'\\banco_alunos.db'

def Conexao_Banco():
    con = None
    try:
        con = sqlite3.connect(nomeBanco)
    except Error as ex:
        print(ex)
    return con

def dql(query): #select
    vcon = Conexao_Banco()
    c = vcon.cursor()
    c.execute(query)
    res = c.fetchall()
    vcon.close()
    return res

def dml(query): #insert,update,delete
    try:
        vcon = Conexao_Banco()
        c = vcon.cursor()
        c.execute(query)
        vcon.commit()
        vcon.close()
    except Error as ex:
        print(ex)