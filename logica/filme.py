filmes=[]

def adicionar_filme(cod_filme,titulo,genero,ano):
    filme = [cod_filme,titulo,genero,ano]
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

def iniciar_filmes():
    adicionar_filme(555555,"Amadeus","terror",1999)
    adicionar_filme(444444,"Homem Aranha","acao",1999)
