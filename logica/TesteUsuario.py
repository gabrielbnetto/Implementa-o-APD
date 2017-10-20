import unittest
import usuario

class TesteUsuario(unittest.TestCase):

    def setUp(self):
        usuario.remover_todos_usuarios()

    def test_sem_usuario(self):
        usuarios = usuario.listar_usuarios()
        self.assertEqual(0, len(usuarios))

    def test_adicionar_um_usuario(self):
        usuario.adicionar_usuario(555555,"Joao","joao@hotmail.com","123456")
        usuarios = usuario.listar_usuarios()
        self.assertEqual(1, len(usuarios))

        u = usuarios[0]
        self.assertEqual(555555, u[0])
        self.assertEqual("Joao", u[1])
        self.assertEqual("joao@hotmail.com", u[2])
        self.assertEqual("123456", u[3])

    def test_adicionar_dois_usuarios(self):
        usuario.adicionar_usuario(555555,"Joao","joao@hotmail.com","123456")
        usuario.adicionar_usuario(444444,"Lucas","lucas@hotmail.com","RNIEHO")
        usuarios = usuario.listar_usuarios()
        self.assertEqual(2, len(usuarios))


    def test_remover_usuario(self):
        usuario.adicionar_usuario(555555,"Joao","joao@hotmail.com","123456")
        usuario.remover_usuario(555555)
        usuarios = usuario.listar_usuarios()
        self.assertEqual(0, len(usuarios))

        
    def test_buscar_usuario(self):
        usuario.adicionar_usuario(555555,"Joao","joao@hotmail.com","123456")
        usuario.adicionar_usuario(444444,"Lucas","lucas@hotmail.com","RNIEHO")
        u = usuario.buscar_usuario(444444)
        self.assertEqual("Lucas", u[1])
        self.assertEqual("lucas@hotmail.com", u[2])
        self.assertEqual("RNIEHO", u[3])


if __name__ == '__main__':
    unittest.main(exit=False)
