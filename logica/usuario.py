usuarios=[]

def adicionar_usuario(cpf,nome,email,senha):
    usuario = [cpf,nome,email,senha]
    usuarios.append(usuario)

def listar_usuarios():
    return usuarios

def buscar_usuario(cpf):
    for u in usuarios:
        if (u[0] == cpf):
            return u
    return None

def remover_usuario(cpf):
    for u in usuarios:
        if (u[0] == cpf):
            usuarios.remove(u)
            return True
    return False

def iniciar_usuarios():
    adicionar_usuario(555555,"Joao","joao@hotmail.com","123456")
    adicionar_usuario(444444,"Lucas","lucas@hotmail.com","RNIEHO")
