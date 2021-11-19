from app import db

class Pessoa(db.Model):
    __tablename__ = 'pessoas'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    idade = db.Column(db.Integer)
    sexo = db.Column(db.String(1))
    salario = db.Column(db.Float)

    def __init__(self, nome='Anônimo', idade=18, sexo='M', salario=1.039):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.salario = salario
    
    def __repr__(self):
        return '<Pessoa %r>' % self.nome

import pandas as pd

class Restaurante():
    __tablename__= 'restaurante'

    x = pd.read_csv(r"C:\Users\artur\Downloads\05-templates\dados\Fast_Food_Restaurants_US.csv")

    id = x['id']