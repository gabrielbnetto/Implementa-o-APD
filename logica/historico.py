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

def limpar_historico():
    global filmes_vistos_usuarios
    filmes_vistos_usuarios = []

