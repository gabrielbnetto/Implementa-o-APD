from logica import usuario

def imprimir_usuario(usuario):
    print("CPF: ",  usuario[0])
    print ("Nome: ", usuario[1])
    print ("Email: ", usuario[2])
    print ("Senha: ", usuario[3])

def menu_adicionar():
    print ("Adicionar Usuario \n")
    cpf = int(input("CPF: "))
    nome = (input("Nome: ")
    email = input("Email: ")
    senha = int(input("Senha: "))
    usuario.adicionar_usuario(cpf,nome,email,senha)

def menu_listar():
    print ("Listar Usuarios \n")
    usuarios = usuario.listar_usuarios()
    for u in usuarios:
        imprimir_usuario(u)

def menu_buscar():
    print ("Buscar Usuario por CPF \n")
    cpf = int(input("CPF: "))
    u = usuario.buscar_usuario(cpf)
    if (u == None):
        print ("Usuario não encontrado")
    else:
        imprimir_usuario(u)

def menu_remover():
    print ("Remover Usuario \n")
    cpf = int(input("CPF: "))
    u = usuario.remover_usuario(cpf)
    if (u == False):
        print ("Usuario não encontrado")
    else:
        print ("Usuario removido")

def mostrar_menu():
    rodar_usuario = True
    menu = ("Menu Usuario\n"+
             "(1) Adicionar novo Usuario \n" +
             "(2) Listar Usuario \n" +
             "(3) Buscar Usuario por CPF \n" +
             "(4) Remover Usuario \n" +
             "(0) Voltar\n"+
            "----------------")

    while(rodar_usuario):
        print (menu)
        op = int(input("Digite sua escolha: "))

        if (op == 1):
            menu_adicionar()
        elif(op == 2):
            menu_listar()
        elif(op == 3):       
            menu_buscar()
        elif (op == 4):
            menu_remover()
        elif (op == 0):
            rodar_usuario = False
