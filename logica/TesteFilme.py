import unittest
import filme

class TesteFilme(unittest.TestCase):

    def setUp(self):
        filme.remover_todos_filmes()

    def test_sem_filmes(self):
        filmes = filme.listar_filmes()
        self.assertEqual(0, len(filmes))

    def test_adicionar_um_filme(self):
        filme.adicionar_filme(555555, "It", "terror", 2017, "filmes/It.mp4")
        filmes = filme.listar_filmes()
        self.assertEqual(1, len(filmes))

        f = filmes[0]
        self.assertEqual(555555, f[0])
        self.assertEqual("It", f[1])
        self.assertEqual("terror", f[2])
        self.assertEqual(2017, f[3])
        self.assertEqual("filmes/It.mp4", f[4])

    def test_adicionar_dois_filmes(self):
        filme.adicionar_filme(555555, "It", "terror", 2017, "filmes/It.mp4")
        filme.adicionar_filme(333333, "Thor Ragnarok", "acao", 2017, "filmes/Thor Ragnarok.mp4")
        filmes = filme.listar_filmes()
        self.assertEqual(2, len(filmes))

    def test_remover_filme(self):
        filme.adicionar_filme(333333, "Thor Ragnarok", "acao", 2017, "filmes/Thor Ragnarok.mp4")
        filme.remover_filme(333333)
        filmes = filme.listar_filmes()
        self.assertEqual(0, len(filmes))

    def test_buscar_filme(self):
        filme.adicionar_filme(333333, "Thor Ragnarok", "acao", 2017, "filmes/Thor Ragnarok.mp4")
        filme.adicionar_filme(555555, "It", "terror", 2017, "filmes/It.mp4")
        f = filme.buscar_filme(333333)
        self.assertEqual("Thor Ragnarok", f[1])
        self.assertEqual("acao", f[2])
        self.assertEqual(2017, f[3])
        self.assertEqual("filmes/Thor Ragnarok.mp4", f[4])

    def test_buscar_filme_por_genero(self):
        filme.adicionar_filme(333333, "Thor Ragnarok", "acao", 2017, "filmes/Thor Ragnarok.mp4")
        filme.adicionar_filme(555555, "It", "terror", 2017, "filmes/It.mp4")
        f = filme.buscar_filme_por_genero("acao")
        self.assertEqual(333333, f[0])
        self.assertEqual("Thor Ragnarok", f[1])
        self.assertEqual(2017, f[3])
        self.assertEqual("filmes/Thor Ragnarok.mp4", f[4])

if __name__ == '__main__':
    unittest.main(exit=False)
