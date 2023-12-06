from flask import Flask, jsonify, request
from dao import HistoriaDAO
from services import HistoriaService
from model import HistoriaModel

app = Flask(__name__)


db_config = {
        "host":"database-3.c86pb1hq4aoj.us-east-1.rds.amazonaws.com",
        "database":"ponderada",
        "user":"admin",
        "password":"senha123"
}

# Crie uma instância de HistoriaDAO e conecte-a ao banco de dados
historia_dao = HistoriaDAO()
historia_dao.conectar(**db_config)

historia_service = HistoriaService(historia_dao)

@app.route('/gethistorias/<int:historia_id>', methods=['GET'])
def obter_historia(historia_id):
    historia = historia_service.encontrar_historia_por_id(historia_id)
    return jsonify(historia.to_json()) if historia else jsonify({"message": "História não encontrada"}), 404

@app.route('/gettodashistorias', methods=['GET'])
def obter_todas_historias():
    historias = historia_service.obter_todas_historias()
    return jsonify([historia.to_json() for historia in historias])

@app.route('/createhistorias', methods=['POST'])
def criar_historia():
    data = request.json
    nova_historia = historia_service.criar_historia(data.get('titulo'), data.get('content'))
    return jsonify(nova_historia.to_json()), 201

@app.route('/createhistoriagpt', methods=['POST'])
def criar_historia_gpt():
    nova_historia = historia_service.criar_historia_gpt()
    return jsonify(nova_historia.to_json()), 201

@app.route('/deletehistorias/<int:historia_id>', methods=['DELETE'])
def excluir_historia(historia_id):
    historia_service.excluir_historia_por_id(historia_id)
    return jsonify({"message": f"História {historia_id} excluída"}), 200

if __name__ == '__main__':
    app.run(debug=True)
