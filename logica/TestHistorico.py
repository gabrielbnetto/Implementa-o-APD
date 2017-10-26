import unittest
import historico
import filme

class TestHistorico(unittest.TestCase):

    def setUp(self):
        historico.limpar_historico()

    def test_sem_registro(self):
        historicos = historico.listar_filmes_assistidos(555555)
        self.assertEqual(0,len(historicos))

    def test_adicionar_um_registro(self):
        filme.iniciar_filmes()
        historico.registrar_filme_assistido(555555,555555)
        historicos = historico.listar_filmes_assistidos(555555)
        self.assertEqual(1,len(historicos))

        h = historicos[0]
        self.assertEqual("Amadeus",h)

    def test_adicionar_dois_resgistros(self):
        filme.iniciar_filmes()
        historico.registrar_filme_assistido(444444,555555)
        historico.registrar_filme_assistido(444444,444444)
        historicos = historico.listar_filmes_assistidos(444444)
        self.assertEqual(2,len(historicos))

        self.assertEqual("Amadeus",historicos[0])
        self.assertEqual("Homem Aranha",historicos[1])

    def buscar_historico_por_cpf(self):
        filme.iniciar_filmes()
        historico.registrar_filme_assistido(444444,555555)
        historico.registrar_filme_assistido(555555,444444)
        historico1 = historico.listar_filmes_assistidos(444444)
        historico2 = historico.listar_filmes_assistidos(555555)

        self.assertEqual("Amadeus",historico1[0])
        self.assertEqual("Homem Aranha",historico2[0])
        

if __name__ == '__main__':
    unittest.main(exit=False)
