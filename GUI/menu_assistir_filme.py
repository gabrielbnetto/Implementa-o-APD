from logica import usuario
from logica import filme
from logica import video_stream
from logica import historico

def assistir_filme():
    cpf = int(input("\nCPF do usuário: "))
    user = usuario.buscar_usuario(cpf)
    
    while user is None:
        print("CPF inválido")
        cpf = int(input("Entre com o CPF do usuario que vai assistir o filme: "))
        user = usuario.buscar_usuario(cpf)
        
    print("\nFilmes disponíveis para assistir: ")
    filmes = filme.listar_filmes()
    for f in filmes:
        print("Código: " + str(f[0]) + " - " + f[1] + " - " + f[2])
    
    cod_filme = int(input("\nDigite o código do filme que deseja assistir: "))
    chosen = filme.buscar_filme(cod_filme)
    while chosen == None:
        print("Código inválido")
        cod_filme = int(input("Digite o código do filme que deseja assistir: "))
        chosen = filme.buscar_filme(cod_filme)
        
    print("Carregando o filme " + chosen[1])
    start =  input("Deseja começar o filme? (S/N): ")
    if start == "S" or start == "s":
        cod_filme = chosen[0]
        nome = chosen[1]
        url = chosen[4]
        video_stream.play_video(nome, url)
        historico.registrar_filme_assistido(cpf, cod_filme)
    else:
        return

def mostrar_menu():
    rodar_mostrar_filmes = True
    menu = ("\n.-------Menu Assistir Filme------.\n"+
           "|  (1) Assistir à um filme       |\n"+
           "|  (0) Voltar                    |\n"+
           ".--------------------------------.")

    while(rodar_mostrar_filmes):
        print(menu)
        op = int(input("Digite sua escolha: "))

        if(op == 1):
            assistir_filme()
        elif(op == 0):
            rodar_mostrar_filmes = False
