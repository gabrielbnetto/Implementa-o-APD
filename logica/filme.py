filmes = []

def adicionar_filme(cod_filme, titulo, genero, ano, url):
    filme = [cod_filme, titulo, genero, ano, url]
    filmes.append(filme)

def listar_filmes():
    return filmes

def buscar_filme(cod_filme):
    for f in filmes:
        if (f[0] == cod_filme):
            return f
    return None

def buscar_filme_por_genero(genero):
    for f in filmes:
        if (f[2] == genero):
            return f
    return None

def remover_filme(cod_filme):
    for f in filmes:
        if (f[0] == cod_filme):
            filmes.remove(f)
            return True
    return False

def remover_todos_filmes():
    global filmes
    filmes = []

def iniciar_filmes():
    adicionar_filme(555555, "It", "terror", 2017, "filmes/It.mp4")
    adicionar_filme(444444, "Star Wars: The Last Jedi", "acao", 2017, "filmes/Star Wars The Last Jedi.mp4")
    adicionar_filme(333333, "Thor Ragnarok", "acao", 2017, "filmes/Thor Ragnarok.mp4")
