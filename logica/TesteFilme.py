import unittest
import filme

class TesteFilme(unittest.TestCase):

    def setUp(self):
        filme.remover_todos_filmes()

    def test_sem_filmes(self):
        filmes = filme.listar_filmes()
        self.assertEqual(0, len(filmes))

    def test_adicionar_um_filme(self):
        filme.adicionar_filme(555555, "Amadeus", "terror", 1999)
        filmes = filme.listar_filmes()
        self.assertEqual(1, len(filmes))

        f = filmes[0]
        self.assertEqual(555555, f[0])
        self.assertEqual("Amadeus", f[1])
        self.assertEqual("terror", f[2])
        self.assertEqual(1999, f[3])

    def test_adicionar_dois_filmes(self):
        filme.adicionar_filme(555555,"Amadeus","terror",1999)
        filme.adicionar_filme(444444,"Homem Aranha","acao",1999)
        filmes = filme.listar_filmes()
        self.assertEqual(2, len(filmes))

    def test_remover_filme(self):
        filme.adicionar_filme(444444,"Homem Aranha","acao",1999)
        filme.remover_filme(444444)
        filmes = filme.listar_filmes()
        self.assertEqual(0, len(filmes))

    def test_buscar_filme(self):
        filme.adicionar_filme(444444,"Homem Aranha","acao",1999)
        filme.adicionar_filme(555555,"Amadeus","terror",1999)
        f = filme.buscar_filme(444444)
        self.assertEqual("Homem Aranha", f[1])
        self.assertEqual("acao", f[2])
        self.assertEqual(1999, f[3])

    def test_buscar_filme_por_genero(self):
        filme.adicionar_filme(444444,"Homem Aranha","acao",1999)
        filme.adicionar_filme(555555,"Amadeus","terror",1999)
        f = filme.buscar_filme_por_genero("acao")
        self.assertEqual(444444, f[0])
        self.assertEqual("Homem Aranha", f[1])
        self.assertEqual(1999, f[3])

if __name__ == '__main__':
    unittest.main(exit=False)
