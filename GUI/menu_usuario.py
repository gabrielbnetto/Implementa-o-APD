from logica import usuario
from logica import historico
from logica import filme

def imprimir_usuario(usuario):
    print("CPF: ",  usuario[0])
    print ("Nome: ", usuario[1])
    print ("Email: ", usuario[2])
    print ("Senha: ", usuario[3])
    print()

def menu_adicionar():
    print ("\nAdicionar Usuario \n")
    cpf = int(input("CPF: "))
    nome = input("Nome: ")
    email = input("Email: ")
    senha = input("Senha: ")
    usuario.adicionar_usuario(cpf,nome,email,senha)

def menu_registrar_filme_historico():
    print("\nAdicionar Filme Assistido \n")
    cpf = int(input("CPF: "))
    cod_filme = int(input("Codigo do Filme: "))
    filmes = filme.listar_filmes()
    for Filme in filmes:
        if cod_filme == Filme[0]:
            historico.registrar_filme_assistido(cpf, cod_filme)
            print("Filme Registrado")
            return
        else:
            h = False
    if h == False:
        print("\nFilme não encontrado\n")

def menu_listar_filmes_historico():
    print("\nListar Historico de filmes \n")
    cpf = int(input("CPF: "))
    historicos = historico.listar_filmes_assistidos(cpf)
    if historicos == []:
        print("Não há filmes assistidos")
    else:
        for h in historicos:
            print("Filme:",h)


def menu_listar():
    print ("\nListar Usuarios \n")
    usuarios = usuario.listar_usuarios()
    for u in usuarios:
        imprimir_usuario(u)

def menu_buscar():
    print ("\nBuscar Usuario por CPF \n")
    cpf = int(input("CPF: "))
    u = usuario.buscar_usuario(cpf)
    if (u == None):
        print ("Usuario não encontrado")
    else:
        imprimir_usuario(u)

def menu_remover():
    print ("\nRemover Usuario \n")
    cpf = int(input("CPF: "))
    u = usuario.remover_usuario(cpf)
    if (u == False):
        print ("Usuario não encontrado")
    else:
        print ("Usuario removido")

def mostrar_menu():
    rodar_usuario = True
    menu = ("\n.-----------Menu Usuario---------.\n"+
            "|   (1) Adicionar novo Usuario   |\n"+
            "|   (2) Listar Usuario           |\n"+
            "|   (3) Registrar Filme Historico|\n"+
            "|   (4) Listar Filmes Historico  |\n"+
            "|   (5) Buscar Usuario por CPF   |\n"+
            "|   (6) Remover Usuario          |\n"+
            "|   (0) Voltar                   |\n"+
            ".--------------------------------.")

    while(rodar_usuario):
        print (menu)
        op = int(input("Digite sua escolha: "))

        if (op == 1):
            menu_adicionar()
        elif(op == 2):
            menu_listar()
        elif(op == 3):
            menu_registrar_filme_historico()
        elif (op == 4):
            menu_listar_filmes_historico()
        elif (op == 5):
            menu_buscar()
        elif(op == 6):
            menu_remover()
        elif (op == 0):
            rodar_usuario = False
