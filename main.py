#ESSE ARQUIVO SERVE SÓ PRA INICIALIZAR A APLICAÇÃO

import customtkinter as ctk

from database import inicializar_banco
from telaLogin import login
#Configura a janela
janela = ctk.CTk(fg_color="#081024")
janela.title("Tela de Login")
janela.geometry("850x1000")

inicializar_banco()

login(janela)

janela.mainloop()#Abre a janela 
