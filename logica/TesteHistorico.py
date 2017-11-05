import unittest
import historico

class TesteHistorico(unittest.TestCase):

    def setUp(self):
        historico.limpar_historico()

    def test_sem_registro(self):
        historico = historico.listar_filmes_assistidos(12093102)
        self.assertEqual(0,len(historico))

if __name__ == '__main__':
    unittest.main(exit = False)
