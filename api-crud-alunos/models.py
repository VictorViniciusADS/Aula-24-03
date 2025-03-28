from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Aluno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    aluno_id = db.Column(db.String(5), nullable=False, unique=True)
    nome = db.Column(db.String(40), nullable=False)
    endereco = db.Column(db.String(60))
    cidade = db.Column(db.String(15))
    estado = db.Column(db.String(15))
    cep = db.Column(db.String(10))
    pais = db.Column(db.String(15))
    telefone = db.Column(db.String(24))

    def __repr__(self):
        return f'<Aluno {self.nome}>'
    
    from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Turma(db.Model):
    __tablename__ = 'turma'
    id_turma = db.Column(db.Integer, primary_key=True, autoincrement=True)  # Chave Primária
    nome_turma = db.Column(db.String(100), nullable=False)  # Nome da turma
    id_professor = db.Column(db.Integer, nullable=False)  # ID do professor
    horario = db.Column(db.String(50), nullable=False)  # Horário da turma 

from flask_sqlalchemy import SQLAlchemy

#professor 
db = SQLAlchemy()

class Professor(db.Model):
    __tablename__ = 'professor'
    id_professor = db.Column(db.Integer, primary_key=True, autoincrement=True)  # ID único (PK)
    nome_completo = db.Column(db.String(255), nullable=False)  # Nome completo
    email = db.Column(db.String(100), nullable=False, unique=True)  # Email único
    telefone = db.Column(db.String(20), nullable=False)  # Telefone

#Pagamento 
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Pagamento(db.Model):
    __tablename__ = 'pagamento'
    id_pagamento = db.Column(db.Integer, primary_key=True, autoincrement=True)  # ID do Pagamento (PK)
    id_aluno = db.Column(db.Integer, nullable=False)  # ID do Aluno
    data_pagamento = db.Column(db.Date, nullable=False)  # Data do Pagamento
    valor_pago = db.Column(db.Float, nullable=False)  # Valor Pago
    forma_pagamento = db.Column(db.String(50), nullable=False)  # Forma de Pagamento
    referencia = db.Column(db.String(100), nullable=True)  # Referência (opcional)

    #Presença dos alunos 
    from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Presenca(db.Model):
    __tablename__ = 'presenca'
    id_presenca = db.Column(db.Integer, primary_key=True, autoincrement=True)  # ID único
    id_aluno = db.Column(db.Integer, nullable=False)  # ID do aluno
    data_presenca = db.Column(db.Date, nullable=False)  # Data da presença
    presente = db.Column(db.Boolean, nullable=False)  # Presente (True/False)

#Atividade do aluno
    from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class AtividadeAluno(db.Model):
    __tablename__ = 'atividade_aluno'
    id_atividade = db.Column(db.Integer, primary_key=True)  # Chave estrangeira para Atividade
    id_aluno = db.Column(db.Integer, primary_key=True)  # Chave estrangeira para Aluno

    #Usuarios e Usuarios Professor
    from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Usuario(db.Model):
    __tablename__ = 'usuario'
    id_usuario = db.Column(db.Integer, primary_key=True, autoincrement=True)  # ID único
    login = db.Column(db.String(50), nullable=False, unique=True)  # Login (único)
    senha = db.Column(db.String(255), nullable=False)  # Senha
    nivel_acesso = db.Column(db.String(20), nullable=False)  # Nível de acesso
    id_professor = db.Column(db.Integer, db.ForeignKey('professor.id_professor'), nullable=True)  # FK para Professor (opcional)

    professor = db.relationship('Professor', backref='usuarios')  # Relacionamento com Professor