# Estrutura do banco de dados as rotas

from pythonrest import database

from datetime import datetime
class Usuario(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, nullable=False)
    email= database.Column(database.String, nullable=False, unique=True)
    password= database.Column(database.String, nullable=False)
    fotos = database.relationship("Foto", backref="usuario", lazy=True)


class Foto(database.Model):
   id = database.Column(database.Integer, primary_key=True)
   imagem= database.Column(database.String, nullable=False,default="default=png")
   data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.utcnow())
   id_usuario = database.Column(database.Integer,  database.ForeignKey('usuario.id'), nullable = False)






