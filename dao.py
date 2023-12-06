
import mysql.connector
from mysql.connector import Error
from typing import Union, List

from model import HistoriaModel 


class HistoriaDAO:

    def __init__(self):
        self.connection = None
        self.cursor = None

    def conectar(self, host, database, user, password):
        self.connection = mysql.connector.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )
        self.cursor = self.connection.cursor()
    
    def find_by_id(self,historia_id: int ):
        try:
            query = "SELECT * FROM historias WHERE id = %s"
            self.cursor.execute(query, (historia_id,))
            result = self.cursor.fetchone()

            if result:
                historia = HistoriaModel(result[1], result[2])  
                historia.id = result[0]
                return historia
            else:
                return None
        
        except Error as e:
            print(f"Erro ao buscar história por ID: {e}")
            return None
        
    
    def find_all(self) -> List[HistoriaModel]:
        try:
            query = "SELECT * FROM historias"
            self.cursor.execute(query)
            results = self.cursor.fetchall()

            historias = [HistoriaModel(id=row[0], titulo=row[1], content=row[2]) for row in results]
            return historias

        except Error as e:
            print(f"Erro ao buscar todas as histórias: {e}")
            return []


    def create(self, historia: HistoriaModel):
        try:
            query = "INSERT INTO historias (titulo, content) VALUES (%s, %s)"
            values = (historia.titulo, historia.content)
            self.cursor.execute(query, values)
            self.connection.commit()
            historia.id = self.cursor.lastrowid

        except Error as e:
            print(f"Erro ao criar história: {e}")


    def delete_by_id(self, historia_id:int):
        try:
            query = "DELETE FROM historias WHERE id = %s"
            self.cursor.execute(query, (historia_id,))
            self.connection.commit()

        except Error as e:
            print(f"Erro ao excluir história por ID: {e}")
            