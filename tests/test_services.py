import unittest
from unittest.mock import MagicMock
from services import HistoriaService
from model import HistoriaModel
from dao import HistoriaDAO

class TestHistoriaService(unittest.TestCase):
    def setUp(self):
        # Configurar mocks ou instâncias necessárias para os testes
        self.mock_dao = MagicMock(spec=HistoriaDAO)
        self.service = HistoriaService(self.mock_dao)

    def test_excluir_historia_por_id(self):
        # Exemplo de teste para o método excluir_historia_por_id
        historia_id = 1
        self.service.excluir_historia_por_id(historia_id)
        self.mock_dao.delete_by_id.assert_called_once_with(historia_id)

    def test_criar_historia_gpt(self):
        # Verifica se o que está sendo retornado é uma string
        
        #self.mock_dao.create.return_value = HistoriaModel(id=1, **gpt_data)
        result = self.service.criar_historia_gpt()
        self.assertIsInstance(result.titulo, str)
        self.assertIsInstance(result.content, str)


    def test_obter_todas_historias(self):
        # Verifica se todas as historias (história 1 e história 2 estão sendo retornadas)
        historia_mock1 = HistoriaModel(id=1, titulo="História 1", content="Conteúdo 1")
        historia_mock2 = HistoriaModel(id=2, titulo="História 2", content="Conteúdo 2")
        self.mock_dao.find_all.return_value = [historia_mock1, historia_mock2]

        result = self.service.obter_todas_historias()

        self.assertEqual(result, [historia_mock1, historia_mock2])

if __name__ == '__main__':
    unittest.main()
