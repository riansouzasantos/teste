from users import database

class Usuario(database.Model):
    id_usuario = database.Column(database.Integer, primary_key=True)
    nome = database.Column(database.String, nullable=True, unique=False)
    email = database.Column(database.String, nullable=True, unique=False)
    telefone = database.Column(database.String, nullable=True, unique=False)
