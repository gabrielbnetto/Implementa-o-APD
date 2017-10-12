from GUI import menu_filme
from GUI import menu_usuario
from logica import historico

def menu_geral():
    run_menu = True
    print(".--------------------------------------.\n"+
          "|   Escolha uma das seguintes opcoes:  |\n"+
          "|   (1)Ver Menu de Filmes              |\n"+
          "|   (2)Ver Menu de Usuario             |\n"+
          "|   (3)Ver Historico de Filmes         |\n"+
          "|   (0)Sair                            |\n"+
          ".--------------------------------------.\n")

    escolha = int(input())
    while run_menu:
        if escolha == 1:
            menu_filme.mostrar_menu()

        elif escolha == 2:
            menu_usuario.mostrar_menu()

        elif escolha == 0:
            run_menu = False
            menu_geral()

menu_geral()

