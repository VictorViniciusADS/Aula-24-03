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
