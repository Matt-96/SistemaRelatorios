
from PIL import Image

import customtkinter as ctk
from componentes.botoes import criar_btnPersonalizado
from componentes.conteinersTelaLogin import criar_quadroLogin, criar_labelLogin, criar_campoUsuario, criar_campoSenha, \
    mostrarLogin, criar_labelLoginTitulo, criar_frameUsuario, criar_labelIconeUsuario, \
    criar_frameSenha, criar_labelIconeSenha, criar_btnVisibilidadeSenha, criar_linhaCentral, criar_txtCentral, \
    criar_TituloUsuario, criar_TituloSenha
from database import verificar_login
from menuPrincipal import menu_principal



def login(janela):


    #função de autenticação
    def autenticar():
        usuario = campo_usuario.get()
        senha = campo_senha.get()

        acesso = verificar_login(usuario, senha)

        if acesso:
            resultado_login.configure(text="Login feito com sucesso",text_color="green", font=("Roboto", 20))
            quadroLogin.destroy()
            resultado_login.destroy()
            menu_principal(janela,usuario, login)
        else:
            resultado_login.configure(text="Credenciais inválidas.", text_color="red", font=("Roboto",20))

    #QUADRO LOGIN
    quadroLogin = criar_quadroLogin(janela) # QUADRO DO LOGIN
    label_login = criar_labelLogin(quadroLogin) # TITULO LOGIN
    labelTitulo = criar_labelLoginTitulo(quadroLogin)
    criar_linhaCentral(quadroLogin)
    criar_txtCentral((quadroLogin))

    #CAMPO DE INPUT DO USUARIO
    frameUsuario = criar_frameUsuario(quadroLogin)


    criar_labelIconeUsuario(frameUsuario)

    campo_usuario = criar_campoUsuario(frameUsuario) #ENTRY DO USUARIO
    criar_TituloUsuario(quadroLogin)

    frameSenha = criar_frameSenha(quadroLogin)

    criar_labelIconeSenha(frameSenha)



    campo_senha = criar_campoSenha(frameSenha) # ENTRY DE SENHA)
    criar_btnVisibilidadeSenha(frameSenha,campo_senha)
    criar_TituloSenha(quadroLogin)


    criar_btnPersonalizado(quadroLogin,text="Entrar",width=350, height=50, command=autenticar, fg_color="#087CFF",
                           font=("Roboto",25),border_color="#A78BFA", border_width=2,hover="False") #BOTAO ENTRAR

    #CAMPO FEEDBACK
    resultado_login = mostrarLogin(janela)

    janela.mainloop()#Abre a janela

