
class HistoriaModel:
    def __init__(self,id=None,titulo=None,content=None):
        self.id = id
        self.titulo = titulo
        self.content = content

    def to_json(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "content": self.content,
        } if self.id is not None else {
            "titulo": self.titulo,
            "content": self.content,
        }