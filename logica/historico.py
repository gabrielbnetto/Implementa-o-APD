from logica import filme
from logica import usuario

filmes_vistos_usuarios = []

def registrar_filme_assistido(cpf, cod_filme):
    for i in range(len(filmes_vistos_usuarios)):
        if filmes_vistos_usuarios[i][0] == cpf:
            filmes_vistos_usuarios[i].append(cod_filme)
            return
    filmes_vistos_usuarios.append([cpf, cod_filme])


def listar_filmes_assistidos(cpf):
    codigos_filmes = []
    for i in range(len(filmes_vistos_usuarios)):
        if filmes_vistos_usuarios[i][0] == cpf:
            codigos_filmes = filmes_vistos_usuarios[i][1:]
            break
    filmes = []
    for codigo in codigos_filmes:
        f = filme.buscar_filme(codigo)
        filmes.append(f[1])
    return filmes
            
##registrar_filme_assistido(1234567, 555555)
##registrar_filme_assistido(1234567, 444444)
##
##registrar_filme_assistido(1473343, 444444)
##
##registrar_filme_assistido(9743458, 444444)
##
##print(listar_filmes_assistidos(1234567))
##print(listar_filmes_assistidos(1473343))
##print(listar_filmes_assistidos(9743458))
