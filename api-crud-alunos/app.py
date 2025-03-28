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

 #Para executar os testes turma 

from flask import Flask, request, jsonify

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meu_banco.db'  # Substitua pelo banco usado
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Modelo Turma
class Turma(db.Model):
    __tablename__ = 'turma'
    id_turma = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_turma = db.Column(db.String(100), nullable=False)
    id_professor = db.Column(db.Integer, nullable=False)
    horario = db.Column(db.String(50), nullable=False)

# Rota para listar todas as turmas
@app.route('/turmas', methods=['GET'])
def listar_turmas():
    turmas = Turma.query.all()
    return jsonify([{
        'id_turma': turma.id_turma,
        'nome_turma': turma.nome_turma,
        'id_professor': turma.id_professor,
        'horario': turma.horario
    } for turma in turmas])

# Rota para criar uma nova turma
@app.route('/turmas', methods=['POST'])
def criar_turma():
    dados = request.json
    nova_turma = Turma(
        nome_turma=dados['nome_turma'],
        id_professor=dados['id_professor'],
        horario=dados['horario']
    )
    db.session.add(nova_turma)
    db.session.commit()
    return jsonify({'message': 'Turma criada com sucesso!'}), 201

# Rota para atualizar uma turma
@app.route('/turmas/<int:id_turma>', methods=['PUT'])
def atualizar_turma(id_turma):
    turma = Turma.query.get_or_404(id_turma)
    dados = request.json
    turma.nome_turma = dados['nome_turma']
    turma.id_professor = dados['id_professor']
    turma.horario = dados['horario']
    db.session.commit()
    return jsonify({'message': 'Turma atualizada com sucesso!'})

# Rota para deletar uma turma
@app.route('/turmas/<int:id_turma>', methods=['DELETE'])
def deletar_turma(id_turma):
    turma = Turma.query.get_or_404(id_turma)
    db.session.delete(turma)
    db.session.commit()
    return jsonify({'message': 'Turma deletada com sucesso!'})

# Inicializar o banco de dados
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)

    #Para a tabela professor
    from flask import Flask, request, jsonify

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meu_banco.db'  # Banco de dados SQLite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Modelo Professor
class Professor(db.Model):
    __tablename__ = 'professor'
    id_professor = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_completo = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    telefone = db.Column(db.String(20), nullable=False)

# Rota para listar todos os professores
@app.route('/professores', methods=['GET'])
def listar_professores():
    professores = Professor.query.all()
    return jsonify([{
        'id_professor': professor.id_professor,
        'nome_completo': professor.nome_completo,
        'email': professor.email,
        'telefone': professor.telefone
    } for professor in professores])

# Rota para criar um novo professor
@app.route('/professores', methods=['POST'])
def criar_professor():
    dados = request.json
    novo_professor = Professor(
        nome_completo=dados['nome_completo'],
        email=dados['email'],
        telefone=dados['telefone']
    )
    db.session.add(novo_professor)
    db.session.commit()
    return jsonify({'message': 'Professor criado com sucesso!'}), 201

# Rota para atualizar um professor
@app.route('/professores/<int:id_professor>', methods=['PUT'])
def atualizar_professor(id_professor):
    professor = Professor.query.get_or_404(id_professor)
    dados = request.json
    professor.nome_completo = dados['nome_completo']
    professor.email = dados['email']
    professor.telefone = dados['telefone']
    db.session.commit()
    return jsonify({'message': 'Professor atualizado com sucesso!'})

# Rota para deletar um professor
@app.route('/professores/<int:id_professor>', methods=['DELETE'])
def deletar_professor(id_professor):
    professor = Professor.query.get_or_404(id_professor)
    db.session.delete(professor)
    db.session.commit()
    return jsonify({'message': 'Professor deletado com sucesso!'})

# Inicializar o banco de dados
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)

    #codigo para pagamentos
    from flask import Flask, request, jsonify

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meu_banco.db'  # Banco de dados SQLite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Modelo Pagamento
class Pagamento(db.Model):
    __tablename__ = 'pagamento'
    id_pagamento = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_aluno = db.Column(db.Integer, nullable=False)
    data_pagamento = db.Column(db.Date, nullable=False)
    valor_pago = db.Column(db.Float, nullable=False)
    forma_pagamento = db.Column(db.String(50), nullable=False)
    referencia = db.Column(db.String(100), nullable=True)

# Rota para listar pagamentos
@app.route('/pagamentos', methods=['GET'])
def listar_pagamentos():
    pagamentos = Pagamento.query.all()
    return jsonify([{
        'id_pagamento': pagamento.id_pagamento,
        'id_aluno': pagamento.id_aluno,
        'data_pagamento': str(pagamento.data_pagamento),
        'valor_pago': pagamento.valor_pago,
        'forma_pagamento': pagamento.forma_pagamento,
        'referencia': pagamento.referencia
    } for pagamento in pagamentos])

# Rota para criar um novo pagamento
@app.route('/pagamentos', methods=['POST'])
def criar_pagamento():
    dados = request.json
    novo_pagamento = Pagamento(
        id_aluno=dados['id_aluno'],
        data_pagamento=dados['data_pagamento'],
        valor_pago=dados['valor_pago'],
        forma_pagamento=dados['forma_pagamento'],
        referencia=dados.get('referencia')
    )
    db.session.add(novo_pagamento)
    db.session.commit()
    return jsonify({'message': 'Pagamento criado com sucesso!'}), 201

# Rota para atualizar um pagamento
@app.route('/pagamentos/<int:id_pagamento>', methods=['PUT'])
def atualizar_pagamento(id_pagamento):
    pagamento = Pagamento.query.get_or_404(id_pagamento)
    dados = request.json
    pagamento.id_aluno = dados['id_aluno']
    pagamento.data_pagamento = dados['data_pagamento']
    pagamento.valor_pago = dados['valor_pago']
    pagamento.forma_pagamento = dados['forma_pagamento']
    pagamento.referencia = dados.get('referencia')
    db.session.commit()
    return jsonify({'message': 'Pagamento atualizado com sucesso!'})

# Rota para deletar um pagamento
@app.route('/pagamentos/<int:id_pagamento>', methods=['DELETE'])
def deletar_pagamento(id_pagamento):
    pagamento = Pagamento.query.get_or_404(id_pagamento)
    db.session.delete(pagamento)
    db.session.commit()
    return jsonify({'message': 'Pagamento deletado com sucesso!'})

# Inicializar o banco de dados
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)

    #Crude para os alunos 
    from flask import Flask, request, jsonify

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meu_banco.db'  # Banco de dados SQLite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Modelo Presenca
class Presenca(db.Model):
    __tablename__ = 'presenca'
    id_presenca = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_aluno = db.Column(db.Integer, nullable=False)
    data_presenca = db.Column(db.Date, nullable=False)
    presente = db.Column(db.Boolean, nullable=False)

# Rota para listar todas as presenças
@app.route('/presencas', methods=['GET'])
def listar_presencas():
    presencas = Presenca.query.all()
    return jsonify([{
        'id_presenca': presenca.id_presenca,
        'id_aluno': presenca.id_aluno,
        'data_presenca': str(presenca.data_presenca),
        'presente': presenca.presente
    } for presenca in presencas])

# Rota para criar uma nova presença
@app.route('/presencas', methods=['POST'])
def criar_presenca():
    dados = request.json
    nova_presenca = Presenca(
        id_aluno=dados['id_aluno'],
        data_presenca=dados['data_presenca'],
        presente=dados['presente']
    )
    db.session.add(nova_presenca)
    db.session.commit()
    return jsonify({'message': 'Presença criada com sucesso!'}), 201

# Rota para atualizar uma presença
@app.route('/presencas/<int:id_presenca>', methods=['PUT'])
def atualizar_presenca(id_presenca):
    presenca = Presenca.query.get_or_404(id_presenca)
    dados = request.json
    presenca.id_aluno = dados['id_aluno']
    presenca.data_presenca = dados['data_presenca']
    presenca.presente = dados['presente']
    db.session.commit()
    return jsonify({'message': 'Presença atualizada com sucesso!'})

# Rota para deletar uma presença
@app.route('/presencas/<int:id_presenca>', methods=['DELETE'])
def deletar_presenca(id_presenca):
    presenca = Presenca.query.get_or_404(id_presenca)
    db.session.delete(presenca)
    db.session.commit()
    return jsonify({'message': 'Presença deletada com sucesso!'})

# Inicializar o banco de dados
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)

    from flask import Flask, request, jsonify

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meu_banco.db'  # Banco de dados SQLite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Modelo Atividade
class Atividade(db.Model):
    __tablename__ = 'atividade'
    id_atividade = db.Column(db.Integer, primary_key=True, autoincrement=True)
    descricao = db.Column(db.String(255), nullable=False)
    data_realizacao = db.Column(db.Date, nullable=False)

# Rota para listar todas as atividades
@app.route('/atividades', methods=['GET'])
def listar_atividades():
    atividades = Atividade.query.all()
    return jsonify([{
        'id_atividade': atividade.id_atividade,
        'descricao': atividade.descricao,
        'data_realizacao': str(atividade.data_realizacao)
    } for atividade in atividades])

# Rota para criar uma nova atividade
@app.route('/atividades', methods=['POST'])
def criar_atividade():
    dados = request.json
    nova_atividade = Atividade(
        descricao=dados['descricao'],
        data_realizacao=dados['data_realizacao']
    )
    db.session.add(nova_atividade)
    db.session.commit()
    return jsonify({'message': 'Atividade criada com sucesso!'}), 201

# Rota para atualizar uma atividade
@app.route('/atividades/<int:id_atividade>', methods=['PUT'])
def atualizar_atividade(id_atividade):
    atividade = Atividade.query.get_or_404(id_atividade)
    dados = request.json
    atividade.descricao = dados['descricao']
    atividade.data_realizacao = dados['data_realizacao']
    db.session.commit()
    return jsonify({'message': 'Atividade atualizada com sucesso!'})

# Rota para deletar uma atividade
@app.route('/atividades/<int:id_atividade>', methods=['DELETE'])
def deletar_atividade(id_atividade):
    atividade = Atividade.query.get_or_404(id_atividade)
    db.session.delete(atividade)
    db.session.commit()
    return jsonify({'message': 'Atividade deletada com sucesso!'})

# Inicializar o banco de dados
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)

    from flask import Flask, request, jsonify

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meu_banco.db'  # Banco SQLite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Rota para listar todos os usuários
@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    usuarios = Usuario.query.all()
    return jsonify([{
        'id_usuario': usuario.id_usuario,
        'login': usuario.login,
        'nivel_acesso': usuario.nivel_acesso,
        'id_professor': usuario.id_professor
    } for usuario in usuarios])

# Rota para criar um novo usuário
@app.route('/usuarios', methods=['POST'])
def criar_usuario():
    dados = request.json
    novo_usuario = Usuario(
        login=dados['login'],
        senha=dados['senha'],  # Idealmente, use uma função de hash para senhas
        nivel_acesso=dados['nivel_acesso'],
        id_professor=dados.get('id_professor')  # Opcional
    )
    db.session.add(novo_usuario)
    db.session.commit()
    return jsonify({'message': 'Usuário criado com sucesso!'}), 201

# Rota para atualizar um usuário existente
@app.route('/usuarios/<int:id_usuario>', methods=['PUT'])
def atualizar_usuario(id_usuario):
    usuario = Usuario.query.get_or_404(id_usuario)
    dados = request.json
    usuario.login = dados['login']
    usuario.senha = dados['senha']  # Atualize com a senha hash aqui
    usuario.nivel_acesso = dados['nivel_acesso']
    usuario.id_professor = dados.get('id_professor')  # Opcional
    db.session.commit()
    return jsonify({'message': 'Usuário atualizado com sucesso!'})

# Rota para deletar um usuário
@app.route('/usuarios/<int:id_usuario>', methods=['DELETE'])
def deletar_usuario(id_usuario):
    usuario = Usuario.query.get_or_404(id_usuario)
    db.session.delete(usuario)
    db.session.commit()
    return jsonify({'message': 'Usuário deletado com sucesso!'})

# Inicializar o banco de dados
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
    