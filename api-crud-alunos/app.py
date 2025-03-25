from flask import Flask
from models import db, Aluno

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()  # Cria a tabela no banco de dados

from flask import Flask, request, jsonify
from models import db, Aluno

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Listar Alunos Cadastrados (READ)
@app.route('/alunos', methods=['GET'])
def listar_alunos():
    alunos = Aluno.query.all()
    return jsonify([{
        "aluno_id": aluno.aluno_id,
        "nome": aluno.nome,
        "endereco": aluno.endereco,
        "cidade": aluno.cidade,
        "estado": aluno.estado,
        "cep": aluno.cep,
        "pais": aluno.pais,
        "telefone": aluno.telefone
    } for aluno in alunos])

# Cadastrar Novos Alunos (CREATE)
@app.route('/alunos', methods=['POST'])
def cadastrar_aluno():
    data = request.json
    novo_aluno = Aluno(
        aluno_id=data['aluno_id'],
        nome=data['nome'],
        endereco=data.get('endereco'),
        cidade=data.get('cidade'),
        estado=data.get('estado'),
        cep=data.get('cep'),
        pais=data.get('pais'),
        telefone=data.get('telefone')
    )
    db.session.add(novo_aluno)
    db.session.commit()
    return jsonify({"message": "Aluno cadastrado com sucesso!"}), 201

# Alterar Dados de Alunos Cadastrados (UPDATE)
@app.route('/alunos/<aluno_id>', methods=['PUT'])
def alterar_aluno(aluno_id):
    aluno = Aluno.query.filter_by(aluno_id=aluno_id).first()
    if not aluno:
        return jsonify({"message": "Aluno não encontrado!"}), 404

    data = request.json
    aluno.nome = data.get('nome', aluno.nome)
    aluno.endereco = data.get('endereco', aluno.endereco)
    aluno.cidade = data.get('cidade', aluno.cidade)
    aluno.estado = data.get('estado', aluno.estado)
    aluno.cep = data.get('cep', aluno.cep)
    aluno.pais = data.get('pais', aluno.pais)
    aluno.telefone = data.get('telefone', aluno.telefone)

    db.session.commit()
    return jsonify({"message": "Dados do aluno atualizados com sucesso!"})

# Excluir Alunos (DELETE)
@app.route('/alunos/<aluno_id>', methods=['DELETE'])
def excluir_aluno(aluno_id):
    aluno = Aluno.query.filter_by(aluno_id=aluno_id).first()
    if not aluno:
        return jsonify({"message": "Aluno não encontrado!"}), 404

    db.session.delete(aluno)
    db.session.commit()
    return jsonify({"message": "Aluno excluído com sucesso!"})
