import unittest
import filme

class TesteFilme(unittest.TestCase):

    def setUp(self):
        filme.remover_todos_filmes()

    def teste_sem_filmes(self):
        filmes = filme.listar_filmes()
        self.assertEqual(0,len(filmes))



if __name__ == '__main__':
    unittest.main(exit=False)
