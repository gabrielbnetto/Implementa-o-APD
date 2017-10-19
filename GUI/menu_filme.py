from logica import filme

def imprimir_filme(filme):
    print("Codigo do Filme: ",  filme[0])
    print ("Título: ", filme[1])
    print ("Gênero: ", filme[2])
    print ("Ano: ", filme[3])
    print()

def menu_adicionar():
    print ("\nAdicionar Filme \n")
    cod_filme = int(input("Codigo do Filme: "))
    titulo = input("Título: ")
    genero = input("Gênero: ")
    ano = int(input("Ano: "))
    filme.adicionar_filme(cod_filme,titulo,genero,ano)

def menu_listar():
    print ("\nListar Filmes \n")
    filmes = filme.listar_filmes()
    for f in filmes:
        imprimir_filme(f)

def menu_buscar():
    print ("\nBuscar Filme por Codigo \n")
    cod_filme = int(input("Codigo do Filme: "))
    f = filme.buscar_filme(cod_filme)
    if (f == None):
        print ("Filme não encontrado")
    else:
        imprimir_filme(f)

def menu_buscar_por_genero():
    print ("\nBuscar Filme por Gênero \n")
    genero = input("Gênero: ")
    f = filme.buscar_filme_por_genero(genero)
    if (f == None):
        print ("Filme não encontrado")
    else:
        imprimir_filme(f)

def menu_remover():
    print ("\nRemover Filme \n")
    cod_filme = int(input("Codigo do Filme: "))
    f = filme.remover_filme(cod_filme)
    if (f == False):
        print ("Filme não encontrado")
    else:
        print ("Filme removido")

def mostrar_menu():
    rodar_filme = True
    menu = ("\n.---------Menu Filme-----------.\n"+
            "|(1) Adicionar novo Filme      |\n"+
            "|(2) Listar Filmes             |\n"+
            "|(3) Buscar Filme por Codigo   |\n"+
            "|(4) Buscar Filme por Genero   |\n"+
            "|(5) Remover Filme             |\n"+
            "|(0) Voltar                    |\n"+
            ".------------------------------.")

    while(rodar_filme):
        print (menu)
        op = int(input("Digite sua escolha: "))

        if (op == 1):
            menu_adicionar()
        elif(op == 2):
            menu_listar()
        elif(op == 3):       
            menu_buscar()
        elif (op == 4):
            menu_buscar_por_genero()
        elif (op == 5):
            menu_remover()
        elif (op == 0):
            rodar_filme = False
