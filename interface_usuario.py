from GUI import menu_filme
from GUI import menu_usuario
import time

run_menu = True

def mostrar_menu_principal():
    print(".--------------------------------------.\n"+
          "|   Escolha uma das seguintes opcoes:  |\n"+
          "|   (1)Ver Menu de Filmes              |\n"+
          "|   (2)Ver Menu de Usuario             |\n"+
          "|   (0)Sair                            |\n"+
          ".--------------------------------------.\n")
    return int(input())


while run_menu:
    escolha = mostrar_menu_principal()
    if escolha == 1:
        menu_filme.mostrar_menu()

    elif escolha == 2:
        menu_usuario.mostrar_menu()

    elif escolha == 0:
        print("--------------Saindo--------------------")
        run_menu = False


