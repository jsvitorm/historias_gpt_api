from typing import Union, List
from dao import HistoriaDAO
from gptAPI import Gpt
from model import HistoriaModel


class HistoriaService:
    def __init__(self, historia_dao: HistoriaDAO):
        self.historia_dao = historia_dao

    def encontrar_historia_por_id(self, historia_id: int) -> Union[HistoriaModel, None]:
        return self.historia_dao.find_by_id(historia_id)
    
    def obter_todas_historias(self) -> List[HistoriaModel]:
        return self.historia_dao.find_all()

    def criar_historia(self, titulo: str, content: str) -> HistoriaModel:
        nova_historia = HistoriaModel(id=None, titulo=titulo, content=content)
        self.historia_dao.create(nova_historia)
        return nova_historia
    
    def criar_historia_gpt(self) -> HistoriaModel:
        gpt_data = Gpt.gerar_historia()
        nova_historia = HistoriaModel(titulo=gpt_data["titulo"], content=gpt_data["content"])
        self.historia_dao.create(nova_historia)
        return nova_historia

    def excluir_historia_por_id(self, historia_id: int) -> None:
        self.historia_dao.delete_by_id(historia_id)


